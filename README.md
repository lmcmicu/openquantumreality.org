# Updating web pages

**Either [in GitHub](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files) or offline:**

1. Edit one or more of the `.md` files in the [`markdown/`](https://github.com/lmcmicu/openquantumreality.org/tree/main/markdown) directory.

2. **If you are editing offline**, [commit](https://git-scm.com/docs/git-commit) your changes to a new branch and then [push](https://git-scm.com/docs/git-push) your branch to GitHub. You will then need to [open a pull request](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request) to merge your branch to the main branch. **If you are [using GitHub](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)** all of this should be taken care of automatically (but you will be asked to confirm each step).

3. If you need to link to an image or some other web content (a PDF file, audio / video file, etc.), send these by email to the web server administrator

**On the web server (only for the web server administrator):**

> [!CAUTION]
> Before making any changes to the server,
you should dry run the following steps on a development branch (you can use the branch associated with the [pull request](https://docs.github.com/en/pull-requests/reference/pull-requests) corresponding to the change) on your own workstation to be certain that that the files in the `html/` directory are being generated correctly. The below steps assume that this has been done and that the changes [have been merged](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/merging-a-pull-request) to the main branch.

1. Transfer any images or other required resources (PDF files, videos, etc.) to the `html/resources/` directory on the web server.

2. On the server, navigate to the `www/` directory, update the source code using `git pull`, and recompile it using `make` (or `make -B`). If all goes well, this will look (something) like:
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

Test: - ![#f03c15](test)

3. Ideally, ![#ce2029](you will have already tried recompiling the code on your own laptop and verified that you can do so without error before making any changes whatsoever to the server). If there are errors, adjust the `.md` file as necessary. Note that the paths to linked images or other resources need to be adjusted so that `resource.ext` becomes `resources/resource.ext`.

4. If the code compiles without errors, check each generated file in the `html/` directory and if there are any further problems (formatting issues, etc.), adjust the `.md` file accordingly until compilation gives the desired output.
