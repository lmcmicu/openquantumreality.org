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

    markdown_parser = Markdown(extensions=['tables'])
    is_p_start = re.compile(r"<\s*[pP]\s*>")
    is_p_end = re.compile(r"<\s*/\s*p\s*>")
    is_br = re.compile(r"<\s*br\s*/\s*>")
    is_td = re.compile(r"<td ")
    is_th = re.compile(r"<th ")
    is_tooltip = re.compile(r'title="')

    def convert(markdown):
        html = markdown_parser.convert(markdown)
        # TODO: Do this more efficiently.
        html = is_p_start.sub('<p class="mb-4">', html)
        html = is_p_end.sub("</p>", html)
        html = is_br.sub('<span style="height: 12px; display: block;"></span>', html)
        html = is_td.sub('<td class="font-monospace fst-italic" ', html)
        html = is_th.sub('<th class="font-monospace fst-italic" ', html)
        html = is_tooltip.sub(
            'data-bs-toggle="tooltip" '
            'data-bs-delay="100" '
            'data-bs-animation="true" '
            'data-bs-html="true" '
            'title="',
            html
        )
        return html

    def get_middle_newline_index(body):
        body_len = len(body)
        index = round(body_len / 2)
        while index < body_len and body[index] != "\n":
            index += 1
        return index

    def in_block(line):
        return line.startswith("|")

    def get_lines_at_cutoff(body, cutoff_index):
        previous_index = get_prev_newline_index(body, cutoff_index)
        previous_line = body[previous_index + 1: cutoff_index]
        next_index = get_next_newline_index(body, cutoff_index)
        next_line = body[cutoff_index + 1 : next_index]
        return previous_line, previous_index, next_line, next_index

    def get_column_cutoff(body):
        cutoff_index = get_middle_newline_index(body)
        previous_line, _, next_line, next_index = get_lines_at_cutoff(
            body, cutoff_index
        )
        while in_block(previous_line) and in_block(next_line):
            cutoff_index = next_index
            previous_line, _, next_line, next_index = get_lines_at_cutoff(
                body, cutoff_index
            )
        return cutoff_index

    def get_prev_newline_index(body, newline_index):
        prev_newline_index = newline_index - 1
        while prev_newline_index > 0 and body[prev_newline_index] != "\n":
            prev_newline_index -= 1
        return prev_newline_index

    def get_next_newline_index(body, newline_index):
        next_newline_index = newline_index + 1
        while next_newline_index < len(body) and body[next_newline_index] != "\n":
            next_newline_index += 1
        return next_newline_index

    if len(body) > 500:
        # Note that this isn't perfect. You must manually inspect the beginnings and endings
        # of each generated column in the .html file to make sure that the split didn't
        # occur at a spot that would invalidate a html tag or markdown ref, for instance.
        # If there is a problem, then the fix should be as easy as adding a few newlines to the
        # .md file at around the cutoff point to force it to cutoff somewhere different. This
        # should work since whitespace is counted when determining the initial guess for the mid
        # point.
        cutoff_index = get_column_cutoff(body)
        columns = f"""
        <div class="col-sm-6" style="text-align: left;">
            {convert(body[:cutoff_index])}
        </div>
        <div class="col-sm-6" style="text-align: left;">
            {convert(body[cutoff_index:])}
        </div>""".lstrip()
        centering = ""
    else:
        columns = f"""
        <div class="col-sm-2">&nbsp;</div>
        <div class="col-sm-8">
            {convert(body)}
        </div>
        <div class="col-sm-2">&nbsp;</div>""".lstrip()
        centering = "text-center"

    contents = f"""
    <div class="container {centering}">
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
