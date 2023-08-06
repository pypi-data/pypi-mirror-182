# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tempcord']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'tempcord',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'arkhon7',
    'author_email': 'reviuy9@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
