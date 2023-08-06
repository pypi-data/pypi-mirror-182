# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['compsyn']

package_data = \
{'': ['*']}

install_requires = \
['Pillow',
 'beautifulsoup4',
 'black',
 'boto3',
 'google-api-core',
 'google-auth',
 'google-cloud',
 'google-cloud-vision',
 'googleapis-common-protos',
 'grpcio',
 'ipykernel',
 'ipython',
 'kymatio',
 'matplotlib',
 'memory-profiler',
 'nltk',
 'notebook',
 'numba',
 'pandas',
 'pytest',
 'pytest-cov',
 'pytest-depends',
 'qloader',
 'requests',
 'scikit-image',
 'scikit-learn',
 'seaborn',
 'textblob',
 'toml']

setup_kwargs = {
    'name': 'compsyn',
    'version': '1.0.2',
    'description': 'python package to explore the color of language',
    'long_description': 'None',
    'author': 'comp-syn',
    'author_email': 'group@comp-syn.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
