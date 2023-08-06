# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['grand_challenge']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'grand-challenge',
    'version': '0.1.0',
    'description': 'Next Generation Grand Challenge Python Client',
    'long_description': '# Grand Challenge\nNext Generation Grand Challenge Python Client\n',
    'author': 'James Meakin',
    'author_email': '12661555+jmsmkn@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
