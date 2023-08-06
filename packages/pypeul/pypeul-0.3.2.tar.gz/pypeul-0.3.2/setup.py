# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['pypeul']
setup_kwargs = {
    'name': 'pypeul',
    'version': '0.3.2',
    'description': 'A Python 3 IRC library thought for the programmer.',
    'long_description': '# Pypeul\n\nPypeul is an IRC client library written in Python.\n\nIt mainly aims at creating IRC bots and provides an easy to use API\nbased on callbacks. It also features a nice way to parse and write\nformatted text.\n\n**Copyright**: Copyright 2010-2012- by the Pypeul team, see AUTHORS.\n\n**License**: LGPL, see COPYING for details.\n',
    'author': 'mickael9',
    'author_email': 'mickael9@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/zopieux/pypeul',
    'py_modules': modules,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
