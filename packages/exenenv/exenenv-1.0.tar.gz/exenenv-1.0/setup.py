# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['exenenv']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'exenenv',
    'version': '1.0',
    'description': 'Environment variables verifier and type converter.',
    'long_description': '# ExenENV\nEnvironment variables verifier and type converter.\n\n## Installation\nLibrary is available for installation from PyPI\n```shell\n$ pip install exenenv\n```\n\n## Basic Usage\n```python\nimport os\nfrom exenenv import EnvironmentProfile\n\nos.environ["REQUIRED_VARIABLE"] = "20"  # assume it\'s set to this\n\n\nclass Environment(EnvironmentProfile):\n    REQUIRED_VARIABLE: int\n    DEFAULT_VALUE_VARIABLE: float = 30.0\n\n\nenv = Environment()\nenv.load()\n\nprint(f"{env.REQUIRED_VARIABLE=}\\n{env.DEFAULT_VALUE_VARIABLE=}")\n```\n```\nenv.REQUIRED_VARIABLE=20\nenv.DEFAULT_VALUE_VARIABLE=30.0\n```\n',
    'author': 'Exenifix',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
