# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['textual_filedrop']

package_data = \
{'': ['*']}

install_requires = \
['rich>=12.6.0,<13.0.0', 'textual>=0.7.0,<0.8.0']

setup_kwargs = {
    'name': 'textual-filedrop',
    'version': '0.2.0',
    'description': 'FileDrop widget for Textual, easily drag and drop files into your terminal apps.',
    'long_description': '![textual-filedrop](https://user-images.githubusercontent.com/16024979/208708722-e550d8ca-22a7-47f0-adf9-16cad570cdfd.png)\n\n# textual-filedrop\n\nAdd filedrop support to your [Textual](https://github.com/textualize/textual/) apps, easily drag and drop files into your terminal apps.\n\n> _Tested in `Windows Terminal` only. Other terminals/operating systems may not be using the [Paste](https://textual.textualize.io/events/paste/) event._\n\n## Install\n\n```\npip install textual-filedrop\n```\n\n## Usage\n\nYou can find more examples [here](./examples).\n\n```py\nfrom textual_filedrop import FileDrop\n```\n\n```py\n# add FileDrop widget to your app\nyield FileDrop(id="filedrop")\n```\n\n```py\n# focus the widget\nself.query_one("#filedrop").focus()\n```\n\n```py\n# when the files are selected/dropped\ndef on_file_drop_selected(self, message: FileDrop.Selected) -> None:\n    path = message.path\n    filepaths = message.filepaths\n    filenames = message.filenames\n    filesobj = message.filesobj\n    print(path, filepaths, filenames, filesobj)\n\n\n# output: path, [filepaths], [filenames], [filesobj]\n```\n\n## Examples\n\n### [subdomain_lister](./examples/subdomain_lister.py)\n\nDrag and drop the subdomain list files and see the results as a tree list.\n\n![subdomain_lister](https://user-images.githubusercontent.com/16024979/208706132-0a33bb21-51b8-441a-aeb9-668dbfcb382c.gif)\n\n### [fullscreen](./examples/fullscreen.py)\n\nFullscreen example, will show the results in the textual console.\n\n### [hidden](./examples/hidden.py)\n\nAs long as focus is on, the FileDrop widget will be active even if it is not visible on the screen.\n\n## Dev\n\n```\npoetry install\n\ntextual console\npoetry run textual run --dev examples/subdomain_lister.py\n```\n',
    'author': 'agmmnn',
    'author_email': 'agmmnn@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.8,<4.0.0',
}


setup(**setup_kwargs)
