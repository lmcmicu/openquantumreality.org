# Updating web pages

**Either [in GitHub](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files) or offline:**

1. Edit one or more of the `.md` files in the [`markdown/`](https://github.com/lmcmicu/openquantumreality.org/tree/main/markdown) directory.

2. **If you are editing offline**, [commit](https://git-scm.com/docs/git-commit) your changes to a new branch and then [push](https://git-scm.com/docs/git-push) your branch to GitHub. You will then need to [open a pull request](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request) to merge your branch to the [main branch](https://github.com/lmcmicu/openquantumreality.org/tree/main). **If you are editing a file [using GitHub](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)** all of this should be taken care of automatically (but you will be asked to confirm each step).

3. If you need to link to an image or some other web content (a PDF file, audio / video file, etc.), send these by email to the web server administrator

**On the web server (only for the web site admin):**

1. Add any images or other required resources (PDF files, videos, etc.) to the `html/resources/` directory.

2. Navigate to the `www/` directory, update the source code using `git pull`, and recompile it using `make` (or `make -B`):
<pre>
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
</pre>

3. Check the output in the `html/` directory and adjust the edited `.md` file as necessary.
