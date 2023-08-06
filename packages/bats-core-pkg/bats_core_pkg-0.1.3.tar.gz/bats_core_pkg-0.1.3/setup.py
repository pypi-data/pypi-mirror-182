# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bats_core_pkg']

package_data = \
{'': ['*'],
 'bats_core_pkg': ['dist/*',
                   'dist/bin/*',
                   'dist/lib/bats-core/*',
                   'dist/libexec/bats-core/*']}

entry_points = \
{'console_scripts': ['bats_core_pkg = bats_core_pkg:main']}

setup_kwargs = {
    'name': 'bats-core-pkg',
    'version': '0.1.3',
    'description': 'Python wrapper on tops of bats-core',
    'long_description': '# bats-core-pkg\nSimple wrapper to bats-core to be able to pull it from pypi.\n',
    'author': 'David Caro',
    'author_email': 'dcaro@wikimedia.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/david-caro/bats-core-pkg',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
