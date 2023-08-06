# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tailors_fast']

package_data = \
{'': ['*']}

install_requires = \
['OpenCC>=1.1.6,<2.0.0',
 'fasttext>=0.9.2,<0.10.0',
 'ftfy>=6.1.1,<7.0.0',
 'hao>=3.7.3,<4.0.0',
 'jieba>=0.42.1,<0.43.0']

entry_points = \
{'console_scripts': ['tailors-fast-train = tailors_fast.train:train']}

setup_kwargs = {
    'name': 'tailors-fast',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'orctom',
    'author_email': 'orctom@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
