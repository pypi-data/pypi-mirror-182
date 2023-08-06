# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flowgl']

package_data = \
{'': ['*']}

install_requires = \
['requests-toolbelt>=0.10.1,<0.11.0']

setup_kwargs = {
    'name': 'flowgl',
    'version': '0.1.0',
    'description': 'Flow Immersive python client for datasets API',
    'long_description': '# Flow python client\n\nA python client for the Flow API.\n\n## Installation\n\nFirst, install [python](https://www.python.org/downloads/) and [poetry](https://python-poetry.org/docs/#installing-with-the-official-installer).\n\nThen, clone the repository, create a virtual environment, and install the dependencies.\n    \n```bash\ngit clone\ncd flow-python-client\npython -m venv venv\nsource venv/bin/activate\npoetry install\n```\n',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
