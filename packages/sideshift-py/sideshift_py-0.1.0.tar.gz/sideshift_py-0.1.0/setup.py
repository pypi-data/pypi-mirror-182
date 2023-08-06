# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sideshift_py']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'sideshift-py',
    'version': '0.1.0',
    'description': '',
    'long_description': '# SideShift-py\ntodo',
    'author': 'bart',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
