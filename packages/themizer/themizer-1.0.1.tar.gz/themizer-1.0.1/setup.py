# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['themizer']

package_data = \
{'': ['*'], 'themizer': ['.vscode/*']}

install_requires = \
['colorama>=0.4.6,<0.5.0']

entry_points = \
{'console_scripts': ['themizer = themizer.args:process_args']}

setup_kwargs = {
    'name': 'themizer',
    'version': '1.0.1',
    'description': 'An easy and fast CLI app to change between custom themes in Unix-like systems.',
    'long_description': "# Themizer\n> An easy and fast CLI app to change between custom themes in Unix-like systems\n\n## Installation\n```bash\n> pip install themizer # Install with pip\n> themizer -v # Check if themizer has been installed correctly\n```\n\n## Usage\n**Create a theme:**\n```bash\n> themizer create foo # foo is the name of the theme to create\n```\n\n**Apply a theme:**\n```bash\n> themizer apply bar\n```\n\n**Apply the last used theme:**\n```bash\n> themizer apply # When you not specify the theme to use themizer will try to use the last applied theme\n```\n\n**Delete a theme:**\n```bash\n> themizer delete baz\n```\n> Note: you can use quotes for themes with spaces in its name. E.g. `themizer apply 'Space Plumber'`\n\n\n## Creating a theme\nIf you create a theme and apply it directly it will raise this error:\n```\n[ ERROR ] The theme config body is empty\n```\nThis happens because you should configure your theme manually, this little guide will help you in the process of create a new one.  \n\n### Theme structure\n\nAll the themes are saved in `~/.config/themizer/themes/` by default, and the structure of a theme looks like this:\n```\n'theme-name/'\n ├── after-execute\n ├── before-execute\n ├── theme.config\n └── ...\n```\n\n| Directory / File |\xa0Description |\n| --- | --- |\n| `theme.config` | Here is stored all info about the theme and the instructions to apply it, more info below. |\n| `before-execute` | This file will be execute before Themizer actually moves the themes and applies it. Use its shebang to execute anything you want. |\n| `after-execute` | The same as `before-execute` but after the theme is actually applied. |\n\n### Configuration of the theme\nThe `theme.config` is spliced in two parts, the header and the body.\n\n\n#### The header:\nThe header stores optional information about the theme itself (in this case a custom name for it) and the body what directories should move from the theme and where they should go. Looking like this:\n```toml\n[theme] # Header of the theme config\nname = 'custom_name' # The default name is the name of the directory\n```\n\n#### The body:\nThe body is former for the relative path of the config to move `theme-name/super-config` and the destination `~/.config/super-app`. Looking like this:\n```toml\n['super-config'] # Relative directory from the theme path\ndest = '~/.config/super-app' # Absolute path (can use ~to refer the home path)\n```\n#### Example:\nDirectory structure:\n```bash\nfoo-theme/\n ├── after-execute\n ├── before-execute\n ├── theme.config\n ├── fish/... # Some config for fish shell\n └── htop/... # Some config for htop\n```\nConfiguration file:\n```toml\n[theme]\nname = 'Kanagawa Theme'\n\n['fish']\ndest = '~/.config/fish'\n\n['htop']\ndest = '~/.htop'\n```\n\nWhen you run `themizer apply 'Kanagawa Theme'` themizer will execute `before-script`, copy `foo-theme/fish/` to `~/.config/fish/`, copy `foo-theme/htop/` to `~/.htop/` and finally execute `after-script`.\n\n> Note: As you can assume the subdirectory `theme` will not work correctly as its name is used to refer the header of the configuration.'\n\n## Configuration\nYour configuration directory is located by default in `~/.config/themizer/`.\n\n### Custom config path\nYou can use your custom path for the config using `--config`:\n```\n> themizer --config /path/to/config/directory\n```\n\n## Contributing\nFeel free to report a bug or request a branch merge, I appreciate any contribution.\n\n## Author\n\nCreated with :heart: by [Kutu](https://kutu-dev.github.io/).\n> - GitHub - [kutu-dev](https://github.com/kutu-dev)\n> - Twitter - [@kutu_dev](https://twitter.com/kutu_dev)\n",
    'author': 'kutu-dev',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kutu-dev/themizer',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
