# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['sealedsecretmgr']

package_data = \
{'': ['*']}

install_requires = \
['black>=22.12.0,<23.0.0']

entry_points = \
{'console_scripts': ['sealedsecret = sealedsecretmgr.cli:__main__']}

setup_kwargs = {
    'name': 'sealedsecretmgr',
    'version': '0.1.0',
    'description': 'SealedSecret Manager',
    'long_description': '`sealedsecret`: A tool to manage [SealedSecrets](https://github.com/bitnami-labs/sealed-secrets)\n\n## Installation\n\n`pipx install sealedsecretmgr`\n\n## Usage\n\nTo list existing SealedSecrets with keys in your namespace\n\n```\n$ sealedsecret list\nmy-super-secret\n\tDATABASE_PASSWORD\n```\n\nYou can pass an optional `--namespace` argument.\n\n\nTo retrieve and view a SealedSecret you can get it.\n\n```\nsealedsecret get secret-name\n```\n\nTo create a new SealedSecret:\n```\nsealedsecret create new-secret-name my-key my-value-to-protect\n```\n\nTo add a key or edit an existing key in an exitsing SealedSecret:\n```\nsealedsecret update existing-secret-name my-new-key a-value\n```\n\nThe update and create commands only print the resource, you can redirect the output of edit an update to a file and then apply it using `kubectl apply -f` or you can pipe directly to `kubectl apply -`\n',
    'author': 'David Vincelli',
    'author_email': 'david.vincelli@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/dvincelli/sealedsecretmgr',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
