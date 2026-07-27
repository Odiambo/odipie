"""Lazy-loading helpers for optional AI/ML dependencies."""

from __future__ import annotations

import importlib
import importlib.metadata
import inspect
import warnings
from dataclasses import dataclass
from typing import Any

_LAZY_MODULES = {
    "tensorflow": "tensorflow",
    "torch": "torch",
    "sklearn": "sklearn",
    "transformers": "transformers",
    "numpy": "numpy",
    "pandas": "pandas",
    "matplotlib": "matplotlib",
    "plt": "matplotlib.pyplot",
    "cv2": "cv2",
}

_DISTRIBUTIONS = {
    "tensorflow": "tensorflow",
    "torch": "torch",
    "sklearn": "scikit-learn",
    "transformers": "transformers",
    "numpy": "numpy",
    "pandas": "pandas",
    "matplotlib": "matplotlib",
    "plt": "matplotlib",
    "cv2": "opencv-python",
}

_module_cache: dict[str, Any] = {}
_accessed_modules: set[str] = set()


@dataclass
class LazyLoader:
    """Proxy that imports a module on first attribute access."""

    module_name: str
    import_path: str
    _module: Any = None

    def _load_module(self) -> Any:
        if self._module is None:
            try:
                self._module = importlib.import_module(self.import_path)
            except ImportError as exc:
                raise ImportError(
                    f"Failed to lazy load {self.module_name}: {exc}. "
                    f"Install the optional dependency for {self.import_path}."
                ) from exc
            _module_cache[self.module_name] = self._module
            _accessed_modules.add(self.module_name)
        return self._module

    def __getattr__(self, name: str) -> Any:
        return getattr(self._load_module(), name)

    def __dir__(self) -> list[str]:
        try:
            return dir(self._load_module())
        except ImportError:
            return []

    def __repr__(self) -> str:
        state = "loaded" if self._module is not None else "pending"
        return f"<LazyLoader {self.module_name!r} ({state})>"


def __getattr__(name: str) -> Any:
    if name in _LAZY_MODULES:
        module_or_loader = _module_cache.get(name)
        if module_or_loader is None:
            module_or_loader = LazyLoader(name, _LAZY_MODULES[name])
            _module_cache[name] = module_or_loader
        return module_or_loader

    if name == "load_model":
        return load_model
    if name == "preprocess_data":
        return preprocess_data
    if name == "train_model":
        return train_model

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(
        list(globals())
        + list(_LAZY_MODULES)
        + ["load_model", "preprocess_data", "train_model"]
    )


def load_model(model_path: str, framework: str = "auto", *, trusted: bool = False) -> Any:
    """Load a TensorFlow or PyTorch model when the selected framework is needed."""
    if framework == "auto":
        if model_path.endswith((".h5", ".keras")):
            framework = "tensorflow"
        elif model_path.endswith((".pth", ".pt")):
            framework = "torch"
        else:
            raise ValueError("Cannot auto-detect framework. Pass framework explicitly.")

    if framework == "tensorflow":
        tf = __getattr__("tensorflow")
        return tf.keras.models.load_model(model_path)

    if framework == "torch":
        torch = __getattr__("torch")
        load_kwargs: dict[str, Any] = {}
        if "weights_only" in inspect.signature(torch.load).parameters:
            load_kwargs["weights_only"] = not trusted
        elif not trusted:
            warnings.warn(
                "This PyTorch version does not support weights_only=True. "
                "Only load trusted model files.",
                RuntimeWarning,
                stacklevel=2,
            )
        return torch.load(model_path, **load_kwargs)

    raise ValueError(f"Unsupported framework: {framework}")


def preprocess_data(data: Any, method: str = "standard") -> Any:
    """Preprocess tabular data with optional NumPy or scikit-learn imports."""
    if method == "standard":
        __getattr__("sklearn")
        from sklearn.preprocessing import StandardScaler

        return StandardScaler().fit_transform(data)

    if method == "normalize":
        numpy = __getattr__("numpy")
        array = numpy.asarray(data, dtype=float)
        norms = numpy.linalg.norm(array, axis=1, keepdims=True)
        return numpy.divide(array, norms, out=numpy.zeros_like(array), where=norms != 0)

    raise ValueError(f"Unknown preprocessing method: {method}")


def train_model(X: Any, y: Any, model_type: str = "random_forest") -> Any:
    """Train a small demonstration model with lazy framework imports."""
    if model_type == "random_forest":
        __getattr__("sklearn")
        from sklearn.ensemble import RandomForestClassifier

        return RandomForestClassifier().fit(X, y)

    if model_type == "neural_network":
        tensorflow = __getattr__("tensorflow")
        model = tensorflow.keras.Sequential(
            [
                tensorflow.keras.layers.Dense(64, activation="relu"),
                tensorflow.keras.layers.Dense(32, activation="relu"),
                tensorflow.keras.layers.Dense(1, activation="sigmoid"),
            ]
        )
        model.compile(optimizer="adam", loss="binary_crossentropy")
        return model.fit(X, y)

    raise ValueError(f"Unknown model type: {model_type}")


def get_loaded_modules() -> list[str]:
    """Return modules that have been imported through an Odipie lazy proxy."""
    return sorted(_accessed_modules)


def force_load_all() -> dict[str, str]:
    """Import every configured lazy module and return a status map."""
    statuses: dict[str, str] = {}
    for module_name in _LAZY_MODULES:
        try:
            module_or_loader = __getattr__(module_name)
            if isinstance(module_or_loader, LazyLoader):
                module_or_loader._load_module()
            statuses[module_name] = "loaded"
        except ImportError as exc:
            statuses[module_name] = f"not installed: {exc}"
    return statuses


def check_versions() -> dict[str, str]:
    """Return installed package versions without importing heavy modules."""
    versions: dict[str, str] = {}
    for module_name, distribution in _DISTRIBUTIONS.items():
        try:
            versions[module_name] = importlib.metadata.version(distribution)
        except importlib.metadata.PackageNotFoundError:
            versions[module_name] = "not installed"
    return versions


__all__ = [
    "LazyLoader",
    "check_versions",
    "force_load_all",
    "get_loaded_modules",
    "load_model",
    "preprocess_data",
    "train_model",
]
