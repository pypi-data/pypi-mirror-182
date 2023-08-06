# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['firecore']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.6.0,<0.7.0', 'numpy>=1.24.0,<2.0.0', 'rjsonnet>=0.4.5,<0.5.0']

setup_kwargs = {
    'name': 'firecore',
    'version': '0.1.0',
    'description': '',
    'long_description': '# firecore',
    'author': 'SunDoge',
    'author_email': '384813529@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
