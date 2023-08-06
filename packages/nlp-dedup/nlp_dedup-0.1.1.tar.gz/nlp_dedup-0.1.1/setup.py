# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['nlp_dedup']

package_data = \
{'': ['*']}

install_requires = \
['datasketch>=1.5.8,<2.0.0',
 'joblib>=1.2.0,<2.0.0',
 'more-itertools>=9.0.0,<10.0.0',
 'tqdm>=4.64.1,<5.0.0']

entry_points = \
{'console_scripts': ['dedup = nlp_dedup.cli:main']}

setup_kwargs = {
    'name': 'nlp-dedup',
    'version': '0.1.1',
    'description': 'Remove duplicates and near-duplicates from text corpora, no matter the scale.',
    'long_description': '# NLPDedup\n\nRemove duplicates and near-duplicates from text corpora, no matter the scale.\n\n______________________________________________________________________\n[![Documentation](https://img.shields.io/badge/docs-passing-green)](https://saattrupdan.github.io/NLPDedup/nlp_dedup.html)\n[![License](https://img.shields.io/github/license/saattrupdan/NLPDedup)](https://github.com/saattrupdan/NLPDedup/blob/main/LICENSE)\n[![LastCommit](https://img.shields.io/github/last-commit/saattrupdan/NLPDedup)](https://github.com/saattrupdan/NLPDedup/commits/main)\n[![Code Coverage](https://img.shields.io/badge/Coverage-0%25-red.svg)](https://github.com/saattrupdan/NLPDedup/tree/main/tests)\n\n\nDevelopers:\n\n- Dan Saattrup Nielsen (dan.nielsen@alexandra.dk)\n- Kenneth Enevoldsen (kennethcenevoldsen@gmail.com)\n\n\n# Installation\n\nThe package is available on PyPI, so you can install the package using your favourite\npackage manager. For instance, `pip install nlp_dedup` or `poetry add nlp_dedup`.\n\n\n# Quick start\n\nIf the corpus is stored as `corpus.txt` (both `txt` and `jsonl` files are supported),\nthe following deduplicates the corpus and stores the deduplicates corpus into the\nfolder `deduplicated`:\n\n```\n$ dedup corpus.txt deduplicated\n```\n\nThis defaults to deduplicating based on blocks of 13 consecutive words, where two\ndocuments are considered near-duplicate if they have more than 80% of these blocks in\ncommon. This can all be changed to your specific needs, however.\n\nSee `$ dedup --help` for more information on all the settings.\n',
    'author': 'Dan Saattrup Nielsen',
    'author_email': 'dan.nielsen@alexandra.dk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
