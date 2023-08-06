# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['inspyre_toolbox',
 'inspyre_toolbox.console_kit',
 'inspyre_toolbox.conversions',
 'inspyre_toolbox.conversions.roman_numerals',
 'inspyre_toolbox.core.errors',
 'inspyre_toolbox.core_helpers',
 'inspyre_toolbox.humanize',
 'inspyre_toolbox.humanize.errors',
 'inspyre_toolbox.live_timer',
 'inspyre_toolbox.proc_man',
 'inspyre_toolbox.pypi',
 'inspyre_toolbox.spanners',
 'inspyre_toolbox.syntactic_sweets',
 'inspyre_toolbox.sys_man']

package_data = \
{'': ['*']}

install_requires = \
['DateTime>=4.3,<5.0',
 'inflect>=5.3.0,<6.0.0',
 'inspy-logger>=2.1a14,<3.0',
 'inspyred-print>=1.2.1,<2.0.0',
 'psutil>=5.8.0,<6.0.0',
 'pypattyrn>=1.2,<2.0',
 'tqdm>=4.64.0,<5.0.0']

setup_kwargs = {
    'name': 'inspyre-toolbox',
    'version': '1.3.1.dev3',
    'description': 'A toolbox containing some useful tools for Inspyre Softworks packages. Generally useful to some programmers too.',
    'long_description': None,
    'author': 'T Blackstone',
    'author_email': 't.blackstone@inspyre.tech',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
