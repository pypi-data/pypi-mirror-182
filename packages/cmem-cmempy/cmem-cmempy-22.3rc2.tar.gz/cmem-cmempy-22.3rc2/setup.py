# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cmem',
 'cmem.cmempy',
 'cmem.cmempy.custom_tasks',
 'cmem.cmempy.dp',
 'cmem.cmempy.dp.admin',
 'cmem.cmempy.dp.authorization',
 'cmem.cmempy.dp.proxy',
 'cmem.cmempy.dp.titles',
 'cmem.cmempy.health',
 'cmem.cmempy.linking',
 'cmem.cmempy.plugins',
 'cmem.cmempy.queries',
 'cmem.cmempy.transform',
 'cmem.cmempy.transform.rules',
 'cmem.cmempy.vocabularies',
 'cmem.cmempy.workflow',
 'cmem.cmempy.workspace',
 'cmem.cmempy.workspace.activities',
 'cmem.cmempy.workspace.export_',
 'cmem.cmempy.workspace.import_',
 'cmem.cmempy.workspace.projects',
 'cmem.cmempy.workspace.projects.datasets',
 'cmem.cmempy.workspace.projects.resources',
 'cmem.cmempy.workspace.search',
 'cmem.cmempy.workspace.tasks']

package_data = \
{'': ['*']}

install_requires = \
['certifi>=2022.12.7,<2023.0.0',
 'pyparsing>=3.0.9,<4.0.0',
 'pysocks>=1.7.1,<2.0.0',
 'rdflib>=6.2.0,<7.0.0',
 'requests-toolbelt>=0.10.1,<0.11.0',
 'requests>=2.28.1,<3.0.0',
 'six>=1.16.0,<2.0.0']

setup_kwargs = {
    'name': 'cmem-cmempy',
    'version': '22.3rc2',
    'description': 'API wrapper for eccenca Corporate Memory',
    'long_description': '# cmempy\n\ncmempy is a Python API wrapper for [eccenca Corporate Memory](https://documentation.eccenca.com/).\n\n## Installation\n\nTo install the Python library run:\n\n    pip install cmem-cmempy\n\nYou may consider installing the package only for the current user:\n\n    pip install cmem-cmempy --user\n\n## Configuration and Usage\n\ncmempy is intended for Linked Data Experts to interface with the eccenca Corporate Memory backend components DataIntegration and DataPlatform.\n\nThe cmempy manual including basic usage patterns and configuration is available at:\n\n[https://eccenca.com/go/cmempy](https://eccenca.com/go/cmempy)\n\ncmempy works with Python 2.7 as well as with Python 3.\n',
    'author': 'eccenca GmbH',
    'author_email': 'cmempy-developer@eccenca.com',
    'maintainer': 'Sebastian Tramp',
    'maintainer_email': 'sebastian.tramp@eccenca.com',
    'url': 'https://eccenca.com/go/cmempy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3,<4',
}


setup(**setup_kwargs)
