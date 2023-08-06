# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dbtest']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dbtest',
    'version': '0.1.0',
    'description': 'Testing for dbt.',
    'long_description': 'None',
    'author': 'Indi Harrington',
    'author_email': 'hi@indigo.rocks',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
