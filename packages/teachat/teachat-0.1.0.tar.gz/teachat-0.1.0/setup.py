# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['teachat']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'teachat',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'RA',
    'author_email': 'numpde@null.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
