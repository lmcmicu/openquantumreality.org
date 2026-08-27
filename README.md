# Updating a web page

1. Edit the desired `.md` file in the `markdown/` directory as needed using your favourite editor. E.g.,

        $ vi markdown/index.md

2. If necessary, add any linked-to binary files or other resources to the `html/resources/` directory.

3. Compile the source code:

        $ make
	    python3 markdown2html.py markdown/events.md src/events-from-markdown.html
	    python3 markdown2html.py markdown/index.md src/index-from-markdown.html
	    python3 markdown2html.py markdown/join.md src/join-from-markdown.html
	    python3 markdown2html.py markdown/news.md src/news-from-markdown.html
	    python3 markdown2html.py markdown/research.md src/research-from-markdown.html
	    python3 markdown2html.py markdown/team.md src/team-from-markdown.html
	    python3 jinja2html.py src/events.jinja2 html/events.html
	    python3 jinja2html.py src/index.jinja2 html/index.html
	    python3 jinja2html.py src/join.jinja2 html/join.html
	    python3 jinja2html.py src/news.jinja2 html/news.html
	    python3 jinja2html.py src/research.jinja2 html/research.html
	    python3 jinja2html.py src/team.jinja2 html/team.html
