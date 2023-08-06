# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['movee']

package_data = \
{'': ['*']}

install_requires = \
['impall>=1.1.1,<2.0.0',
 'pyyaml>=6.0,<7.0',
 'safer>=4.4.1,<5.0.0',
 'tdir>=1.4.1,<2.0.0',
 'termtosvg>=1.1.0,<2.0.0']

setup_kwargs = {
    'name': 'movee',
    'version': '0.10.0',
    'description': '🎦 movee: Script asciinema movies 🎦',
    'long_description': '🎦 movee: Script asciinema movies 🎦\n--------------------------------------------\n\nLove asciinema movies? Have performance anxiety?\n\nmovee lets you script your asciinema movies, for Python, bash\nor any other command interpreter.\n',
    'author': 'Tom Ritchford',
    'author_email': 'tom@swirly.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
