# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['garpyclient']

package_data = \
{'': ['*'], 'garpyclient': ['resources/*']}

install_requires = \
['PyYAML>=5.1,<7.0', 'requests>=2.22,<3.0']

extras_require = \
{'cloudscraper': ['cloudscraper>=1.2.58,<2.0.0']}

setup_kwargs = {
    'name': 'garpyclient',
    'version': '0.1.1',
    'description': 'Basic library for authenticating and querying Garmin Connect',
    'long_description': '# Garpyclient: Basic library for authenticating and querying Garmin Connect\n\n\n[![PyPI-Status](https://img.shields.io/pypi/v/garpyclient.svg)](https://pypi.org/project/garpyclient)\n[![Tests](https://github.com/felipeam86/garpyclient/actions/workflows/test.yml/badge.svg)](https://github.com/felipeam86/garpyclient/actions/workflows/test.yml) \n[![Coveralls](https://coveralls.io/repos/github/felipeam86/garpyclient/badge.svg?branch=develop)](https://coveralls.io/github/felipeam86/garpyclient?branch=develop)\n\n\n\n`garpyclient` is a simple library to communicate with Garmin Connect. It was extracted from\n[garpy](https://github.com/felipeam86/garpy) and the idea is for this to become the core client\nlibrary of it in a next iteration. Ideally, `garpyclient` is intended to be used by other python libraries that want to download their data from Garmin Connect. It is kept simple on purpose so that\nend users can build upon it with their own workflows. As an example, the following code will fetch the \nlatest activity from your Garmin profile:\n\n\n```python\nfrom garpyclient import GarminClient\n\nwith GarminClient(username="user", password="pass") as client:\n    activities = client.list_activities()\n    response = client.get_activity(activities[0]["activityId"], fmt="original")\n```\n\nThe file content will be found in `response.content`. The format of the file will depend on the parameter `fmt` to which you can pass the following values:\n\n- For an overview of the activities: `summary` or `details`\n- For data points of the activity: `gpx`, `tcx`, `original` (usually fit format) and `kml`.\n\n\n## Installation\n\n``garpyclient`` requires Python 3.7 or higher on your system. \nInstall with pip as follows:\n\n\n```bash\n    pip install -U garpyclient\n```\n\nIf you are new to Python, I recommend you install [Miniconda](https://docs.conda.io/en/latest/miniconda.html). To my knowledge, it is the simplest way of installing a robust and\nlightweight Python environment.\n\n\n## Acknowledgements\n\nThe original library ([garpy](https://github.com/felipeam86/garpy)) is based on\n[garminexport](https://github.com/petergardfjall/garminexport). I borrowed the GarminClient, refactored it to my taste and created a package from it.\n\n',
    'author': 'Felipe Aguirre Martinez',
    'author_email': 'felipeam86@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/felipeam86/garpyclient',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.9,<4.0.0',
}


setup(**setup_kwargs)
