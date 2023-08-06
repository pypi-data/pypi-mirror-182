# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['paperview', 'paperview.retrieval']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.3.0,<10.0.0',
 'PyMuPDF>=1.21.1,<2.0.0',
 'PyPDF2>=2.12.1,<3.0.0',
 'attrs>=22.1.0,<23.0.0',
 'boto3>=1.26.32,<2.0.0',
 'bs4>=0.0.1,<0.0.2',
 'ipykernel>=6.19.4,<7.0.0',
 'jupyter>=1.0.0,<2.0.0',
 'notebook>=6.5.2,<7.0.0',
 'pdfminer.six>=20221105,<20221106',
 'pikepdf>=6.2.6,<7.0.0',
 'pre-commit>=2.20.0,<3.0.0',
 'pytest>=7.2.0,<8.0.0',
 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'paperview',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'anaka',
    'author_email': 'alex.naka@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
