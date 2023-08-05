# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vhpy']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'vhpy',
    'version': '0.1.0',
    'description': "V&H (or 'V and H' or 'VH') Coordinates in Python",
    'long_description': 'V&H (or \'V and H\' or \'VH\') Coordinates in Python\n\nI created a python class to do V&H coordinate math and conversions. It\'s something I\'ve done before in perl, and seemed like it might be useful to someone.\n\nFor those of you who don\'t know what V&H coordinates are, consider yourself lucky. V&H coordinates are an old system, created in the late fifties, to map locations for AT&T. According to Voip-Info.org, the system was designed to be easy to use with a slide rule.\n\nAT&T dropped a gird over the US, placed at an angle, so it could get most of Canada, all of the 48 states, and some of Cuba. This allowed an approximate location for any AT&T telephone switch on a grid of roughly 10000 x 10000 points with no fractions or extra decimal places. Hawaii and Alaska don\'t fit in the 10000 x 10000 scheme, but work fine with bigger numbers.\n\nTelcordia has a hillarious map showing how add-hoc V&H is on this [page](https://web.archive.org/web/20100430211425/http://www.trainfo.com/products_services/tra/vhpage.html)\n![Telcordia V&H Map](https://web.archive.org/web/20110716141834im_/http://www.trainfo.com/images/products_services/trainfo/Vhpgmap1.gif "Telcordia V&H Map")\n\nIf you\'ve never used V&H before then there\'s nothing for you to see here. Look at the Telcordia map, have a chuckle and move on.\n\nBut for those of you in the telco field who need a python module for V&H, here it is.\n\nThe class file: [VH.py](http://www.burgerbum.com/python/VH.py)\nThe test file: [testVH.py](http://www.burgerbum.com/python/testVH.py)\n\n----\nPaul Pomerleau is the author of [Networking for English Majors](http://www.burgerbum.com/networkingforenglishmajors.com), which teaches people with liberal arts and social science degrees how to get jobs in computer networking. You don\'t need a computer science degree to get a well-paying job in computing.\n\n\n\n## Release Process\nTODO: Figure out the best steps to do a release.\n\nUpdate [CHANGELOG.md](./CHANGELOG.md)\n\n\n```shell\npoetry version patch\ngit add -p\ngit commit -m "bump version"\ngit push\n```',
    'author': 'Paul Pomerleau',
    'author_email': 'None',
    'maintainer': 'Kurt Abersold',
    'maintainer_email': 'kurtabersold@gmail.com',
    'url': 'https://github.com/kurtabersold/vhpy',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
