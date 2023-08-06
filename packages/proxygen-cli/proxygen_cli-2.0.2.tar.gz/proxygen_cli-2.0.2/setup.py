# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['proxygen_cli', 'proxygen_cli.cli', 'proxygen_cli.lib']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'cryptography>=38.0.3,<39.0.0',
 'jinja2>=3.1.2,<4.0.0',
 'lxml>=4.9.1,<5.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'pyjwt>=2.6.0,<3.0.0',
 'pyyaml>=6.0,<7.0',
 'requests>=2.28.1,<3.0.0',
 'tabulate>=0.9.0,<0.10.0',
 'yaspin>=2.2.0,<3.0.0']

entry_points = \
{'console_scripts': ['proxygen = proxygen_cli.cli.command_main:main']}

setup_kwargs = {
    'name': 'proxygen-cli',
    'version': '2.0.2',
    'description': "CLI for interacting with NHSD APIM's proxygen service",
    'long_description': '# proxygen-cli\n\n## Getting started\n\n    1. Get some credentials from API Management\n    # TODO make these steps work, for now one has to manually create these files\n    2. Add those credentials to your machine, see the `proxygen credentials` command.\n    3. Set the API you wish to work on, see the `proxygen settings` command.\n',
    'author': 'Ben Strutt',
    'author_email': 'ben.strutt1@nhs.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/NHSDigital/proxygen-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
