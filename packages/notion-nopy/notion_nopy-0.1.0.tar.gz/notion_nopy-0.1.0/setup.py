# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nopy', 'nopy.objects', 'nopy.props']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.1,<0.24.0', 'python-dateutil>=2.8.2,<3.0.0']

setup_kwargs = {
    'name': 'notion-nopy',
    'version': '0.1.0',
    'description': 'An unofficial OOP interface for the Notion API.',
    'long_description': '# Welcome to NoPy!\n\nNoPy is an unofficial OOP interface for the [Notion API](https://developers.notion.com/reference/intro).\n\n## Installation\n\nTODO.\n\n## Getting Started\n\nCreate an instance of a `NotionClient` and pass in your integration token. Refer the [docs](https://developers.notion.com/docs/authorization#set-up-the-auth-flow-for-an-internal-integration) to find out how to set up the integration token and more.\n\n```python\n\nfrom nopy import NotionClient\n\nclient = NotionClient("your-notion-integration-token")\n\ndb = client.retrieve_db("your-db-id")\n\nprint(db.title) # The database title.\nprint(db.description) # The database description.\n\n# Getting all the pages in the database.\nfor page in db.get_pages():\n    print(page.title) # The page title.\n\n# Closing the client.\nclient.close()\n```\n\n**NOTE**: Instead of passing in the integration token, you could instead store the token in the environment variables with the key `NOTION_TOKEN`.\n',
    'author': 'Visakh Unnikrishnan',
    'author_email': 'visakhcu96@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
