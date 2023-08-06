# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['assistance']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.88.0,<0.89.0',
 'keyring>=23.13.1,<24.0.0',
 'openai>=0.25.0,<0.26.0',
 'uvicorn[standard]>=0.20.0,<0.21.0']

setup_kwargs = {
    'name': 'assistance',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Assistance\n',
    'author': 'Simon Biggs',
    'author_email': 'simon.biggs@radiotherapy.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
