# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['test_port_gun']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['test-port-gun = test_port_gun.main:app']}

setup_kwargs = {
    'name': 'test-port-gun',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Portal Gun\nThe awesome Portal Gun',
    'author': 'danprince8984',
    'author_email': 'danprince8984@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
