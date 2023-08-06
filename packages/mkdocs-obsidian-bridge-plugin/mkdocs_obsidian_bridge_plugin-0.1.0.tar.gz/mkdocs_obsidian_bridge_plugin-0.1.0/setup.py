# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mkdocs_obsidian_bridge_plugin']

package_data = \
{'': ['*']}

install_requires = \
['markdown>=3.2.1,<3.4', 'mkdocs>=1.4.2,<2.0.0']

entry_points = \
{'mkdocs.plugins': ['obsidian-bridge = '
                    'mkdocs_obsidian_bridge_plugin.plugin:ObsidianBridgePlugin']}

setup_kwargs = {
    'name': 'mkdocs-obsidian-bridge-plugin',
    'version': '0.1.0',
    'description': 'An MkDocs plugin that helps exporting your Obsidian vault as an MkDocs site.',
    'long_description': '# Obsidian ➡️ MkDocs Bridge\n\nAn MkDocs plugin that helps exporting your [Obsidian](https://obsidian.md) vault as an MkDocs site.\n\nWIP\n\n<!--\n## Setup\n\nInstall the plugin using pip:\n\n`pip install mkdocs-roamlinks-plugin`\n\nActivate the plugin in `mkdocs.yml`:\n```yaml\nplugins:\n  - search\n  - roamlinks\n```\n\n## Usage\n\nTo use this plugin, simply create a link that only contains the filename of file you wish to link to.\n\n| origin                  | convert                             |\n| ----------------------- | ----------------------------------- |\n| `[Git Flow](git_flow.md)` | `[Git Flow](../software/git_flow.md)` |\n| `[[Git Flow]]`            | `[Git Flow](../software/git_flow.md)` |\n| `[[software/Git Flow]]`   | `[software/Git Flow](../software/git_flow.md)` |\n| `![[image.png]]`           | `![image.png](../image/imag.png)`      |\n| `[[#Heading identifiers]]` | `[Heading identifiers in HTML](#heading-identifiers-in-html)`|\n| `[[Git Flow#Heading]]`     |  `[Git Flow](../software/git_flow.md#heading)` |\n\n\n## TODO\n\n- [ ] convert admonition, for example\n\n[obsidian style admonition](https://help.obsidian.md/How+to/Use+callouts)\n```\n> [!info]\n> something\n```\n\nto [mkdoc material style](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)\n```\n!!! note\n\n    something\n```\n- [ ] `%% comment %%` to HTML comment\n-->\n',
    'author': 'GooRoo',
    'author_email': 'sergey.olendarenko@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
