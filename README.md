# flake8-if-expr

[![pypi](https://badge.fury.io/py/flake8-if-expr.svg)](https://pypi.org/project/flake8-if-expr)
[![Python: 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://pypi.org/project/flake8-if-expr)
[![Downloads](https://img.shields.io/pypi/dm/flake8-if-expr.svg)](https://pypistats.org/packages/flake8-if-expr)
![CI Status](https://github.com/afonasev/flake8-if-expr/workflows/ci/badge.svg?branch=master)
[![Code coverage](https://codecov.io/gh/afonasev/flake8-if-expr/branch/master/graph/badge.svg)](https://codecov.io/gh/afonasev/flake8-if-expr)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://en.wikipedia.org/wiki/MIT_License)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Description

The plugin forbids `if expressions` (ternary operator).

## Installation

```bash
pip install flake8-if-expr
```

## Examples

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
