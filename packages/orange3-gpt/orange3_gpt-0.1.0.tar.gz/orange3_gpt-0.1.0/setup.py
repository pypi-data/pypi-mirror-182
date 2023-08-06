# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['orangecontrib', 'orangecontrib.gpt', 'orangecontrib.gpt.widgets']

package_data = \
{'': ['*']}

install_requires = \
['openai>=0.25.0,<0.26.0']

setup_kwargs = {
    'name': 'orange3-gpt',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Orange3 GPT Addon\n',
    'author': 'Rafael Irgolic',
    'author_email': 'hello@irgolic.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
