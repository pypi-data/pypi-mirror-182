# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['e621']

package_data = \
{'': ['*']}

install_requires = \
['backports.cached-property>=1.0.1,<2.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'requests>=2.27.1,<3.0.0',
 'typing-extensions>=4.1.1,<5.0.0']

setup_kwargs = {
    'name': 'e621-stable',
    'version': '1.0.4',
    'description': 'e621.net API wrapper written in Python',
    'long_description': '# e621\n\ne621 is a feature-rich high-level e621 and e926 API wrapper.\n\nIt provides access to almost all of the endpoints available. The only exceptions are unstable and admin-only endpoints.\n\ne621 API documentation is currently highly undocumented, unstable, and sometimes even untruthful. We tried to wrap it in a sanest possible way, properly documenting all the possible ways to interact with it. However, if you still have any questions, bugs to report, or features to request -- please, create an issue on our [github page]("https://github.com/Hmiku8338/e621-py-stable") and we will reply as soon as we can.\n\n## Installation\n\n```bash\npip install e621-stable\n```\n\n## Quickstart\n\nWe translate everything the API returns to python data types created with pydantic. Everything is 100% typehinted so you get autocomplete everywhere and your IDE will warn you if you are sending invalid arguments or using nonexistent attributes.\n\n### Creating the api client\n\n* To create the most basic client, all you need to do is\n\n```python\nfrom e621 import E621\n\napi = E621()\n```\n\n* If you wish to get information about your account, use your blacklist or create/update/delete any of the e621\'s entities, you will have to create an api key and put it into the API client as such:\n\n```python\napi = E621(("your_e621_login", "your_e621_api_key"))\n```\n\n### Searching\n\nThe majority of the endpoints allow you to query for a list of their entities, be it posts, pools or tags.\n\n* To search for posts that match the "canine" but not the "3d" tag:\n\n```python\nposts = api.posts.search("canine -3d")\n# Or\nposts = api.posts.search(["canine", "-3d"])\n```\n\n* To search for pools whose names start with "hello" and end with "kitty":\n\n```python\nposts = api.pools.search(name_matches="hello*kitty")\n```\n\n* e621 searching api is paginated, which means that if you want to get a lot of posts, you will have to make multiple requests with a different "page" parameter. To simplify interactions with paginated queries, all of our searching endpoints support the "limit", "page", and "ignore_pagination" parameters. If you wish to get a specific number of entities, simply pass the "limit" and "ignore_pagination" arguments:\n\n```python\ntags = api.tags.search(name_matches="large_*", limit=900, ignore_pagination=True)\n```\n\n### Accessing Attributes\n\nWhen you have retrieved the entities, you can access any of their attributes without dealing with json.\n\n```python\nfor post in posts:\n    print(post.score.total, post.all_tags, post.relationships.parent_id)\n    with open(f"{post.id}.{post.file.ext}", "wb") as f:\n        f.write(requests.get(post.file.url).content)\n```\n\n### Getting\n\nMany entities that have unique identifiers (such as post_id or username) support indexing using these ids:\n\n```python\npost = api.posts.get(3291457)\nposts = api.posts.get([3291457, 3069995])\npool = api.pools.get(28232)\nuser = api.users.get("fox")\n```\n\n### Updating\n\n```python\napi.posts.update(3291457, tag_string_diff="canine -male", description="Rick roll?")\n```\n\n### Creating\n\n```python\nfrom pathlib import Path\n\napi.posts.create(\n    tag_string="canine 3d rick_roll",\n    file=Path("path/to/rickroll.webm"),\n    rating="s",\n    sources=[],\n    description="Rick roll?"\n)\n```\n',
    'author': 'Hmiku8338',
    'author_email': 'hmiku8338@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Hmiku8338/e621-py-stable',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
