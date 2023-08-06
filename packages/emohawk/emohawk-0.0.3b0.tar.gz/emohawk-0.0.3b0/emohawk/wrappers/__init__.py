# (C) Copyright 2022 ECMWF.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.


import os
import warnings
from importlib import import_module

from emohawk import Data

_HELPERS = {}


def _wrappers():
    if not _HELPERS:
        here = os.path.dirname(__file__)
        for path in os.listdir(here):
            if path.endswith(".py") and path[0] not in ("_", "."):
                name, _ = os.path.splitext(path)
                try:
                    _HELPERS[name] = import_module(f".{name}", package=__name__).wrapper
                except Exception as e:
                    warnings.warn(f"Error loading wrapper '{name}': {e}")
    return _HELPERS


def get_wrapper(data, *args, **kwargs):
    """Returns an object that wraps classes from other packages to support."""
    if isinstance(data, Data):
        return data

    for name, h in _wrappers().items():
        wrapper = h(data, *args, **kwargs)
        if wrapper is not None:
            return wrapper.mutate()

    fullname = ".".join([data.__class__.__module__, data.__class__.__qualname__])

    raise ValueError(f"Cannot find a wrapper for class {fullname}")
