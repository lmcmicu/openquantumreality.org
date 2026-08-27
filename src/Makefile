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

templates := $(wildcard *.jinja2)

all: $(templates:%.jinja2=../html/%.html)

../html/%.html: %.jinja2
	python3 generate_html_from_template.py $^ $@
