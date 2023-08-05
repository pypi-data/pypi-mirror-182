# Bunzbar

## System requirements
+ Linux system where `xsetroot -name {}` as visible. (E.g. Archlinux with Dwm)

## How to get it

+ If you use Archlinux you can get the bunzbar by installing the PKGBUILD file.
+ For other distributions see Manual installation.

## Manual installation

### Get the Python module installed

First of all you need to install the bunzbar python module.
After installing python and pip, use one of the following options to install it.

+  Using pip:
```bash
pip install bunzbar
```
+  From source:
```bash
git clone git@gitlab.com:02742/bunzbar.git
cd bunzbar
pip install build twine
make build
pip install dist/*.whl
```


### Post installation

#### Make the command accessable 

A few options to acceave this

+ Add `~/.local/bin` to your `$PATH` (non persistant)
```bash
export PATH=~/.local/bin:$PATH
```
+ Add it to your `$PATH` using your `.bashrc` file
```bash
echo "export PATH=~/.local/bin:$PATH" >> .bashrc
```
+ Create a link
```bash
ln -s ~/.local/bin/bunzbar /usr/bin/bunzbar
```
+ Get Arch
#### Configuration
```bash
bunzbar
```

#### Start bunzbar in daemon mode
```bash
bunzbar -d
```

## Links

- [gitlab](https://gitlab.com/02742/bunzbar/)
- [pypi](https://pypi.org/project/bunzbar/)
