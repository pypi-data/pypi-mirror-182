# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['GDrivePlayer']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'gdriveplayer',
    'version': '0.1.0',
    'description': 'A python wrapper for gdriveplayer.co API',
    'long_description': '# GDrivePlayerAPI\nA python wrapper for gdriveplayer.co API\n',
    'author': 'adenosinetp10',
    'author_email': 'adenosinetp10@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
