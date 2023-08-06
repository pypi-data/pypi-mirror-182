# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['graph_searcher',
 'graph_searcher.data_structures',
 'graph_searcher.data_structures.edge',
 'graph_searcher.data_structures.graph',
 'graph_searcher.data_structures.vertex',
 'graph_searcher.ui',
 'graph_searcher.ui.cli']

package_data = \
{'': ['*']}

install_requires = \
['celluloid', 'matplotlib', 'numpy', 'spatialmath-python']

entry_points = \
{'console_scripts': ['graph_searcher = graph_searcher.ui.cli.cli:main']}

setup_kwargs = {
    'name': 'graph-searcher',
    'version': '0.1.0',
    'description': 'A visual representation of search algorithms for graphs',
    'long_description': '# graph searcher\n',
    'author': 'Pablo',
    'author_email': 'pablohuggem@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
