"""Compatibility shim for older examples that import ``lazy_init_py``.

New code should prefer ``import odipie`` after installing the package.
"""

from odipie import LazyLoader
from odipie import __dir__ as __dir__
from odipie import __getattr__ as __getattr__
from odipie import check_versions
from odipie import force_load_all
from odipie import get_loaded_modules
from odipie import load_model
from odipie import preprocess_data
from odipie import train_model

__all__ = [
    "LazyLoader",
    "check_versions",
    "force_load_all",
    "get_loaded_modules",
    "load_model",
    "preprocess_data",
    "train_model",
]
