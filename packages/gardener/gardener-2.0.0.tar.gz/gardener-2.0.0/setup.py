# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gardener']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'gardener',
    'version': '2.0.0',
    'description': 'Hook-based tree manipulation library',
    'long_description': 'None',
    'author': 'Dmitry Gritsenko',
    'author_email': 'k01419q45@ya.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
