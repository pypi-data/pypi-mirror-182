# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypod']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'pyaudio>=0.2.12,<0.3.0',
 'rich>=12.6.0,<13.0.0',
 'textual>=0.6.0,<0.7.0']

entry_points = \
{'console_scripts': ['pypod = pypod.cli:cli']}

setup_kwargs = {
    'name': 'python-pod',
    'version': '0.1.0',
    'description': 'Python terminal music player',
    'long_description': '## PyPod\n\nPython console music player\n\n```bash\n$ brew install portaudio\n$ poetry install\n```\n\n\n### Usage\n```bash\n$ pypod <path-to-directory>\n$ pypod filename.wav\n```\n',
    'author': 'Misha Behersky',
    'author_email': 'bmwant@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
