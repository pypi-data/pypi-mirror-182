# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['artemis',
 'artemis._utilities',
 'artemis.additivity',
 'artemis.comparison',
 'artemis.importance_methods',
 'artemis.importance_methods.model_agnostic',
 'artemis.importance_methods.model_specific',
 'artemis.interactions_methods',
 'artemis.interactions_methods.model_agnostic',
 'artemis.interactions_methods.model_agnostic.partial_dependence_based',
 'artemis.interactions_methods.model_agnostic.performance_based',
 'artemis.interactions_methods.model_specific',
 'artemis.interactions_methods.model_specific.gb_trees',
 'artemis.interactions_methods.model_specific.random_forest',
 'artemis.visualizer']

package_data = \
{'': ['*']}

install_requires = \
['ipykernel>=6.17.0,<7.0.0',
 'networkx>=2.8.8,<3.0.0',
 'numpy>=1.22.0,<2.0.0',
 'pandas>=1.5.1,<2.0.0',
 'scikit-learn>=1.1.3,<2.0.0',
 'seaborn>=0.12.1,<0.13.0',
 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'pyartemis',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Artur Żółkowski',
    'author_email': 'artur.zolkowski@wp.pl',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
