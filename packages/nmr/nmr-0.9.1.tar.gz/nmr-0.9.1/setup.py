# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nmr', 'nmr.types']

package_data = \
{'': ['*']}

install_requires = \
['chess>=1.9.3,<2.0.0',
 'datacls>=4.5.0,<5.0.0',
 'dtyper>=2.0.0,<3.0.0',
 'lat-lon-parser>=1.3.0,<2.0.0',
 'typer>=0.7.0,<0.8.0',
 'xmod>=1.3.2,<2.0.0']

setup_kwargs = {
    'name': 'nmr',
    'version': '0.9.1',
    'description': '🔢 name all canonical things 🔢',
    'long_description': "🔢 ``nmr``: name all canonical things 🔢\n\nConvert each canonical thing into a number, and then that number into a unique,\nnon-repeating name from a short list of common, short English words... or use a\nword list of your choice.\n\nInstalls both a module named ``nmr`` and an executable called ``nmr.py``\n\nEXAMPLE\n=========\n\n.. code-block:: python\n\n    import nmr\n\n    assert nmr(0) == ['the']\n    assert nmr(2718281828) == ['the', 'race', 'tie', 'hook']\n\n    for i in range(-2, 3):\n        print(i, ':', *nmr(i))\n\n    # Prints\n    #   -2 : to\n    #   -1 : of\n    #   0 : the\n    #   1 : and\n    #   2 : a\n",
    'author': 'Tom Ritchford',
    'author_email': 'tom@swirly.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
