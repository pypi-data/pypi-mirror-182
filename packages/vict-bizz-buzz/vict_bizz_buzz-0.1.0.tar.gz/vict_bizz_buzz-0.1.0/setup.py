# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vict_bizz_buzz']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'vict-bizz-buzz',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Victor Tsetsulin',
    'author_email': 'victor.tsetsulin@nexttrucking.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
