# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['mongo_unit_of_work']

package_data = \
{'': ['*']}

install_requires = \
['ddd-misc>=0.8.1,<0.9.0', 'motor>=3.1.1,<4.0.0']

setup_kwargs = {
    'name': 'mongo-unit-of-work',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Aziz',
    'author_email': 'walkingonadream2012@mail.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
