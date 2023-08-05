# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['temper_std']

package_data = \
{'': ['*']}

install_requires = \
['temper-core==0.0.3']

setup_kwargs = {
    'name': 'temper-std',
    'version': '0.0.3',
    'description': '',
    'long_description': 'None',
    'author': 'None',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
