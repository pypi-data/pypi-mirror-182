# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['identity_sdk']

package_data = \
{'': ['*']}

install_requires = \
['starlite>=1.45.1,<2.0.0']

setup_kwargs = {
    'name': 'identity-sdk',
    'version': '0.1.0',
    'description': "The Python SDK for The Hacker App's identity platform",
    'long_description': "# Identity SDK\n\nThe Python SDK for The Hacker App's identity platform.\n",
    'author': 'Alex Krantz',
    'author_email': 'alex@krantz.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
