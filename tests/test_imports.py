from __future__ import annotations

import odipie
import lazy_init_py


def test_lazy_access_returns_proxy_without_importing_module() -> None:
    tensorflow_proxy = odipie.tensorflow

    assert isinstance(tensorflow_proxy, odipie.LazyLoader)
    assert "tensorflow" not in odipie.get_loaded_modules()


def test_version_check_does_not_force_lazy_imports() -> None:
    odipie.check_versions()

    assert "tensorflow" not in odipie.get_loaded_modules()


def test_legacy_lazy_init_py_shim_uses_package_runtime() -> None:
    assert lazy_init_py.get_loaded_modules() == odipie.get_loaded_modules()
