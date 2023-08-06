# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cmem',
 'cmem.cmemc',
 'cmem.cmemc.cli',
 'cmem.cmemc.cli.commands',
 'cmem.cmemc.cli.manual_helper']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4',
 'certifi',
 'click-didyoumean',
 'click-help-colors',
 'click==7.1.2',
 'cmem-cmempy==22.3rc3',
 'configparser',
 'jinja2',
 'natsort',
 'prometheus-client',
 'pygments',
 'pyjwt',
 'requests',
 'six',
 'tabulate',
 'timeago',
 'treelib',
 'types-six',
 'types-tabulate',
 'urllib3']

entry_points = \
{'console_scripts': ['cmemc = cmem.cmemc.cli:main']}

setup_kwargs = {
    'name': 'cmem-cmemc',
    'version': '22.3rc1',
    'description': 'Command line client for eccenca Corporate Memory',
    'long_description': '# cmemc\n\ncmemc is the official command line client for [eccenca Corporate Memory](https://documentation.eccenca.com/).\n\n## Installation\n\nIn order to install the cmemc, run:\n\n    pip install cmem-cmemc\n\nYou may consider installing cmemc only for the current user:\n\n    pip install cmem-cmemc --user\n\n## Configuration and Usage\n\ncmemc is intended for System Administrators and Linked Data Expert, who wants to automate and remote control activities on eccenca Corporate Memory.\n\nThe cmemc manual including basic usage pattern, configuration as well as a command reference is available at:\n\n[https://eccenca.com/go/cmemc](https://eccenca.com/go/cmemc)\n\ncmemc only works with Python 3 and refuses to work with Python 2.x.\nIn addition to that, cmemc will warn you in case an untested Python environment is used.\n\n',
    'author': 'eccenca',
    'author_email': 'cmempy-developer@eccenca.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://eccenca.com/go/cmemc',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
