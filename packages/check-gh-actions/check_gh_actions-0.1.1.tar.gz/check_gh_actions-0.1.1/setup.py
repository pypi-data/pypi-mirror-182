# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['check_gh_actions']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'check-gh-actions',
    'version': '0.1.1',
    'description': '',
    'long_description': '# Check gh actions',
    'author': 'Maxim V4S',
    'author_email': 'maxim.d@v4scale.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
