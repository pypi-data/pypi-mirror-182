# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cricguru', 'cricguru.helpers']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2', 'pandas>=1.5.2,<2.0.0']

setup_kwargs = {
    'name': 'cricguru',
    'version': '0.4.0',
    'description': '',
    'long_description': '# cricguru\n\nA work in progress module for the CricInfo StatsGuru data.\n',
    'author': 'Pavithran',
    'author_email': 'pavithranthilakanathan@gmai.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/puppetmaster12/cricguru',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
