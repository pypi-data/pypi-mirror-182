# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gr_tk']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0']

entry_points = \
{'console_scripts': ['gr = gr_tk.gr:cli']}

setup_kwargs = {
    'name': 'gr-tk',
    'version': '0.1.0',
    'description': 'Gerenciamento de risco - tool kit para CLI',
    'long_description': '# gr\nCálculos de gerenciamento de risco para trading\n',
    'author': 'Valmir Franca',
    'author_email': 'vfranca3@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
