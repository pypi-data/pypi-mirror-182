# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['slack_okta_bot']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0', 'slack-bolt>=1.16.1,<2.0.0']

entry_points = \
{'console_scripts': ['slack-okta-bot = slack_okta_bot:slack.run_local']}

setup_kwargs = {
    'name': 'slack-okta-bot',
    'version': '0.0.1',
    'description': 'Provides quick access to Okta user management from Slack',
    'long_description': 'None',
    'author': 'Mathew Moon',
    'author_email': 'me@mathewmoon.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mathewmoon/slack-okta-bot',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
