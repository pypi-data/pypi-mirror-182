![python version](https://img.shields.io/pypi/pyversions/space-rocks)
![PyPI](https://img.shields.io/pypi/v/space-rocks) [![Documentation Status](https://readthedocs.org/projects/rocks/badge/?version=latest)](https://rocks.readthedocs.io/en/latest/?badge=latest) [![arXiv](https://img.shields.io/badge/arXiv-2209.10697-f9f107.svg)](https://arxiv.org/abs/2209.10697)
 [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

<p align="center">
  <img width="260" src="https://raw.githubusercontent.com/maxmahlke/rocks/master/docs/_static/logo_rocks.svg">
</p>

[Features](#features) - [Install](#install) - [Documentation](#documentation)

*Disclaimer: The SsODNet service and its database are in an alpha version and under constant revision. The provided values and access methods may change without notice.*

## Features

Explore asteroid data on the command-line...

``` sh
$ rocks id 221
(221) Eos

$ rocks class Eos
MB>Outer

$ rocks albedo Eos
0.136 +- 0.004

$ rocks taxonomy Eos
K

$ rocks density Eos
4.559e+03 +- 1.139e+03 kg/m$^3$
```

... and in a `python` script.

``` python
>>> import rocks
>>> rocks.identify("1902ug")
('Fortuna', 19)
>>> ceres = rocks.Rock("ceres")
>>> ceres.diameter.value
848.4
>>> ceres.diameter.unit
'km'
>>> ceres.mass.value
9.384e+20
>>> ceres.mass.error
6.711e+17
```

## Install

Install from PyPi using `pip`:

     $ pip install space-rocks

The minimum required `python` version is 3.7.


## Documentation

Check out the documentation at [rocks.readthedocs.io](https://rocks.readthedocs.io/en/latest/) or run

     $ rocks docs
