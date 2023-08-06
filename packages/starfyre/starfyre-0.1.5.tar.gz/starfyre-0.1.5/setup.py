# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['starfyre']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'starfyre',
    'version': '0.1.5',
    'description': '',
    'long_description': '# Starfyre ⭐🔥\n\nCreate reactive frontends using only Python\n',
    'author': 'Sanskar Jethi',
    'author_email': 'sansyrox@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
