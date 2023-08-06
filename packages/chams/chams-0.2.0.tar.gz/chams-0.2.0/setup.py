# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chams']

package_data = \
{'': ['*']}

install_requires = \
['openai>=0.25.0,<0.26.0', 'rich>=12.6.0,<13.0.0', 'typer>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['chams = chams.__main__:app']}

setup_kwargs = {
    'name': 'chams',
    'version': '0.2.0',
    'description': '',
    'long_description': '# chams - NLP Tasks with OpenAI GPT-3\n\nWelcome to chams, a Python package for natural language processing (NLP) tasks such as paraphrasing and email generation using OpenAI\'s GPT-3 model.\n\n## Installation\n\nyou can install chams by running the following command:\n\n```bash\npip install chams\n```\n\n## Usage\nTo use chams, you will need to set the OPENAI_API_KEY environment variable to your OpenAI API key.\n\nYou can then use the following command to generate emails with chams:\n\n```bash\nchams email "send login for the database to infrastructure team" --language "en" -n 3\n```\n\nThis will generate 3 emails with the subject "send login for the database to infrastructure team" in English.\n\nYou can also use the paraphrase command to generate paraphrased text. For example:\n    \n```bash\nchams paraphrase --text "Hello, how are you doing?" --language "en" --number 2\n```\nThis will generate 2 paraphrased versions of the text "Hello, how are you doing?" in English.\n\n## Author\nchams was created by Zakaria Fellah. You can reach him at [fellah.zakaria@yahoo.com](mailto:fellah.zakaria@yahoo.com)\n\n## License\nchams is released under the MIT license.',
    'author': 'Zakaria Fellah',
    'author_email': 'fellah.zakaria@yahoo.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
