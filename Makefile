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
.DELETE_ON_ERROR:
.SUFFIXES:

jinja2_files := $(wildcard src/*.jinja2)
jinja2_testfiles := $(wildcard test/src/*.jinja2)
markdown_files := $(wildcard markdown/*.md)
template_files := $(wildcard templates/*.md)
html_files := $(wildcard html/*.md)
html_testfiles := $(wildcard test/html/*.html)

.PHONY: all reinit test_setup build_test test test clean

all: $(jinja2_files:src/%.jinja2=html/%.html)

reinit:
	rm -Rf markdown
	cp -rp templates markdown

html/%.html: src/%.jinja2 $(markdown_files:markdown/%.md=src/%-from-markdown.html)
	python3 jinja2html.py $< $@

src/%-from-markdown.html: markdown/%.md
	python3 markdown2html.py $< $@

test: build_test | test/html test/src
	@for htmlfile in $(notdir $(html_testfiles)); \
	do \
		diff --strip-trailing-cr -Z -s -q test/html/$$htmlfile templates_html/$$htmlfile || exit 1 ; \
	done

build_test: $(jinja2_testfiles:test/src/%.jinja2=test/html/%.html)
	@echo "Test files copied. Please run ~make test~ again (yes I know this is the second time)."

test/html:
	mkdir -p $@

test/src:
	mkdir -p $@
	cp -f src/*.jinja2 src/bootstrap* src/navbar-fragment.html src/page-footer.html $@
	@echo "Test directory created. Please run ~make test~ again."

test/html/%.html: test/src/%.jinja2 $(template_files:templates/%.md=test/src/%-from-markdown.html)
	python3 jinja2html.py $< $@

test/src/%-from-markdown.html: templates/%.md
	python3 markdown2html.py $< $@

clean:
	rm -Rf test

