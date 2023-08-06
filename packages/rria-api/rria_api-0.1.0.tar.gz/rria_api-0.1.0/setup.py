# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['robot-api', 'robot-api.gen3', 'robot-api.gen3.api_gen3', 'robot-api.ned']

package_data = \
{'': ['*']}

install_requires = \
['pyniryo>=1.1.2,<2.0.0']

setup_kwargs = {
    'name': 'rria-api',
    'version': '0.1.0',
    'description': '',
    'long_description': '# robot-api\n Robot API\n\nLinks Úteis:\nhttps://docs.niryo.com/dev/ros/v4.1.1/en/source/overview.html',
    'author': 'felipeadsm',
    'author_email': '97059009+felipeadsm@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
