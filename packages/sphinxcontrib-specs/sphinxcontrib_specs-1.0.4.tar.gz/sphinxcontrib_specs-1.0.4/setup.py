# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['sphinxcontrib', 'sphinxcontrib.specs']

package_data = \
{'': ['*'], 'sphinxcontrib.specs': ['theme/*', 'theme/static/*']}

setup_kwargs = {
    'name': 'sphinxcontrib-specs',
    'version': '1.0.4',
    'description': 'Extensions for building Specializations content.',
    'long_description': 'None',
    'author': 'Ashley Trinh',
    'author_email': 'ashley@hackbrightacademy.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
