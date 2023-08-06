# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cricguru', 'cricguru.helpers']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'cricguru',
    'version': '0.1.0',
    'description': '',
    'long_description': '# cricguru\n\nA work in progress module for the CricInfo StatsGuru data.\n',
    'author': 'Pavithran',
    'author_email': 'pavithranthilakanathan@gmai.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
