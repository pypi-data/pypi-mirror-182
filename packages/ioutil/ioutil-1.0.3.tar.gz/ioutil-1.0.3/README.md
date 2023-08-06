# IOutil

[![PyPI](https://img.shields.io/pypi/v/ioutil)](https://pypi.python.org/pypi/ioutil)
[![Pypi - License](https://img.shields.io/github/license/codesrg/ioutil)](https://github.com/codesrg/ioutil/blob/main/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ioutil?color=red)](https://pypi.python.org/pypi/ioutil)

To read and write files.

csv, json, parquet, text, toml formats is supported.

## Installation

`pip install -U ioutil`

## Usage

```
usage: ioutil [options]

optional arguments:
  -h, --help      show this help message and exit
  -v, --version   show version number and exit.

to read/write files:
  path            path to read/write
  -r, --read      to read file
  -w, --write     to write file
  -d, --data      data to write
  -f, --format    file format to use
  -m, --mode      mode to open file
  --rfv           will return formatted string (CSV only)

-w/--write function may return error as it expects data in specific datatype.
Writing files using commandline isn't recommended.
```

### Python Script

To read/write csv file.

```python
from ioutil import csv

data = [['a', 'b'], [1, 2], [3, 4]]
path = '.../file.csv'
csv.write(data=data, path=path)  # to write csv
csv.read(path=path)  # to read csv
```

```python
from ioutil import File

data = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
path = '.../file.csv'

File.write(data=data, path=path)  # to write file
File.read(path=path)  # to read file
```

### Command Line (not recommended)

To write a text file.

```
$ ioutil ".../file.txt" --data "data" --write
True
```

###

To read a json file.

```
$ ioutil ".../file.json" --read
### content of a file ###
```

## Issues:

If you encounter any problems, please file an [issue](https://github.com/codesrg/ioutil/issues) along with a detailed
description.