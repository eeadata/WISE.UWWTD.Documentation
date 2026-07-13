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

extensions = ['sphinx.ext.autodoc',
              'myst_parser',
              'sphinx_design',
              'sphinx_copybutton',
              'sphinx_togglebutton'
              ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_theme_options = {   
    "secondary_sidebar_items": ["page-toc", "edit-this-page", "sourcelink"],
    "show_toc_level": 3, 
    "use_edit_page_button": False,
    "navbar_align": "right",
}





html_static_path = ['_static']
html_css_files = ['custom.css']

html_show_copyright = False

html_js_files = [
    "js/mermaid-zoom.js",
]



# MERMAID DIAGRAMS 
mermaid_init_js = """
mermaid.initialize({theme:"neutral"});
"""