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

MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.DEFAULT_GOAL := all
# .DELETE_ON_ERROR:
.SUFFIXES:

markdown_files := $(wildcard markdown/*.md)
html_files := $(wildcard html/*.html)
jinja2_files := $(wildcard src/*.jinja2)

template_markdown_files := $(wildcard templates/markdown/*.md)
# TODO: Do we really need these two?
template_html_files := $(wildcard templates/html/*.html)
template_jinja2_files := $(wildcard templates/src/*.jinja2)

test_html_files := $(wildcard test/html/*.html)
test_jinja2_files := $(wildcard test/src/*.jinja2)

.PHONY: all reinit clean test

# Make all the pages in the html/ directory:

all: $(jinja2_files:src/%.jinja2=html/%.html)

html/%.html: src/%.jinja2 $(markdown_files:markdown/%.md=src/%-from-markdown.html)
	python3 jinja2html.py $< $@

src/%-from-markdown.html: markdown/%.md
	python3 markdown2html.py $< $@

# Reinitialize the files in the markdown directory using the templates.
reinit:
	rm -Rf markdown
	cp -rp templates/markdown markdown

# Test the source code using the contents of the templates/ directory.

test: $(template_jinja2_files:templates/src/%.jinja2=test/html/%.html)

test/html:
	mkdir -p $@

test/html/%.html: templates/src/%.jinja2 | test/html
	python3 jinja2html.py $< $@
	diff --strip-trailing-cr -Z -q $@ templates/html/$(@F) || exit 1 ; \

clean:
	rm -Rf test

