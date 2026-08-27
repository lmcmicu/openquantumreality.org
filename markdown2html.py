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

# This is what we need to generate:
# <div class="container text-center">
#   <h1>Welcome to openquantumreality.org!</h1>
#   <hr/>
#   <div class="row align-items-start" style="margin-bottom: 60px">
#     <div class="col-sm">
#       You have found the web site of the John Templeton Foundation-funded project:
#       <i>Open Quantum Systems and the Causal Structure of Reality</i>.
#     </div>
#     <div class="col-sm">
#       These pages are currently under construction. Please check back later for updates.
#     </div>
#   </div>
# </div>


def main():
    parser = argparse.ArgumentParser(
        description='Generate an output HTML file from a Jinja2 template'
    )
    parser.add_argument('INPUT', type=str, help='the input Jinja2 template file')
    parser.add_argument('OUTPUT', type=str, help='the output HTML file')
    # args = parser.parse_args()


if __name__ == "__main__":
    main()
