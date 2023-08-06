# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eagerx_utility',
 'eagerx_utility.camera',
 'eagerx_utility.camera.pybullet',
 'eagerx_utility.ik',
 'eagerx_utility.overlay',
 'eagerx_utility.reset',
 'eagerx_utility.safety',
 'eagerx_utility.solid',
 'eagerx_utility.solid.real']

package_data = \
{'': ['*'],
 'eagerx_utility.camera': ['assets/*'],
 'eagerx_utility.solid': ['assets/*']}

install_requires = \
['eagerx>=0.1.13,<0.2.0']

setup_kwargs = {
    'name': 'eagerx-utility',
    'version': '0.0.1',
    'description': 'Template for creating EAGERx packages.',
    'long_description': 'None',
    'author': 'Jelle Luijkx',
    'author_email': 'j.d.luijkx@tudelft.nl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/eager-dev/eagerx_utility',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
