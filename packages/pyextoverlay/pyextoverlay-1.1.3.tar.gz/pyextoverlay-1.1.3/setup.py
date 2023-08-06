# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['pyextoverlay']
setup_kwargs = {
    'name': 'pyextoverlay',
    'version': '1.1.3',
    'description': 'simple overlay library',
    'long_description': '',
    'author': 'Xenely',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
