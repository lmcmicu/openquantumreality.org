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

from markdown import Markdown

import argparse
import os.path
import re


def main():
    parser = argparse.ArgumentParser(
        description='Generate an output HTML file from a markdown file'
    )
    parser.add_argument('INPUT', type=str, help='the input markdown file')
    parser.add_argument('OUTPUT', type=str, help='the output HTML file')
    args = parser.parse_args()

    with open(args.INPUT) as ip:
        lines = ip.readlines()
        header = ""
        body = ""
        for line in lines:
            if line.strip():
                if not header and line.startswith("# "):
                    header = line.strip().removeprefix('# ')
                else:
                    body += line

    if not header:
        # If the header can't be read, use the filename:
        header = ''.join(args.INPUT.rsplit('.', 1)[:-1])
        header = os.path.basename(header).replace('_', ' ').capitalize()

    markdown_parser = Markdown()
    is_p_start = re.compile(r"<\s*[pP]\s*>")
    is_p_end = re.compile(r"<\s*/p\s*>")

    def convert(markdown):
        html = markdown_parser.convert(markdown)
        html = is_p_start.sub('<p>', html)
        html = is_p_end.sub("</p>", html)
        return html

    is_space = re.compile(r"\s")
    body_len = len(body)
    cutoff_index = round(body_len / 2)
    while cutoff_index < body_len and not is_space.fullmatch(body[cutoff_index]):
        cutoff_index += 1

    if body_len > 500:
        columns = f"""
        <div class="col-sm-6" style="text-align: left;">
            {convert(body[:cutoff_index])}
        </div>
        <div class="col-sm-6" style="text-align: left;">
            {convert(body[cutoff_index:])}
        </div>""".lstrip()
    else:
        columns = f"""
        <div class="col-sm-3">&nbsp;</div>
        <div class="col-sm-6">
            {convert(body)}
        </div>
        <div class="col-sm-3">&nbsp;</div>""".lstrip()

    contents = f"""
    <div class="container text-center">
        <h1>{header}</h1>
        <hr/>
        <div class="row align-items-start" style="margin-bottom: 60px">
            {columns}
        </div>
    </div>""".lstrip()

    with open(args.OUTPUT, "w") as op:
        print(contents, file=op)


if __name__ == "__main__":
    main()
