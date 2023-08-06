# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['evergate', 'evergate._internal', 'evergate.datamodel', 'evergate.procedure']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.2,<2.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'evergate',
    'version': '0.1.0',
    'description': 'An API wrapper for Eve Online Swagger Interface',
    'long_description': '# Evergate - wrapper library for Eve Swagger Interface\n\nA fully typed Python wrapper library for [Eve Swagger Interface](https://esi.evetech.net).\n',
    'author': 'frodo821',
    'author_email': 'sakaic2003@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<3.12',
}


setup(**setup_kwargs)
