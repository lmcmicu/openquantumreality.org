# Updating a web page

1. Navigate to the `src/` directory

        $ cd src/

2. Edit the desired `.jinja2` source file as needed using your favourite editor. E.g.,

        $ vi index.jinja2

3. If necessary, add any linked-to binary files or other resources to the `html/resources/` directory.

4. Compile the source code:

        $ make
        python3 generate_html_from_template.py index.jinja2 ../html/index.html
