# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiosyncapi', 'aiosyncapi.ponicode']

package_data = \
{'': ['*']}

install_requires = \
['asyncer>=0.0.2,<0.0.3', 'orjson>=3.8.3,<4.0.0', 'pydantic>=1.10.2,<2.0.0']

setup_kwargs = {
    'name': 'aiosyncapi',
    'version': '0.0.5',
    'description': 'manage asyncapi documentation',
    'long_description': '',
    'author': 'Arie',
    'author_email': 'ariesorkin3@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/nobox_/aioapi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '==3.11.1',
}


setup(**setup_kwargs)
