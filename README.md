# Decorate-me

[![Version status](https://img.shields.io/pypi/status/decorateme?label=status)](https://pypi.org/project/decorateme)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python version compatibility](https://img.shields.io/pypi/pyversions/decorateme?label=Python)](https://pypi.org/project/decorateme)
[![Version on Docker Hub](https://img.shields.io/docker/v/dmyersturnbull/decorate-me?color=green&label=Docker%20Hub)](https://hub.docker.com/repository/docker/dmyersturnbull/decorate-me)
[![Version on Github](https://img.shields.io/github/v/release/dmyersturnbull/decorate-me?include_prereleases&label=GitHub)](https://github.com/dmyersturnbull/decorate-me/releases)
[![Version on PyPi](https://img.shields.io/pypi/v/decorateme?label=PyPi)](https://pypi.org/project/decorateme)  
[![Build (Actions)](https://img.shields.io/github/workflow/status/dmyersturnbull/decorate-me/Build%20&%20test?label=Tests)](https://github.com/dmyersturnbull/decorate-me/actions)
[![Documentation status](https://readthedocs.org/projects/decorate-me/badge)](https://decorate-me.readthedocs.io/en/stable)
[![Coverage (coveralls)](https://coveralls.io/repos/github/dmyersturnbull/decorate-me/badge.svg?branch=main&service=github)](https://coveralls.io/github/dmyersturnbull/decorate-me?branch=main)
[![Maintainability (Code Climate)](https://api.codeclimate.com/v1/badges/ce5a27b46cbe0f3c3039/maintainability)](https://codeclimate.com/github/dmyersturnbull/decorate-me/maintainability)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/dmyersturnbull/decorate-me/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/dmyersturnbull/decorate-me/?branch=main)

Python decorators for str/repr, equality, immutability, and more.

Save lines and document your class’s behavior at the top.
Just `pip install decorateme` and `import decorateme`.

Licensed under the [Apache License, version 2.0](https://www.apache.org/licenses/LICENSE-2.0).
[New issues](https://github.com/dmyersturnbull/decorate-me/issues) and pull requests are welcome.
Please refer to the [contributing guide](https://github.com/dmyersturnbull/decorate-me/blob/master/CONTRIBUTING.md).
Generated with [Tyrannosaurus](https://github.com/dmyersturnbull/tyrannosaurus).


### List of decorators

**String-like methods**
- auto_repr_str
- auto_str
- auto_repr
- auto_html (for display in Jupyter)
- auto_info (add a .info method)

**Equality**
- auto_eq
- auto_hash
- total_ordering  (from functools)

**Make your class smart**
- auto_obj (auto- for eq, str, and repr)
- dataclass (from dataclasses)

**Docstring-related**
- copy_docstring
- append_docstring

**Timing**
- takes_seconds
- takes_seconds_named
- auto_timeout

**Allow a class to be used as a type**
- iterable_over
- collection_over
- sequence_over
- float_type
- int_type

**Overriding / inheritance**
- final
- overrides
- override_recommended
- ABC (from abc)
- ABCMeta  (from abc)
- abstractmethod  (from abc)


**Mark purpose / use**
- internal
- external
- reserved

**Multithreading**
- thread_safe
- not_thread_safe

**Mutability**
- mutable
- immutable

**Code maturity**
- status (code deprecation & immaturity warnings)

**Singletons**
- auto_singleton


Example of `auto_obj` and `float_type`:
```python
import decorateme
@decorateme.auto_obj()
@decorateme.float_type('weight')
class Uno:
    def __init__(self, weight):
        self.weight = weight
print()
light1, light2, heavy = Uno(3.1), Uno(3.1), Uno(12.8)
assert light1 == light2 != heavy
print(light1)  # 'Duo(weight=22.3)'
assert light1 * heavy == 39.68
```
