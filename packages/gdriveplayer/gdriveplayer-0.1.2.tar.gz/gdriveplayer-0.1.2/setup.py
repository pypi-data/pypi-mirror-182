# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['GDrivePlayer']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'gdriveplayer',
    'version': '0.1.2',
    'description': 'A python wrapper for gdriveplayer.co API',
    'long_description': "# GDrivePlayerAPI\nA python wrapper for gdriveplayer.co API\n\n### Instructions\n```python \npip install gdriveplayer\n```\n\n### Usage\n\nThe wrapper consists of 3 main classes.\n\n* `GAnime`\n* `GMovie`\n* `GDrama`\n\nEach of those classes contain very similar methods.\n\n#### `GAnime`\n\n#### Methods\n\n```python\nsearch(title: str | None = '', limit: int | str | None = 10, page: int | str | None = 1) -> List[Anime]\n```\n\nSearch an Anime. Returns a list of `Anime` Objects.\n\nThe `Anime` Object consists of several attributes such as\n\n* `id` \n* `title`\n* `poster`\n* `genre`\n* `summary`\n* `status`\n* `type`\n* `total_episode`\n* `sub`\n* `player_url`\n\n#### Example\n\n```python\nfrom GDrivePlayer import GAnime\n\ns = GAnime().search(title='Pokemon')\n```\n",
    'author': 'adenosinetp10',
    'author_email': 'adenosinetp10@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/adenosinetp10/GDrivePlayerAPI',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
