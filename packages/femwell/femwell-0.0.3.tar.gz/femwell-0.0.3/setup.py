# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['femwell', 'femwell.examples', 'femwell.mesh', 'femwell.tests']

package_data = \
{'': ['*']}

install_requires = \
['gmsh', 'matplotlib', 'pygmsh', 'scikit-fem>=8.0.0', 'shapely']

setup_kwargs = {
    'name': 'femwell',
    'version': '0.0.3',
    'description': 'Mode solver for photonic and electric waveguides based on FEM',
    'long_description': '#######\nFemwell\n#######\n\n.. image:: https://github.com/helgegehring/femwell/actions/workflows/docs.yml/badge.svg\n    :target: https://HelgeGehring.github.io/femwell/\n.. image:: https://github.com/helgegehring/femwell/actions/workflows/build.yml/badge.svg\n    :target: https://github.com/HelgeGehring/femwell/actions/workflows/build.yml\n\nWorking on a mode solver for photonic/electric waveguides based on scikit-fem\n\n************\nContributors\n************\n- Helge Gehring (Google): Maintainer\n- Simon Bilodeau (Google): Meshes everything',
    'author': 'Helge Gehring',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/HelgeGehring/femwell',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
