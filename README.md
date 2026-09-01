# Updating web pages

## Editing content

**Either [in GitHub](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files#editing-files-in-your-repository) or offline:**

> [!NOTE]
> If using GitHub, follow the directions for editing files in [your own repository](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files#editing-files-in-your-repository). You do not need to fork the repository.

1. Edit one or more of the `.md` files in the [`markdown/`](https://github.com/lmcmicu/openquantumreality.org/tree/main/markdown) directory using [markdown syntax](https://daringfireball.net/projects/markdown/syntax).

2. **If you are editing offline**, [commit](https://git-scm.com/docs/git-commit) your changes to a new branch and then [push](https://git-scm.com/docs/git-push) your branch to GitHub. You will then need to [open a pull request](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request) to request that your branch be merged to the `main` branch. The pull request will then need to be approved by the web server administrator (see below) before it is actually merged (direct commits to `main` are not permitted).  
**If you are [using GitHub](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files#editing-files-in-your-repository)** you will be guided through all of these steps by a wizard, with links to relevant documentation.

3. If your markdown links to an image or some other web content (a PDF file, audio / video file, etc.), send these by email to the web server administrator. **Avoid adding binary files to this repository.**

> [!NOTE]
> This is a public repository. Do not upload sensitive data. Also avoid uploading binaries or large files into the repository itself (use the [releases page](https://github.com/lmcmicu/openquantumreality.org/releases) to create a release and attach the binary files to its release page instead).

## Deploying changes to the server (for the web server administrator only)

> [!CAUTION]
> Before making any changes to the server, you should dry run the changes to be merged on your own workstation to be certain that that the files in the `html/` directory are being generated correctly.
> 1. Run `make test` and then `make -B`
> 2. Open each of the `.html` files in the `html/` directory (on your laptop) in your browser, using  
> **File->Open**, to verify that the generated contents are correct. Everything should display correctly, including images, and audio files should play, etc., as expected if you were interacting with the actual site online.

**If there are problems with the output**, adjust the `.md` file accordingly (or get the author of the proposed changes to do it) until compilation gives the desired output. In particular, **inspect the beginnings and endings of each generated column** in the `.html` file to make sure that the split didn't occur at a spot that would invalidate a html tag or markdown ref, for instance. If there is a problem, then the easiest way to fix it is by adding whitespace characters, e.g., `&nbsp;`, to the end of the document, e.g.,
```
congue purus metus ultricies tellus. Proin et quam. Class aptent taciti sociosqu ad
litora torquent per conubia nostra, per inceptos hymenaeos. Praesent sapien turpis,
fermentum vel, eleifend faucibus, vehicula eu, lacus.  

&nbsp;
&nbsp;
&nbsp;
```
This will fool the script that we use to generate a `.html` file into thinking that the markdown file is longer than it actually is and thus into splitting the text into two columns at a different location.  

Note also that the **paths to linked images or other resources need to be adjusted** so that `resource.ext` becomes `resources/resource.ext` and those images need to be in the `html/resources/` directory.  

More substantial issues can be dealt with by updating the [python script](markdown2html.py) that we use to generate `.html` files from `.md` files.  

**Once you are confident that the output is correct**, you should then:

1. Merge the pull request to the main branch either by using the [command line interface](https://git-scm.com/docs/git-merge) or [online](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/merging-a-pull-request).

2. Transfer any images or other required resources (PDF files, videos, etc.) to the `/var/www/openquantumreality.org/html/resources/` directory on the web server.

3. On the web server, navigate to the `/var/www/openquantumreality.org` directory, update the source code using `git pull`, run `make test`, and finally recompile the `html/` code using `make` (or `make -B`). If all goes well, this will look like (the specific output will be different depending on the specific changes but the output should look something like) this.
<pre>
<b>(mike@sudarshan ~)$ cd /var/www/openquantumreality.org</b>
<b>(mike@sudarshan &lt;main&gt; openquantumreality.org)$ git pull</b>
remote: Enumerating objects: 16, done.
remote: Counting objects: 100% (16/16), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 12 (delta 7), reused 11 (delta 6), pack-reused 0 (from 0)
Unpacking objects: 100% (12/12), 3.92 KiB | 501.00 KiB/s, done.
From github.com:lmcmicu/openquantumreality.org
   40426ca..d5e08a8  main       -> origin/main
Updating 40426ca..d5e08a8
Fast-forward
 README.md                      |   9 ++---
 markdown/README.md             |   1 +
 templates_html/news_item1.html | 142 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 3 files changed, 148 insertions(+), 4 deletions(-)
 create mode 120000 markdown/README.md
 create mode 100644 templates_html/news_item1.html
<b>(mike@sudarshan &lt;main&gt; openquantumreality.org)$ make test</b>
Files test/html/events.html and templates_html/events.html are identical
Files test/html/index.html and templates_html/index.html are identical
Files test/html/join.html and templates_html/join.html are identical
Files test/html/news.html and templates_html/news.html are identical
Files test/html/news_item1.html and templates_html/news_item1.html are identical
Files test/html/research.html and templates_html/research.html are identical
Files test/html/team.html and templates_html/team.html are identical
Files test/html/team_member1.html and templates_html/team_member1.html are identical
<b>(mike@sudarshan &lt;main&gt; openquantumreality.org)$ make -B</b>
python3 markdown2html.py markdown/README.md src/README-from-markdown.html
python3 markdown2html.py markdown/events.md src/events-from-markdown.html
python3 markdown2html.py markdown/index.md src/index-from-markdown.html
python3 markdown2html.py markdown/join.md src/join-from-markdown.html
python3 markdown2html.py markdown/news.md src/news-from-markdown.html
python3 markdown2html.py markdown/news_item1.md src/news_item1-from-markdown.html
python3 markdown2html.py markdown/research.md src/research-from-markdown.html
python3 markdown2html.py markdown/team.md src/team-from-markdown.html
python3 markdown2html.py markdown/team_member1.md src/team_member1-from-markdown.html
python3 jinja2html.py src/events.jinja2 html/events.html
python3 jinja2html.py src/index.jinja2 html/index.html
python3 jinja2html.py src/join.jinja2 html/join.html
python3 jinja2html.py src/news.jinja2 html/news.html
python3 jinja2html.py src/news_item1.jinja2 html/news_item1.html
python3 jinja2html.py src/research.jinja2 html/research.html
python3 jinja2html.py src/team.jinja2 html/team.html
python3 jinja2html.py src/team_member1.jinja2 html/team_member1.html
<b>(mike@sudarshan &lt;main&gt; openquantumreality.org)$</b>
</pre>

4. Ideally, you will have already recompiled the code on your own laptop and **verified that you can do so without any errors before making changes to the server**, so there should be no errors. If there are errors, adjust the `.md` files as necessary (see the instructions above).
