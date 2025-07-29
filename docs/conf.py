# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import django

# -- Path setup --------------------------------------------------------------
# Add project root (where manage.py is) to sys.path
sys.path.insert(0, os.path.abspath('..'))
# Set the Django settings module and setup Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "newsportal.settings")
django.setup()

# -- Project information -----------------------------------------------------
project = 'newsportal'
copyright = '2025, D. Botha'
author = 'D. Botha'
release = 'v1.0.2'

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

language = 'en'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']
