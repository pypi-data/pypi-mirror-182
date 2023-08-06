# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyfluids',
 'pyfluids.enums',
 'pyfluids.fluids',
 'pyfluids.humid_air',
 'pyfluids.io']

package_data = \
{'': ['*']}

install_requires = \
['CoolProp==6.4.3.post1']

setup_kwargs = {
    'name': 'pyfluids',
    'version': '2.3.1',
    'description': 'A simple, full-featured, lightweight CoolProp wrapper for Python',
    'long_description': '# ![PyFluids](https://raw.githubusercontent.com/portyanikhin/PyFluids/main/pictures/header.png)\n\n[![Build & Tests](https://github.com/portyanikhin/PyFluids/actions/workflows/build-tests.yml/badge.svg)](https://github.com/portyanikhin/PyFluids/actions/workflows/build-tests.yml)\n[![CodeQL](https://github.com/portyanikhin/PyFluids/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/portyanikhin/PyFluids/actions/workflows/codeql-analysis.yml)\n[![PyPI](https://img.shields.io/pypi/v/pyfluids)](https://pypi.org/project/pyfluids/)\n[![Python](https://img.shields.io/pypi/pyversions/pyfluids)](https://pypi.org/project/pyfluids/)\n[![License](https://img.shields.io/github/license/portyanikhin/PyFluids)](https://github.com/portyanikhin/PyFluids/blob/master/LICENSE)\n[![codecov](https://codecov.io/gh/portyanikhin/PyFluids/branch/main/graph/badge.svg?token=I1LL66AOJW)](https://codecov.io/gh/portyanikhin/PyFluids)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)\n\nA simple, full-featured, lightweight [CoolProp](http://www.coolprop.org) wrapper for Python.\n\n_**See [full documentation](https://github.com/portyanikhin/PyFluids).**_',
    'author': 'Vladimir Portyanikhin',
    'author_email': 'v.portyanikhin@ya.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/portyanikhin/PyFluids',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.12',
}


setup(**setup_kwargs)
