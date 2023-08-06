# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tiktokpy',
 'tiktokpy.bot',
 'tiktokpy.cli',
 'tiktokpy.client',
 'tiktokpy.models',
 'tiktokpy.models.html',
 'tiktokpy.parsers',
 'tiktokpy.utils']

package_data = \
{'': ['*']}

install_requires = \
['dynaconf>=3.0.0,<4.0.0',
 'humanize>=4.0.0,<5.0.0',
 'loguru>=0.6.0,<0.7.0',
 'playwright-stealth>=1.0.5,<2.0.0',
 'playwright>=1.18.2,<2.0.0',
 'pydantic>=1.6.1,<2.0.0',
 'tqdm>=4.48.0,<5.0.0',
 'typer>=0.4.0,<0.5.0']

extras_require = \
{'html': ['parsel>=1.6.0,<2.0.0']}

entry_points = \
{'console_scripts': ['tiktokpy = tiktokpy.cli:app']}

setup_kwargs = {
    'name': 'tiktokpy',
    'version': '0.9.1',
    'description': 'Tool for automated TikTok interactions.',
    'long_description': '<h1 align="center" style="font-size: 3rem;">\nTikTokPy\n</h1>\n<p align="center">\n <em>Tooling that <b>automates</b> your social media interactions to “farm” Likes and Followers on TikTok</em></p>\n\n<p align="center">\n<a href="https://travis-ci.com/sudoguy/tiktokpy">\n    <img src="https://travis-ci.com/sudoguy/tiktokpy.svg?branch=master" alt="Build Status">\n</a>\n<a href="https://pypi.org/project/tiktokpy/">\n    <img src="https://badge.fury.io/py/tiktokpy.svg" alt="Package version">\n</a>\n</p>\n\n---\n\n## Quickstart.py\n\n```python\nimport asyncio\nfrom tiktokpy import TikTokPy\n\n\nasync def main():\n    async with TikTokPy() as bot:\n        # Do you want to get trending videos? You can!\n        trending_items = await bot.trending(amount=5)\n\n        for item in trending_items:\n            # ❤️ you can like videos\n            await bot.like(item)\n            # or unlike them\n            await bot.unlike(item)\n            # or follow users\n            await bot.follow(item.author.username)\n            # as and unfollow\n            await bot.unfollow(item.author.username)\n\n        # 😏 getting user\'s feed\n        user_feed_items = await bot.user_feed(username="justinbieber", amount=5)\n\n        for item in user_feed_items:\n            # 🎧 get music title, cover, link, author name..\n            print("Music title: ", item.music.title)\n            # #️⃣ print all tag\'s title of video\n            print([tag.title for tag in item.challenges])\n            # 📈 check all video stats\n            print("Comments: ", item.stats.comments)\n            print("Plays: ", item.stats.plays)\n            print("Shares: ", item.stats.shares)\n            print("Likes: ", item.stats.likes)\n\n        # and many other things 😉\n\n\nasyncio.run(main())\n```\n\n## Installation\n\nInstall with pip:\n\n```shell\npip install tiktokpy\n```\n\nInstall browser by playwright\n\n```shell\nplaywright install chromium\n```\n\nIf you have little to no knowledge in programming: Read this Guide ["How to use TiktokPy Python Bot"](https://my-tailwind-nextjs-starter-blog.vercel.app/blog/how-to-use-tiktokpy-for-beginner-programmers-indepth-guide) for beginners\n\n## Run\n\nTo create your cookies and settings.toml file simply run\n\n```shell\npython quicklogin.py\n```\nand then after you login run\n\n```shell\npython quickstart.py\n```\n',
    'author': 'Evgeny Kemerov',
    'author_email': 'eskemerov@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/sudoguy/tiktokpy/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
