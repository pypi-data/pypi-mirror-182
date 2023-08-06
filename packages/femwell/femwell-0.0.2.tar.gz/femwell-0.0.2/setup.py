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
    'version': '0.0.2',
    'description': 'Mode solver for photonic and electric waveguides based on FEM',
    'long_description': 'None',
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
