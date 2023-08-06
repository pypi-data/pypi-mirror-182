# -*- coding: utf-8 -*-

extensions = [
    'jupyterlite_sphinx'
]

master_doc = 'index'
source_suffix = '.rst'

project = 'jupyterlite-xeus-python'
copyright = 'JupyterLite Team'
author = 'JupyterLite Team'

exclude_patterns = []

html_theme = "pydata_sphinx_theme"

jupyterlite_config = "jupyterlite_config.json"
jupyterlite_dir = "."
