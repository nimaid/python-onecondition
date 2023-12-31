# 1️⃣ OneCondition
### An ultra-lightweight package for validating single conditions in Python.
[![Python Version](https://img.shields.io/pypi/pyversions/onecondition?logo=python&logoColor=white)](https://pypi.org/project/onecondition/)
[![PyPI Version](https://img.shields.io/pypi/v/onecondition)](https://pypi.org/project/onecondition/)
[![GitHub Build](https://img.shields.io/github/actions/workflow/status/nimaid/python-onecondition/publish-pypi-release.yml?logo=GitHub)](https://github.com/nimaid/python-onecondition/actions/workflows/publish-pypi-release.yml)
[![Codecov Coverage](https://codecov.io/gh/nimaid/python-onecondition/graph/badge.svg?token=IG0GJD2GIO)](https://codecov.io/gh/nimaid/python-onecondition)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/6016e7276903495c9d4a6f0dc89d2904)](https://app.codacy.com/gh/nimaid/python-onecondition/dashboard)
[![License](https://img.shields.io/pypi/l/onecondition)](https://github.com/nimaid/python-onecondition/raw/main/LICENSE)
[![PyPI Downloads](https://img.shields.io/pypi/dm/onecondition.svg?label=pypi%20downloads&logo=PyPI&logoColor=white)](https://pypi.org/project/onecondition/)

<p align="center"><a href="https://pypi.org/project/onecondition/"><img src="https://pypi.org/static/images/logo-large.9f732b5f.svg" width="200px" alt="onecondition on Pypi"></a></p>

## Usage
```doctest
>>> import onecondition as oc

>>> def inverse(user_input):
...     oc.validate.instance(user_input, (int, float))
...     oc.validate.positive(user_input)
...     return 1 / user_input

>>> inverse(4)
0.25
>>> inverse(0)
Traceback (most recent call last):
    ...
onecondition.ValidationError: Value `0` must be positive (non-zero)
>>> inverse("foobar")
Traceback (most recent call last):
    ...
onecondition.ValidationError: Value `'foobar'` must be an instance of (<class 'int'>, <class 'float'>), not a <class 'str'>

```

# Full Documentation
<p align="center"><a href="https://onecondition.readthedocs.io/en/latest/index.html"><img src="https://brand-guidelines.readthedocs.org/_images/logo-wordmark-vertical-dark.png" width="300px" alt="onecondition on Read the Docs"></a></p>
