# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ffpack', 'ffpack.fdr', 'ffpack.lcc', 'ffpack.lsg', 'ffpack.utils']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.21,<2.0']

setup_kwargs = {
    'name': 'ffpack',
    'version': '0.2.0',
    'description': 'Fatigue and fracture package',
    'long_description': '# FFPACK - Fatigue and Fracture PACKage\n\n![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/dpzhuX/ffpack/python-package.yml?branch=main)\n![GitHub](https://img.shields.io/github/license/dpzhuX/ffpack)\n[![DOI](https://zenodo.org/badge/575208693.svg)](https://zenodo.org/badge/latestdoi/575208693)\n\n## Purpose\n`FFPACK` ( Fatigue and Fracture PACKage ) is an open-source Python library for fatigue and fracture analysis. It supports load cycle counting with ASTM methods, load sequence generators, fatigue damage evaluations, etc. A lot of features are under active development. `FFPACK` is designed to help engineers analyze fatigue and fracture behavior in engineering practice.\n\n## Installation\n\n`FFPACK` can be installed via [PyPI](https://pypi.org/project/ffpack/):\n\n```\npip install ffpack\n```\n\n## Status\n\n`FFPACK` is currently under active development. \n\n## Contents\n\n* Fatigue damage rule\n    * Palmgren-miner damage rule\n        * Naive Palmgren-miner damage rule\n        * Classic Palmgren-miner damage rule\n\n* Load cycle counting\n    * ASTM\n        * ASTM level crossing counting\n        * ASTM peak counting\n        * ASTM simple range counting\n        * ASTM rainflow counting\n    * Rychlik\n        * Rychlik rainflow Counting\n\n* Load sequence generator\n    * Random walk\n        * Uniform random walk\n    * Autoregressive model\n        * Normal autoregressive model\n\n* Utility methods\n    * Cycle counting aggregation\n    * Fitter for SN curve\n    * Sequence peak and valleys\n    * Sequence degitization\n\n## Document\n\nYou can find a complete documentation for setting up `FFPACK` at the [Read the Docs site](https://ffpack.readthedocs.io/en/latest/).\n',
    'author': 'Dongping Zhu',
    'author_email': 'None',
    'maintainer': 'Dongping Zhu',
    'maintainer_email': 'None',
    'url': 'https://pypi.org/project/ffpack',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
