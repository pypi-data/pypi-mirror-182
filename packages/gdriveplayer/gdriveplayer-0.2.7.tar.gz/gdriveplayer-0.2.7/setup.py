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
    'version': '0.2.7',
    'description': 'A python wrapper for gdriveplayer.co API',
    'long_description': '# GDrivePlayerAPI\nA python wrapper for gdriveplayer.co API\n\n### Instructions\n```python \npip install gdriveplayer\n```\n\n### Usage\n\nThe wrapper consists of 4 main classes.\n\n* `GAnime`\n* `GMovie`\n* `GDrama`\n* `GSeries`\n\nEach of those classes contain very similar methods.\n\n#### `GAnime`\n\n#### Methods\n\n```python\nsearch(title: str | None = \'\', limit: int | str | None = 10, page: int | str | None = 1) -> List[Anime]\n```\n\nSearch an Anime. Returns a list of `Anime` Objects.\n\nThe `Anime` Object consists of several attributes such as\n\n* `id` \n* `title`\n* `poster`\n* `genre`\n* `summary`\n* `status`\n* `type`\n* `total_episode`\n* `sub`\n* `player_url`\n\n#### Example\n\n```python\nfrom GDrivePlayer import GAnime\n\ns = GAnime().search(title=\'Pokemon\', limit=3)\nprint(s)\n```\n#### `Output`\n```python\n[<GDrivePlayer.anime.Anime object at 0x7f89b8d63370>, <GDrivePlayer.anime.Anime object at 0x7f89b8d633a0>, <GDrivePlayer.anime.Anime object at 0x7f89b8d63160>]\n```\n\nYou can see the attributes of individual objects by doing \n\n```python\nfrom GDrivePlayer import GAnime\n\ns = GAnime().search(title=\'Bocchi the Rock\')\n\nprint(s[0].title)\nprint(s[0].genre)\nprint(s[0].id)\nprint(s[0].status)\nprint(s[0].summary)\nprint(s[0].total_episode)\n```\n\n#### `Output`\n```\nBocchi the Rock!\nCGDCT, Comedy, Music, Slice of Life\n290813\nOngoing\nHitori Gotou is a high school girl whos starting to learn to play the guitar because she dreams of being in a band, but shes so shy that she hasnt made a single friend. However, her dream might come true after she meets Nijika Ijichi, a girl who plays drums and is looking for a new guitarist for her band.\n11\n```\n\n```python\nLatestAnimes(limit: str | int | None = 10, page: str | int | None = 1, order: str | None = "last_updated", sort: str | None = "DESC") -> List[Anime]\n```\n\nReturns a list of `LatestAnime` objects. The `LatestAnime` object is very similar to `Anime` object. The only difference is that the former doesn\'t contain `summary` attribute. This is due to the original API\'s structure.\n\n```python\nanimeDetail(id: str | int) -> Anime\n```\n\nReturns `Anime` Object of the `id` that is passed to the method.\n\n#### Example\n\n```python\nfrom GDrivePlayer import GAnime\n\ns = GAnime().animeDetail(id=290813)\n\nprint(s)\nprint(s.title)\nprint(s.summary)\n```\n\n#### `Output`\n\n```\n<GDrivePlayer.anime.Anime object at 0x7f7e68282290>\nBocchi the Rock!\nHitori Gotou is a high school girl whos starting to learn to play the guitar because she dreams of being in a band, but shes so shy that she hasnt made a single friend. However, her dream might come true after she meets Nijika Ijichi, a girl who plays drums and is looking for a new guitarist for her band.\n```\n\nThe classes such as `GDrama`, `GMovie` and `GSeries` also contain similar methods and similar Objects like `Anime` and `LatestAnime`.\n\n\n### Disclaimer\n\nThe developer of this wrapper is in no way responsible for how the user utilises, modifies and/or accesses this wrapper.\n',
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
