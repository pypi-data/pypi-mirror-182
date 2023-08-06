# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['minuteinbox']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'minuteinbox',
    'version': '0.1.2',
    'description': 'Unofficial python wrapper for minuteinbox.com',
    'long_description': ' # minuteinbox\n\n[![Version](https://img.shields.io/pypi/v/minuteinbox?logo=pypi)](https://pypi.org/project/minuteinbox)\n[![Quality Gate Status](https://img.shields.io/sonar/alert_status/fedecalendino_minuteinbox?logo=sonarcloud&server=https://sonarcloud.io)](https://sonarcloud.io/dashboard?id=fedecalendino_minuteinbox)\n[![CodeCoverage](https://img.shields.io/sonar/coverage/fedecalendino_minuteinbox?logo=sonarcloud&server=https://sonarcloud.io)](https://sonarcloud.io/dashboard?id=fedecalendino_minuteinbox)\n\nUnofficial python wrapper for minuteinbox.com\n',
    'author': 'Fede Calendino',
    'author_email': 'fede@calendino.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fedecalendino/minuteinbox',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
