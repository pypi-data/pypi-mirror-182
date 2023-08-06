# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['epub_metadata']

package_data = \
{'': ['*']}

install_requires = \
['arrow>=1.2.3,<2.0.0']

setup_kwargs = {
    'name': 'epub-metadata',
    'version': '1.0.0b0',
    'description': '',
    'long_description': '# epub-metadata\nGet metadata from the Epub file.\n\n# Install\n```bash\npip install epub-metadata\n```\n\n# Example\n\n```python\nimport epub_metadata\nepub = epub_metadata.epub(\'tests/Alices Adventures in Wonderland.epub\')\n```\n\nshow all metadata from the Epub file\n\n```python\nprint(epub.metadata)\n# return all metadata from the Epub file\n{\n    \'version\': \'2.0\', \n    \'title\': "Alice\'s Adventures in Wonderland", \n    \'creator\': \'Lewis Carroll\', \n    \'date\': \'1865-07-04\', \n    \'cover\': \'/9j/4AAQSkZJRgABAQE...\', \n    \'cover_type\': \'image/jpeg\', \n    \'description\': \'\', \n    \'publisher\': \'D. Appleton and Co\', \n    \'identifier\': \'eb2934ae-bb1a-4652-bce7-9f78fc5ca496\'\n}\n```\n\nonly show the epub metadata\n```python\nprint(epub.metadata.title)\n# only print the title\nAlice\'s Adventures in Wonderland\n```',
    'author': 'ThanatosDi',
    'author_email': 'yykkold55tw@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
