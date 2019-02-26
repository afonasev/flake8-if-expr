# flake8-if-expr

[![pypi](https://badge.fury.io/py/flake8-if-expr.svg)](https://pypi.org/project/flake8-if-expr)
[![Python: 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://pypi.org/project/flake8-if-expr)
[![Downloads](https://img.shields.io/pypi/dm/flake8-if-expr.svg)](https://pypistats.org/packages/flake8-if-expr)
[![Build Status](https://travis-ci.org/Afonasev/flake8-if-expr.svg?branch=master)](https://travis-ci.org/Afonasev/flake8-if-expr)
[![Code coverage](https://codecov.io/gh/afonasev/flake8-if-expr/branch/master/graph/badge.svg)](https://codecov.io/gh/afonasev/flake8-if-expr)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://en.wikipedia.org/wiki/MIT_License)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Check for if expression (ternary operator).

This module provides a plugin for flake8, the Python code checker.

## Installation

```bash
pip install flake8-if-expr
```

## Example

```python
# code.py
x = 1 if 2 else 3
```

```bash
$ flake8 code.py
./code.py:1:5: KEK100 don`t use "[on_true] if [expression] else [on_false]" syntax
x = 1 if 2 else 3
    ^
```

## License

MIT

## Change Log

### 0.2.1 - 2019.02.26

* update flake8-plugin-utils version

### 0.2.0 - 2019.02.09

* Rewriting with flake8-plugin-utils

### 0.1.1 - 2019.02.08

* Remove pycodestyle from dependencies
* KEK101 error code [#2](https://github.com/Afonasev/flake8-if-expr/pull/2)

### 0.1.0 - 2019.02.07

* First release
