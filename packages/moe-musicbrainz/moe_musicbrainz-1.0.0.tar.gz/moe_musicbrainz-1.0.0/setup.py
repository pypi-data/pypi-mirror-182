# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['moe_musicbrainz']

package_data = \
{'': ['*']}

install_requires = \
['moe>=2.0.0,<3.0.0']

entry_points = \
{'moe.plugins': ['musicbrainz = moe_musicbrainz']}

setup_kwargs = {
    'name': 'moe-musicbrainz',
    'version': '1.0.0',
    'description': 'Template plugin repository.',
    'long_description': '###########\nMusicbrainz\n###########\nThis is a plugin for Moe utilizing the musicbrainz metadata source.\n\nCheck out the `full documentation <https://moe-musicbrainz.readthedocs.io/en/latest/>`_ for more info.\n',
    'author': 'Jacob Pavlock',
    'author_email': 'jtpavlock@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
