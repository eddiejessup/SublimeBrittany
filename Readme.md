Brittany Sublime Text 3 Package
=================================

Use brittany to format a document or selection(s) containing Haskell source code, using [Brittany](https://github.com/lspitzner/brittany).

Install
-------

### Package Control
- See [here](http://wbond.net/sublime_packages/package_control) for instructions on installation of Package Control
- In Sublime Text, search for package 'Brittany'

### Manual
Clone this repository into `Sublime Text 3/Packages` using OS-appropriate location:

OSX:

    git clone git://github.com/eddiejessup/Brittany.git ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/Brittany

Windows:

    git clone git://github.com/eddiejessup/Brittany.git "%APPDATA%\Sublime Text 3\Packages\Brittany"

Linux:

    git clone git://github.com/eddiejessup/Brittany.git ~/.config/sublime-text-3/Packages/Brittany

Usage
-----
Access commands via:

- Right-click menu item `Brittany`
- Menu item `Tools -> Brittany`
- Default keyboard shortcuts:
  - Format: `⌘+k, b` (OSX) or `ctrl+k, b` (Linux and Windows)

The commands work on a selection, multiple selections or if nothing is selected, the whole document.

Requirements
------------
The command `brittany` should be available on the path.

Author & Contributors
---------------------
- [Elliot Marsden](https://github.com/eddiejessup)

License
-------
MIT License
