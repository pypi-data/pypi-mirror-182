# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyspark_factories',
 'pyspark_factories.handlers',
 'pyspark_factories.value_generators']

package_data = \
{'': ['*']}

install_requires = \
['Faker>=13.3.1,<14.0.0', 'dotmap>=1.3.30,<2.0.0', 'pyspark>=3.2.1,<4.0.0']

setup_kwargs = {
    'name': 'pyspark-factories',
    'version': '0.0.1',
    'description': 'Create pyspark dataframes with randomly generated data from structschema',
    'long_description': 'None',
    'author': 'Daan Rademaker',
    'author_email': 'd.v.rademaker@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
