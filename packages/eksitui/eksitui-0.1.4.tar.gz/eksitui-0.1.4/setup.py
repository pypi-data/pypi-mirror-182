# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eksitui']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0', 'textual>=0.8.0,<0.9.0']

entry_points = \
{'console_scripts': ['eksi = eksitui.__main__:main']}

setup_kwargs = {
    'name': 'eksitui',
    'version': '0.1.4',
    'description': 'TUI for Turkish collaborative hypertext dictionary ekşi sözlük.',
    'long_description': '<div align="center">\n<img src="https://user-images.githubusercontent.com/16024979/203560629-9138dfc5-dd6f-492a-be2a-0f2ef168c1b4.png" alt="eksitui screenshot"/>\n<a href="https://github.com/agmmnn/eksitui/releases">\n<img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/agmmnn/eksitui"></a>\n<a href="https://pypi.org/project/eksitui/">\n<img alt="PyPI" src="https://img.shields.io/pypi/v/eksitui"></a>\n\nTerminal User Interface for Turkish collaborative hypertext dictionary [ekşi sözlük](https://eksisozluk.com/). With the power of the [textual](https://github.com/Textualize/textual) framework.\n\n</div>\n\n## Install\n\n```\npip install eksitui\n```\n\n---\n\n> _**ekşi sözlük** is a collaborative hypertext dictionary based on the concept of Web sites built up on user contribution. It is currently one of the largest online communities in Turkey._\n\n> _As an online public sphere, ekşi sözlük is not only utilized by thousands for information sharing on various topics ranging from scientific subjects to everyday life issues, but also used as a virtual socio-political community to communicate disputed political contents and to share personal views. -[wiki](https://en.wikipedia.org/wiki/Ek%C5%9Fi_S%C3%B6zl%C3%BCk)_\n\n## Usage\n\n```python\n$ eksi\n# or\n$ eksi <topic>\n# directly starts the application with given topic\n```\n\n![ss2](https://user-images.githubusercontent.com/16024979/203432272-dfa799ac-e3d4-4320-85a2-1bb6855cf843.png)\n\n### Shortcuts:\n\n```\n      T: Dark/Light Theme\n Ctrl+S: Saves the Screenshot in app\'s folder\n      F: Focus Search Input\n Ctrl+X: Clear Search Input\n      Q: Previous Page\n      W: Next Page\n Ctrl+O: Hide/Show Footer Bar\n Ctrl+Q: Quit\n```\n\n## Dev\n\n```\n$ pip install "textual[dev]"\n$ textual console\n$ poetry run textual run --dev eksitui.main:EksiTUIApp\n```\n\n### Dependencies\n\n- [textual](https://pypi.org/project/textual/)\n- [requests](https://pypi.org/project/requests/)\n\n### Thanks to:\n\n- [Ekşisözlük Unofficial API](https://github.com/e4c6/eksi_unofficial_api) by [e4c6](https://github.com/e4c6)\n',
    'author': 'Gökçe',
    'author_email': 'agmmnn@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/agmmnn/eksitui',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
