# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mkdocs_siemens']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'mkdocs-siemens',
    'version': '0.0.1',
    'description': 'A placeholder package for the Siemens MkDocs theme',
    'long_description': '# Siemens\n\nThis is a placeholder package reserved for open-sourcing the Siemens MkDocs theme.\n\nFor other Siemens Open Source projects, see [opensource.siemens.com](https://opensource.siemens.com)\nand [github.com/siemens](https://github.com/siemens).\n',
    'author': 'Siemens Open Source',
    'author_email': 'opensource@siemens.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://opensource.siemens.com',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
