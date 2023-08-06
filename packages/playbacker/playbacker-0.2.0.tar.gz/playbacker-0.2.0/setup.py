# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['playbacker', 'playbacker.app', 'playbacker.core', 'playbacker.core.tracks']

package_data = \
{'': ['*'], 'playbacker': ['dist/*', 'dist/assets/*']}

install_requires = \
['PyYAML==6.0',
 'SoundFile==0.11.0',
 'fastapi==0.88.0',
 'inquirer==3.1.1',
 'numpy==1.24.0',
 'pydantic==1.10.2',
 'sounddevice==0.4.5',
 'soxr==0.3.3',
 'sse-starlette==1.2.1',
 'typer[all]==0.7.0',
 'uvicorn[standard]==0.20.0',
 'uvloop==0.17.0',
 'watchfiles==0.18.1']

entry_points = \
{'console_scripts': ['playbacker = playbacker.main:cli']}

setup_kwargs = {
    'name': 'playbacker',
    'version': '0.2.0',
    'description': 'Live music performance playback',
    'long_description': 'None',
    'author': 'Lev Vereshchagin',
    'author_email': 'mail@vrslev.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
