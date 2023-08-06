# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['nano_duration', 'nano_duration.calendar']

package_data = \
{'': ['*']}

install_requires = \
['autoflake>=2.0.0,<3.0.0',
 'black>=22.10.0,<23.0.0',
 'flake8-fixme>=1.1.1,<2.0.0',
 'flake8>=6.0.0,<7.0.0',
 'install>=1.3.5,<2.0.0',
 'isort>=5.10.1,<6.0.0',
 'mypy>=0.991,<0.992',
 'pip>=22.3.1,<23.0.0',
 'pytest-cov>=4.0.0,<5.0.0',
 'pytest-env>=0.8.1,<0.9.0',
 'pytest>=7.2.0,<8.0.0']

setup_kwargs = {
    'name': 'nano-duration',
    'version': '0.1.2',
    'description': '',
    'long_description': '# nano_duration: Operations with ISO 8601 durations.\n\n## What is this.\n\nISO 8601 is most commonly known as a way to exchange date-times in textual format.\nto have more precision duration this package included milliseconds, microseconds, and nanoseconds\nA lesser-known aspect of the standard is the representation of durations. They have a\nshape similar to this:\n\n```\nP3Y6M4DT12H30M5S80m90u120n\n```\n\nwhich symbols defined as blow:<br />\n\n```\n"Y" -> "years"\n"M" -> "months"\n"D" -> "days"\n"H" -> "hours"\n"M" -> "minutes"\n"S" -> "seconds"\n"m" -> "miliseconds"\n"u" -> "microseconds"\n"n" -> "nanoseconds"\n```\n\nAs this module maps ISO 8601 dates/times to standard Python data type.\n\n### Parse:\n\nparses an ISO 8601 duration string into Duration object.\n\n```python\nfrom nano_duration import parse\n\nduration = parse("P3Y6M4DT12H24M12S10m80u12n")\n```\n\n### Generate:\n\ngenerate a duration object into ISO 8601 duration string\n\n```python\nfrom nano_duration import Duration, generate\n\ngenerate(\n    Duration(\n        years=3,\n        months=2,\n        days=3,\n        hours=5,\n        seconds=57,\n        miliseconds=8,\n        microseconds=30,\n        nanoseconds=20,\n    )\n)\n```',
    'author': 'xenups',
    'author_email': 'amirhossein@void-star.co',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
