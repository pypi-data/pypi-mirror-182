"""Compute minimal trap-spaces of a Petri-net encoded Boolean model.

Copyright (C) 2022 Sylvain.Soliman@inria.fr and giang.trinh91@gmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as etree
from typing import Generator, IO, List, Optional

import networkx as nx  # TODO maybe replace with lists/dicts

from . import version


def read_pnml(fileobj: IO) -> nx.DiGraph:
    """Parse the given file."""
    root = etree.parse(fileobj).getroot()
    if root.tag != "pnml":
        raise ValueError("Currently limited to parsing PNML files")
    net = nx.DiGraph()

    for place in root.findall("./net/place"):
        net.add_node(
            place.get("id"), kind="place"  # , name=place.find("./name/value").text
        )

    for transition in root.findall("./net/transition"):
        net.add_node(transition.get("id"), kind="transition")

    for arc in root.findall("./net/arc"):
        net.add_edge(arc.get("source"), arc.get("target"))

    return net


def pnml_to_asp(name: str) -> str:
    """Convert a PNML id to an ASP variable."""
    # TODO handle non-accetable chars
    if name.startswith("-"):
        return "n" + name[1:]
    return "p" + name


def write_asp(petri_net: nx.DiGraph, asp_file: IO):
    """Write the ASP program for the maximal conflict-free siphons of petri_net."""
    for node, kind in petri_net.nodes(data="kind"):
        if kind == "place":
            print("{", pnml_to_asp(node), "}.", file=asp_file, sep="")
            if not node.startswith("-"):
                print(
                    f":- {pnml_to_asp(node)}, {pnml_to_asp('-' + node)}.", file=asp_file
                )  # conflict-freeness
        else:  # it's a transition, apply siphon (if one succ is true, one pred must be true)
            preds = list(petri_net.predecessors(node))
            or_preds = "; ".join(map(pnml_to_asp, preds))
            for succ in petri_net.successors(node):
                if succ not in preds:  # optimize obvious tautologies
                    print(f"{or_preds} :- {pnml_to_asp(succ)}.", file=asp_file)


def solve_asp(asp_filename: str, max_output: int, time_limit: int) -> str:
    """Run an ASP solver on program asp_file and get the solutions."""
    result = subprocess.run(
        [
            "clingo",
            str(max_output),
            "--heuristic=Domain",  # maximal w.r.t. inclusion
            "--enum-mod=domRec",
            "--dom-mod=3",
            "--outf=2",  # json output
            f"--time-limit={time_limit}",
            asp_filename,
        ],
        capture_output=True,
        text=True,
    )

    # https://www.mat.unical.it/aspcomp2013/files/aspoutput.txt
    # 30: SAT, all enumerated, optima found, 10 stopped by max
    if result.returncode != 30 and result.returncode != 10:
        print(f"Return code from clingo: {result.returncode}")
        result.check_returncode()  # will raise CalledProcessError

    return result.stdout


def solution_to_bool(places: List[str], sol: List[str]) -> List[str]:
    """Convert a list of present places in sol, to a tri-valued vector."""
    return [place_in_sol(sol, p) for p in places]


def place_in_sol(sol: List[str], place: str) -> str:
    """Return 0/1/- if place is absent, present or does not appear in sol.

    Remember that being in the siphon means staying empty, so the opposite value is the one fixed.
    """
    if "p" + place in sol:
        return "0"
    if "n" + place in sol:
        return "1"
    return "-"


def get_solutions(
    asp_output: str, petri_net: nx.DiGraph, display: bool
) -> Optional[Generator[List[str], None, None]]:
    """Display the ASP output back as trap-spaces."""
    places = []
    for node, kind in petri_net.nodes(data="kind"):
        if kind == "place" and not node.startswith("-"):
            places.append(node)
    if display:
        print(" ".join(places))
    solutions = json.loads(asp_output)
    if display:
        print(
            "\n".join(
                " ".join(solution_to_bool(places, sol["Value"]))
                for sol in solutions["Call"][0]["Witnesses"]
            )
        )
        print("Total time:", solutions["Time"]["Total"], "s")
        return None
    else:
        return (
            solution_to_bool(places, sol["Value"])
            for sol in solutions["Call"][0]["Witnesses"]
        )


def compute_trap_spaces(
    infile: IO, display: bool = False, max_output: int = 0, time_limit: int = 0
) -> Optional[Generator[List[str], None, None]]:
    """Do the minimal trap-space computation on input file infile."""
    petri_net = read_pnml(infile)

    (_, tmpname) = tempfile.mkstemp(suffix=".lp", text=True)
    with open(tmpname, "wt") as asp_file:
        write_asp(petri_net, asp_file)
    solutions = solve_asp(tmpname, max_output, time_limit)
    os.unlink(tmpname)
    return get_solutions(solutions, petri_net, display)


def main():
    """Read the Petri-net send the output to ASP and print solution."""
    parser = argparse.ArgumentParser(
        description=" ".join(__doc__.splitlines()[:3]) + " GPLv3"
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s v{version}".format(version=version),
    )
    parser.add_argument(
        "-m",
        "--max",
        type=int,
        default=0,
        help="Maximum number of solutions (0 for all).",
    )
    parser.add_argument(
        "-t",
        "--time",
        type=int,
        default=0,
        help="Maximum number of seconds for search (0 for no-limit).",
    )
    parser.add_argument(
        "infile",
        type=argparse.FileType("r", encoding="utf-8"),
        nargs="?",
        default=sys.stdin,
        help="Petri-net (PNML) file",
    )
    args = parser.parse_args()

    compute_trap_spaces(
        args.infile, display=True, max_output=args.max, time_limit=args.time
    )


if __name__ == "__main__":
    main()
