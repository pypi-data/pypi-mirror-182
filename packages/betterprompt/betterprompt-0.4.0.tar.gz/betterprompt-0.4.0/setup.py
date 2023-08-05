# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['betterprompt']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'betterprompt',
    'version': '0.4.0',
    'description': '',
    'long_description': None,
    'author': 'Krrish Dholakia',
    'author_email': 'krrishdholakia@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
