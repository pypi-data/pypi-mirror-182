# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pysurrealdb', 'pysurrealdb.clients', 'pysurrealdb.tests']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pysurrealdb',
    'version': '0.1.0',
    'description': 'A library to connect to SurrealDB.',
    'long_description': '# PySurrealDB\nAn unofficial library to connect to SurrealDB.\n\nThe official surreal library is only async, has a lot of dependancies, and is currently undocumented.\n\n---\n## Getting Started\n\nIf you don\'t already have it, install [SurrealDB](https://surrealdb.com/docs/start/installation)\n\nLinux: \n``` bash\n$ curl -sSf https://install.surrealdb.com | sh\n# then\n$ surreal start --user test --pass test\n```\n\n\n### Install PySurrealDB\nPySurrealDB currently has no dependancies, so it can be used on its own by cloning the repo.\n\n\n\n### Examples\n\n```python\nimport pysurrealdb as surreal\n\nconn = surreal.connect(user=\'test\', password=\'test\')\n\nconn.create(\'person\', {\'name\': \'Mike\'})\nconn.query(\'select * from person\')\n```\n\nTo connect to a live SurrealDB server, you can specify the connection info either in the connect call, or in a config file.\n\n```python\nimport pysurrealdb as surreal\nconn = surreal.connect(host=\'surreal.com\', port=8000, user=\'user\', password=\'pass\', database=\'db\', namespace=\'ns\')\n```\n\nOptional Config file:\n```python\n# use a configured connection. \nconn = surreal.connection(\'default\')\n# Requires pysurrealdb.json file. Place it in your root directory, or specify the file location with the env variable \'PYSURREALDB_CONFIG\'.\n\nExample pysurrealdb.json:\n{\n    "connections": {\n        "default": {\n            "host": "localhost",\n            "port": 8000,\n            "user": "test",\n            "password": "test"\n            "database": "test",\n            "namespace": "test",\n        }\n    }\n}\n```\n\n\n## Query Builder\n\nYou can write queries using laravel and masonite style syntax:\n```python\nimport pysurrealdb as surreal\nconn = surreal.connection()\n\n# setup data\nconn.drop(\'person\')\nconn.insert(\'person\', [{\'name\': \'Mike\', \'age\': 31}, {\'name\':\'Mr P\'}])\n\n# query builder examples\nfirst_person = conn.table(\'person\').where(\'name\', \'Mike\').first()\n\nadults = conn.table(\'person\').where(\'age\', \'>=\', 18).order_by(\'age\', \'desc\').limit(10).get()\n```\n\n\nThis project is a work in progress. Please email aurelion314@gmail.com if you have any questions or feedback. Thanks!',
    'author': 'Aurelion314',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
