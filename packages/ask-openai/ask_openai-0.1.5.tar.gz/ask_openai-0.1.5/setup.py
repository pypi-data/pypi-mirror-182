# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ask_openai']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ask-openai',
    'version': '0.1.5',
    'description': 'Explain exceptions using OpenAI',
    'long_description': "This package provides a single minimal implementation\nof a function decorator `ask`.\n\nIf the decorated function raises an error,\nthe decorator asks OpenAI to explain it to you.\n\nUse as follows:\n\n```Python\nimport os\nfrom ask_openai import ask\n\nask = ask(api_key=os.environ['OPENAI_API_KEY'], logger=print)\n\n\n@ask\ndef f(x):\n    return 1 / 0\n```\n\nThis will print something like:\n\n```commandline\nOpenAI explanation: Division by zero is an error because a number cannot be divided by 0.\n```\n",
    'author': 'RA',
    'author_email': 'numpde@null.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
