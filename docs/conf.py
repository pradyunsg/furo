# Configuration file for the Sphinx documentation builder.
#
# Full list of options can be found in the Sphinx documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

#
# -- Project information -----------------------------------------------------
#

project = "mawek"
copyright = "2020, Pradyun Gedam"
author = "Pradyun Gedam"

#
# -- General configuration ---------------------------------------------------
#

extensions = ["sphinx.ext.autodoc"]
templates_path = ["_templates"]

#
# -- Options for HTML output -------------------------------------------------
#

html_theme = "alabaster"

html_static_path = ["_static"]
html_title = "mawek"
