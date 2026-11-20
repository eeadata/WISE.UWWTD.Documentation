"""Links from the documentation to the data explorer published next to it, under explorer/.

The explorer (explorer/ in the repository) is built separately and copied into the published site
by the documentation workflow. Its links are relative, so that they also work in the preview of a
branch, which is published under branch/<name>/.

In a page:

    {explorer}`Browse the prefilled agglomerations <spatial/agglomerations>`

The {codelist} and {fieldtable} directives add a link to their page in the explorer under each table
(explorer_link below).
"""

from docutils import nodes


def explorer_href(docname, path):
    """The address of an explorer page, relative to the HTML page of `docname`."""
    return '../' * docname.count('/') + 'explorer/' + path


def explorer_link(docname, path, text):
    """A paragraph with a link to an explorer page, to put under a table."""
    reference = nodes.reference('', text, refuri=explorer_href(docname, path), internal=False)
    return nodes.paragraph('', '', reference, classes=['explorer-link'])


def explorer_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    title, _, path = text.rpartition('<')
    if not path.endswith('>') or not title.strip():
        message = inliner.reporter.error(f'explorer role: expected "title <path>", got {text!r}', line=lineno)
        return [inliner.problematic(rawtext, rawtext, message)], [message]
    docname = inliner.document.settings.env.docname
    reference = nodes.reference(rawtext, title.strip(), refuri=explorer_href(docname, path[:-1].strip()),
                                internal=False)
    return [reference], []


def setup(app):
    app.add_role('explorer', explorer_role)
    return {'version': '1.0', 'parallel_read_safe': True, 'parallel_write_safe': True}
