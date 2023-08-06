# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kilroy_face_discord',
 'kilroy_face_discord.resources',
 'kilroy_face_discord.scoring']

package_data = \
{'': ['*']}

install_requires = \
['detoxify>=0.5,<0.6',
 'hikari==2.0.0.dev109',
 'kilroy-face-server-py-sdk>=0.9,<0.10',
 'numpy>=1.23,<2.0',
 'omegaconf>=2.2,<3.0',
 'platformdirs>=2.5,<3.0',
 'pydantic[dotenv]>=1.10,<2.0',
 'typer[all]>=0.6,<0.7']

entry_points = \
{'console_scripts': ['kilroy-face-discord = kilroy_face_discord.__main__:cli',
                     'kilroy-face-discord-fetch-models = '
                     'kilroy_face_discord.models:fetch_models']}

setup_kwargs = {
    'name': 'kilroy-face-discord',
    'version': '0.7.1',
    'description': 'kilroy face for Discord 🎮',
    'long_description': '<h1 align="center">kilroy-face-discord</h1>\n\n<div align="center">\n\nkilroy face for Discord 🎮\n\n[![Lint](https://github.com/kilroybot/kilroy-face-discord/actions/workflows/lint.yaml/badge.svg)](https://github.com/kilroybot/kilroy-face-discord/actions/workflows/lint.yaml)\n[![Multiplatform tests](https://github.com/kilroybot/kilroy-face-discord/actions/workflows/test-multiplatform.yaml/badge.svg)](https://github.com/kilroybot/kilroy-face-discord/actions/workflows/test-multiplatform.yaml)\n[![Docker tests](https://github.com/kilroybot/kilroy-face-discord/actions/workflows/test-docker.yaml/badge.svg)](https://github.com/kilroybot/kilroy-face-discord/actions/workflows/test-docker.yaml)\n[![Docs](https://github.com/kilroybot/kilroy-face-discord/actions/workflows/docs.yaml/badge.svg)](https://github.com/kilroybot/kilroy-face-discord/actions/workflows/docs.yaml)\n\n</div>\n\n---\n\n## Installing\n\nUsing `pip`:\n\n```sh\npip install kilroy-face-discord\n```\n\n## Usage\n\nTo run the face server, install the package and run the following command:\n\n```sh\nkilroy-face-discord\n```\n\nThis will start the face server on port 10000 by default.\nThen you can communicate with the server, for example by using\n[this package](https://github.com/kilroybot/kilroy-face-client-py-sdk).\n',
    'author': 'kilroy',
    'author_email': 'kilroymail@pm.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kilroybot/kilroy-face-discord',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
