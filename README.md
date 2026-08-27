# Updating web pages

Either [in GitHub](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files) or offline:

1. Edit one or more of the `.md` files in the [`markdown/`](https://github.com/lmcmicu/openquantumreality.org/tree/main/markdown) directory.

2. Commit your changes and open a pull request in GitHub. If you need to link any images or other resources (PDF files, etc.), send these to whoever has access to the web server. 

On the web server:

3. Add any images or other required resources (PDF files, etc.) to the `html/resources/` directory.

4. Navigate to the `www/` directory, update the source code using `git pull`, and recompile it using `make` (or `make -B`):

        <b>(mike@sudarshan ~)$ cd www</b>
        <b>(mike@sudarshan <main> www)$ git pull</b>
        remote: Enumerating objects: 5, done.
        remote: Counting objects: 100% (5/5), done.
        remote: Compressing objects: 100% (1/1), done.
		remote: Total 3 (delta 2), reused 3 (delta 2), pack-reused 0 (from 0)
		Unpacking objects: 100% (3/3), 309 bytes | 154.00 KiB/s, done.
		From github.com:lmcmicu/openquantumreality.org
		   f1b1ef4..3524982  main       -> origin/main
		Updating f1b1ef4..3524982
		Fast-forward
		 markdown2html.py | 4 ++--
		 1 file changed, 2 insertions(+), 2 deletions(-)
		<b>(mike@sudarshan <main> www)$ make -B</b>
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
