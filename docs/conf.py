# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'WISE.UWWTD.Documentation'
copyright = '2026, WISE.UWWTD.Documentation'
# author = 'Tracasa Global'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Local extensions: _ext/codelist.py renders the code lists from reference/codelist/*.csv,
# _ext/fieldtable.py the field tables from reference/schema/*/*.csv,
# _ext/internal.py keeps the open issues pages out of the published build (-t internal to include them)
# _ext/explorer.py links to the data explorer published under explorer/,
# _ext/versions.py shows the version of a dataflow specification from reference/versions.csv
import os
import sys
sys.path.insert(0, os.path.abspath('_ext'))

extensions = ['codelist',
              'fieldtable',
              'internal',
              'explorer',
              'versions',
              'sphinx.ext.autodoc',
              'myst_parser',
              'sphinx_design',
              'sphinx_copybutton',
              'sphinx_togglebutton',
              'sphinxcontrib.bibtex',
              'sphinxcontrib.mermaid'
              ]

# BIBTEX
bibtex_bibfiles = ['./_sharedFiles/eu_legislation.bib',
                   './_sharedFiles/bibliography.bib',]
bibtex_reference_style = 'author_year'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '*.txt']

# NUMBERING
# The separator must defined in a custom.css :-(
numfig = True
numfig_format = {
    'figure': 'Figure %s',       # Changes "Fig. 1" to "Figure 1"
    'table': 'Table %s',
    'code-block': 'Example %s',  # Changes "Listing 1" to "Example 1"
    'section': 'Section %s',
}

# MATH - Tell MyST to allow dollar signs and advanced math blocks
myst_enable_extensions = [
    "amsmath",
    "dollarmath",
    "colon_fence",
    "linkify",
    "attrs_inline"
]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_theme_options = {
    "logo": {
        "alt_text": "WISE UWWTD Documentation",
        "text": "Urban Waste Water Treatment Directive",
    },
    "secondary_sidebar_items": ["page-toc", "edit-this-page", "sourcelink"],
    "show_toc_level": 4,
    "use_edit_page_button": True,
    "navbar_align": "right",
    # A button to the data explorer (_templates/explorer-navbar.html), before the default items
    "navbar_end": ["explorer-navbar", "theme-switcher", "navbar-icon-links"],
}

html_context = {
    "github_user": "eeadata",
    "github_repo": "WISE.UWWTD.Documentation",
    "github_version": "main",
    "doc_path": "docs",
}

# A snapshot of the documentation for a version of a specification, published under
# versions/<tag>/ when the version is tagged (DOCS_SNAPSHOT=<tag>, set by the workflow). It shows a
# banner, and its links to the data explorer go to the current one, two folders up.
SNAPSHOT = os.environ.get('DOCS_SNAPSHOT', '')
explorer_up = 2 if SNAPSHOT else 0
html_context["explorer_up"] = explorer_up
if SNAPSHOT:
    html_theme_options["announcement"] = (
        f"You are reading the documentation as published with <strong>{SNAPSHOT}</strong>. "
        '<a href="https://eeadata.github.io/WISE.UWWTD.Documentation/">Read the latest version</a>.')
html_logo = "_static/wise.svg"

html_sidebars = {
    "**": ["sidebar-collapse", "sidebar-nav-bs"],
}


html_static_path = ['_static']
html_css_files = [
    'customTable.css',
    'customTheme.css'
    ]

html_show_copyright = False

html_js_files = [
    "js/mermaid-zoom.js",
]

# MERMAID DIAGRAMS 
mermaid_init_js = """
mermaid.initialize({theme:"neutral"});
"""

# -- Draft marker ------------------------------------------------------------
# Every page of the revised Directive section is marked as a draft.

DRAFT_SECTION = "rUWWTD2024"
DRAFT_BANNER = (
    '<aside class="draft-banner" role="note">'
    'Draft \u2013 under review &amp; revision</aside>'
)


def add_draft_banner(app, pagename, templatename, context, doctree):
    if pagename == DRAFT_SECTION or pagename.startswith(DRAFT_SECTION + "/"):
        context["body"] = DRAFT_BANNER + context.get("body", "")


def setup(app):
    app.connect("html-page-context", add_draft_banner)
