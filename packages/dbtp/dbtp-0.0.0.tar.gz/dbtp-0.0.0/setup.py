# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dbt_py', 'dbt_py.cli']

package_data = \
{'': ['*']}

install_requires = \
['rcheck>=0.0.7,<0.0.8']

setup_kwargs = {
    'name': 'dbtp',
    'version': '0.0.0',
    'description': 'Run DBT CLI commands in python',
    'long_description': "# dbt-py\n\nA python library to run dbt cli commands.\n\nAdapted from dagster's dbt resource: https://github.com/dagster-io/dagster/tree/master/python_modules/libraries/dagster-dbt.\n\n# dagster-dbt\n\nThe docs for `dagster-dbt` can be found\n[here](https://docs.dagster.io/_apidocs/libraries/dagster-dbt).\n\nDeleted:\n    * setup.cfg and setup.py in favor of using poetry\n",
    'author': 'Alex Rudolph',
    'author_email': 'alex3rudolph@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
