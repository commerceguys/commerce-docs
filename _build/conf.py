# -*- coding: utf-8 -*-
#
# Drupal Commerce documentation build configuration file, created by
# sphinx-quickstart on Wed Jan 18 19:26:21 2017.
#
import sys, os

sys.path.append(os.path.abspath('exts'))

from sphinx.highlighting import lexers
from pygments.lexers.compiled import CLexer
from pygments.lexers.special import TextLexer
from pygments.lexers.text import RstLexer
from pygments.lexers.web import PhpLexer
from drupalcommerce.sphinx.lexer import TerminalLexer

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.todo',
    'sensio.sphinx.refinclude', 'sensio.sphinx.configurationblock', 'sensio.sphinx.phpcode', 'sensio.sphinx.bestpractice', 'sensio.sphinx.codeblock',
    'drupalcommerce.sphinx', 'sphinxcontrib.phpdomain',
]

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.rst']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

project = u'Drupal Commerce'
copyright = u'2017, Commerce Guys'
author = 'Drupal Commerce Documentation Team'
github_doc_root = 'https://github.com/drupalcommerce/commerce-docs/tree/master/'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
#version = u'0.0.1'
# The full version, including alpha/beta/rc tags.
#release = u'0.0.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
import sphinx_rtd_theme

html_theme = "commerce_theme"

html_theme_path = [sphinx_rtd_theme.get_html_theme_path(), "themes"]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'collapse_navigation': False,
    'display_version': False,
    'analytics_id': 'UA-12478122-2'
}
html_context = {
    # Enable the "Edit in GitHub link within the header of each page.
    'display_github': True,
    'github_user': 'drupalcommerce',
    'github_repo': 'commerce-docs',
    'github_version': 'master/source/',
    'logo': 'logo.png',
    'theme_logo_only': True
}
html_static_path = ['../images']
html_favicon = "../images/favicon.ico"

# enable highlighting for PHP code not between ``<?php ... ?>`` by default
lexers['markdown'] = TextLexer()
lexers['php'] = PhpLexer(startinline=True)
lexers['php-annotations'] = PhpLexer(startinline=True)
lexers['php-standalone'] = PhpLexer(startinline=True)
lexers['rst'] = RstLexer()
lexers['terminal'] = TerminalLexer()

config_block = {
    'apache': 'Apache',
    'markdown': 'Markdown',
    'nginx': 'Nginx',
    'rst': 'reStructuredText',
    'terminal': 'Terminal',
}

# use PHP as the primary domain
primary_domain = 'php'
highlight_language='php'

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'DrupalCommercedoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'DrupalCommerce.tex', u'Drupal Commerce Documentation',
     u'Isaac Horton', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'drupalcommerce', u'Drupal Commerce Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'DrupalCommerce', u'Drupal Commerce Documentation',
     author, 'DrupalCommerce', 'One line description of project.',
     'Miscellaneous'),
]
