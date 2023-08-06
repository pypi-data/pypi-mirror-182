# Themizer
> An easy and fast CLI app to change between custom themes in Unix-like systems

## Installation
```bash
> pip install themizer # Install with pip
> themizer -v # Check if themizer has been installed correctly
```

## Usage
**Create a theme:**
```bash
> themizer create foo # foo is the name of the theme to create
```

**Apply a theme:**
```bash
> themizer apply bar
```

**Apply the last used theme:**
```bash
> themizer apply # When you not specify the theme to use themizer will try to use the last applied theme
```

**Delete a theme:**
```bash
> themizer delete baz
```
> Note: you can use quotes for themes with spaces in its name. E.g. `themizer apply 'Space Plumber'`


## Creating a theme
If you create a theme and apply it directly it will raise this error:
```
[ ERROR ] The theme config body is empty
```
This happens because you should configure your theme manually, this little guide will help you in the process of create a new one.  

### Theme structure

All the themes are saved in `~/.config/themizer/themes/` by default, and the structure of a theme looks like this:
```
'theme-name/'
 ├── after-execute
 ├── before-execute
 ├── theme.config
 └── ...
```

| Directory / File | Description |
| --- | --- |
| `theme.config` | Here is stored all info about the theme and the instructions to apply it, more info below. |
| `before-execute` | This file will be execute before Themizer actually moves the themes and applies it. Use its shebang to execute anything you want. |
| `after-execute` | The same as `before-execute` but after the theme is actually applied. |

### Configuration of the theme
The `theme.config` is spliced in two parts, the header and the body.


#### The header:
The header stores optional information about the theme itself (in this case a custom name for it) and the body what directories should move from the theme and where they should go. Looking like this:
```toml
[theme] # Header of the theme config
name = 'custom_name' # The default name is the name of the directory
```

#### The body:
The body is former for the relative path of the config to move `theme-name/super-config` and the destination `~/.config/super-app`. Looking like this:
```toml
['super-config'] # Relative directory from the theme path
dest = '~/.config/super-app' # Absolute path (can use ~to refer the home path)
```
#### Example:
Directory structure:
```bash
foo-theme/
 ├── after-execute
 ├── before-execute
 ├── theme.config
 ├── fish/... # Some config for fish shell
 └── htop/... # Some config for htop
```
Configuration file:
```toml
[theme]
name = 'Kanagawa Theme'

['fish']
dest = '~/.config/fish'

['htop']
dest = '~/.htop'
```

When you run `themizer apply 'Kanagawa Theme'` themizer will execute `before-script`, copy `foo-theme/fish/` to `~/.config/fish/`, copy `foo-theme/htop/` to `~/.htop/` and finally execute `after-script`.

> Note: As you can assume the subdirectory `theme` will not work correctly as its name is used to refer the header of the configuration.'

## Configuration
Your configuration directory is located by default in `~/.config/themizer/`.

### Custom config path
You can use your custom path for the config using `--config`:
```
> themizer --config /path/to/config/directory
```

## Contributing
Feel free to report a bug or request a branch merge, I appreciate any contribution.

## Author

Created with :heart: by [Kutu](https://kutu-dev.github.io/).
> - GitHub - [kutu-dev](https://github.com/kutu-dev)
> - Twitter - [@kutu_dev](https://twitter.com/kutu_dev)
