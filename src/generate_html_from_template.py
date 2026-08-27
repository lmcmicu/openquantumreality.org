#!/usr/bin/env python3

##
# openquantumreality.org - web site for the John Templeton Foundation-funded
# project, Open Quantum Systems and the Causal Structure of Reality,
# Copyright (C) 2026 Michael E. Cuffaro.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
##

import argparse
import jinja2
import sys

from jinja2.exceptions import TemplateNotFound


def main():
    parser = argparse.ArgumentParser(
        description='Generate an output HTML file from a Jinja2 template'
    )
    parser.add_argument('INPUT', type=str, help='the input Jinja2 template file')
    parser.add_argument('OUTPUT', type=str, help='the output HTML file')
    args = parser.parse_args()

    try:
        loader = jinja2.FileSystemLoader(searchpath="./")
        env = jinja2.Environment(loader=loader)
        template = env.get_template(args.INPUT)
        html = template.render()
    except TemplateNotFound as e:
        print(f"Template not found: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Exception while loading template: {e}")
        sys.exit(1)

    try:
        with open(args.OUTPUT, "w") as outfile:
            outfile.write(html)
    except Exception as e:
        print(f"Error while writing output file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
