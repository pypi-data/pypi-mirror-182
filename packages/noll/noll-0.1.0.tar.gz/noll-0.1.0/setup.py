# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['noll']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'noll',
    'version': '0.1.0',
    'description': 'Nothing. Nil. Nada.',
    'long_description': '# Noll\n\n**Nothing. Nil. Nada.**\n\nAn object that is as not there as I could conjure up.\n\nYou can safely index it and compare with it. It will always return an untruthy value, whether that be `0`, `""`, or itself whenever possible.\n\n```py\nfrom noll import Noll\n\nNoll().index.whatever[\'and\'].you.will.always.end.up[\'with\'].a.Noll[\'object\']\n```\n',
    'author': 'Maximillian Strand',
    'author_email': 'maxi@millian.se',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/deepadmax/noll',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
