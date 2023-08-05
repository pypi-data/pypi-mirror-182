# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['bettered']
install_requires = \
['moe-transcode>=1.1.0,<2.0.0']

entry_points = \
{'console_scripts': ['bettered = bettered:main']}

setup_kwargs = {
    'name': 'bettered',
    'version': '1.1.0',
    'description': 'Automatic helper for redacted better.php.',
    'long_description': '# BetteRED\n\n## Introduction\nbettered automatically transcodes a given path of flac files to mp3 files based on desired quality (MP3 V0 or MP3 320) and creates a corresponding torrent file with a specified announce url.\n\nbettered uses [Moe](https://github.com/MoeMusic/Moe) to initialize and read the configuration, and the plugin [moe_transcode](https://github.com/MoeMusic/moe_transcode) to handle the transcoding logic.\n\n## Installation:\n\n### 1. Install `bettered` from PyPI\n\nI recommend using [pipx](https://pypa.github.io/pipx/) to install `bettered`.\n`$ pipx install bettered`\n\nIf you don\'t care about having `bettered` and it\'s dependencies (mainly `Moe`) in an isolated environment, you can just install normally with pip as well.\n`$ pip install bettered`\n\n### 2. Install `mktorrent`\n`mktorrent` must be built from source unless your package manager includes >=v1.1\n\n~~~\n$ git clone https://github.com/Rudde/mktorrent.git\n$ cd mktorrent\n$ sudo make install\n~~~\n\n### 3. Install `ffmpeg`\nhttps://ffmpeg.org/download.html\n\nRun `ffmpeg -h` to ensure it\'s in your path.\n\n### 4. Configure\n\nYour configuration file should exist in "~/.config/bettered/config.toml" and should look like the following:\n\n``` toml\nenable_plugins = ["transcode"]\n\n[transcode]\ntranscode_path = "~/transcode"\n\n[bettered]\ntorrent_file_path = "~/torrents"\nannounce_url = "https://flacsfor.me/213/announce"\n\n[move]\nalbum_path = "{album.artist} - {album.title} ({album.year})"\n```\n\n`transcode_path` is where the transcoded albums will be placed.\n`torrent_file_path` is where the `.torrent` files will be places\n`announce_url` your announce url for your tracker of choice.\n`album_path` is the format of the album path. This will also have the bitrate automatically appended. See the [Moe docs](https://mrmoe.readthedocs.io/en/latest/plugins/move.html#path-configuration-options) for more information on customizing this value.\n\n### 5. Run\n`bettered -h`\n\n## Contributing:\n\n#### 1. Fork the repository and create a feature/bug fix branch\n\n#### 2. Install development requirements\n`$ poetry install`\n\n#### 3. Hack away\n\n#### 4. Lint your code\n`$ pre-commit run -a`\n\n#### 5. Submit a pull request\n',
    'author': 'Jacob Pavlock',
    'author_email': 'jtpavlock@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/jtpavlock/bettered',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
