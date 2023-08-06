# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tortoiseschema']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'tortoiseschema',
    'version': '0.1.0',
    'description': 'Tortoise ORM combined with pydantic',
    'long_description': '',
    'author': 'Stanislav Zmiev',
    'author_email': 'szmiev2000@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
