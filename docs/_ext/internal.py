"""Keep the internal pages (open issues and decisions) out of the published documentation.

The pages stay in the repository and are built only with the `internal` tag:

    sphinx-build -t internal -b html docs _build/internal

In the default build, which is the one published, the pages are excluded and every reference to
them is removed together with what only made sense around it:

* a reference alone in brackets, "is not final ({ref}`art23-oi-naming`)", loses the brackets;
* a sentence "See {ref}`art23-oi-status`." is removed, and "... and {ref}`art23-oi-x`" loses the
  "and";
* a section titled "Related open issues" is removed, and so is a grid card whose title is one.

A reference that none of these rules can remove is reported as a warning, so that the published
pages never show a broken link to an internal page.
"""

import re
from pathlib import Path

from docutils import nodes
from sphinx.addnodes import pending_xref
from sphinx.transforms import SphinxTransform
from sphinx.util import logging

logger = logging.getLogger(__name__)

INTERNAL_PAGES = ['rUWWTD2024/SpatialPoints/OpenIssues.md', 'rUWWTD2024/Article23/OpenIssues.md']
RELATED_SECTION = 'related open issues'
SEPARATOR = re.compile(r'\s*(,|;|, and|and)\s+')


def is_separator(node):
    return isinstance(node, nodes.Text) and SEPARATOR.fullmatch(str(node)) is not None


def is_internal_build(app):
    return app.tags.has('internal')


def config_inited(app, config):
    labels = set()
    for page in INTERNAL_PAGES:
        text = (Path(app.srcdir) / page).read_text(encoding='utf-8')
        labels |= {label.lower() for label in re.findall(r'^\((.+)\)=$', text, re.M)}
    config.internal_labels = sorted(labels)
    if not is_internal_build(app):
        config.exclude_patterns = list(config.exclude_patterns) + INTERNAL_PAGES


def source_read(app, docname, source):
    """In the published build, drop the internal pages from the toctrees of their dataflow."""
    if is_internal_build(app):
        return
    for page in INTERNAL_PAGES:
        folder, name = page.rsplit('/', 1)
        if docname == f'{folder}/index':
            source[0] = re.sub(rf'^{re.escape(name[:-3])}[ \t]*\n', '', source[0], flags=re.M)


def attached(node, document):
    while node is not None:
        if node is document:
            return True
        node = node.parent
    return False


class RemoveInternalReferences(SphinxTransform):
    default_priority = 900

    def apply(self):
        if is_internal_build(self.app):
            return
        labels = set(self.config.internal_labels)

        def internal(node):
            return (isinstance(node, pending_xref) and node.get('reftype') in ('ref', 'numref')
                    and node.get('reftarget', '').lower() in labels)

        for section in list(self.document.findall(nodes.section)):
            title = section.next_node(nodes.title)
            if title is not None and title.astext().strip().lower() == RELATED_SECTION:
                section.parent.remove(section)

        for ref in list(self.document.findall(pending_xref)):
            if not internal(ref) or not attached(ref, self.document):
                continue
            if not (self.remove_card(ref) or self.remove_in_brackets(ref, internal)
                    or self.remove_see(ref) or self.remove_and(ref)):
                logger.warning(f"reference to the internal label {ref['reftarget']!r} is not removed "
                               'from the published page; rewrite the sentence', location=ref)

    @staticmethod
    def replace_text(text_node, value):
        if value:
            text_node.parent.replace(text_node, nodes.Text(value))
        else:
            text_node.parent.remove(text_node)

    def remove_card(self, ref):
        """A grid card (sphinx-design) that links to an internal page is removed whole."""
        node = ref.parent
        while isinstance(node, nodes.Element) and not isinstance(node, nodes.document):
            if 'sd-col' in node.get('classes', []):
                node.parent.remove(node)
                return True
            node = node.parent
        return False

    def remove_in_brackets(self, ref, internal):
        """Remove the internal references, and the brackets if nothing else is left in them."""
        siblings = ref.parent.children
        i = siblings.index(ref)
        j = i - 1
        while j >= 0 and (internal(siblings[j]) or is_separator(siblings[j])):
            j -= 1
        k = i + 1
        while k < len(siblings) and (internal(siblings[k]) or is_separator(siblings[k])):
            k += 1
        left = siblings[j] if j >= 0 else None
        right = siblings[k] if k < len(siblings) else None
        if isinstance(left, nodes.Text) and str(left).endswith('(') and \
                isinstance(right, nodes.Text) and str(right).startswith(')'):
            for node in siblings[j + 1:k]:
                ref.parent.remove(node)
            parent = left.parent
            self.replace_text(left, str(left)[:-1].rstrip(' '))
            self.replace_text(right, str(right)[1:])
            return parent is not None
        # mixed with other references: drop this one and one separator next to it
        before = siblings[i - 1] if i > 0 else None
        after = siblings[i + 1] if i + 1 < len(siblings) else None
        for sep in (before, after):
            if is_separator(sep) and \
                    any(isinstance(s, pending_xref) and not internal(s) for s in siblings):
                ref.parent.remove(sep)
                ref.parent.remove(ref)
                return True
        return False

    def remove_see(self, ref):
        """'... reported. See {ref}`x`.' and '... a source; see {ref}`x`.' lose the 'See'."""
        siblings = ref.parent.children
        i = siblings.index(ref)
        before = siblings[i - 1] if i > 0 else None
        after = siblings[i + 1] if i + 1 < len(siblings) else None
        if not (isinstance(before, nodes.Text) and re.search(r'(^|\s)[Ss]ee $', str(before))
                and isinstance(after, nodes.Text) and str(after).startswith('.')):
            return False
        head = re.sub(r'[Ss]ee $', '', str(before)).rstrip()
        tail = str(after)
        if head.endswith(';'):
            head = head[:-1]
        elif head.endswith('.') or head == '':
            tail = tail[1:]  # the sentence before already ends with its full stop
        ref.parent.remove(ref)
        self.replace_text(before, head)
        self.replace_text(after, tail)
        return True

    def remove_and(self, ref):
        """'See {ref}`a` and {ref}`x`.' loses ' and {ref}`x`'."""
        siblings = ref.parent.children
        i = siblings.index(ref)
        before = siblings[i - 1] if i > 0 else None
        match = re.search(r'\s+and\s+$', str(before)) if isinstance(before, nodes.Text) else None
        if match and i >= 2 and isinstance(siblings[i - 2], pending_xref):
            ref.parent.remove(ref)
            self.replace_text(before, str(before)[:match.start()])
            return True
        return False


def remove_internal_references(app, doctree):
    RemoveInternalReferences(doctree).apply()


def setup(app):
    app.add_config_value('internal_labels', [], 'env')
    app.connect('config-inited', config_inited)
    app.connect('source-read', source_read)
    # before the collectors (priority 500), so that the table of contents of the page and the
    # search index no longer list what is removed
    app.connect('doctree-read', remove_internal_references, priority=100)
    return {'version': '1.0', 'parallel_read_safe': True, 'parallel_write_safe': True}
