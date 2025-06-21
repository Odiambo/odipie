"""
Lazy loading __init__.py for AI/ML package with heavy dependencies.
"""

import sys
import importlib
from typing import Any, Dict, Optional
import warnings

# Define which modules should be lazy loaded
_LAZY_MODULES = {
    'tensorflow': 'tensorflow',
    'torch': 'torch', 
    'sklearn': 'sklearn',
    'transformers': 'transformers',
    'numpy': 'numpy',
    'pandas': 'pandas',
    'matplotlib': 'matplotlib.pyplot',
    'cv2': 'cv2'
}

# Cache for loaded modules to avoid repeated imports
_module_cache: Dict[str, Any] = {}

# Track what's been accessed for debugging
_accessed_modules = set()

class LazyLoader:
    """
    A lazy loader that imports modules only when accessed.
    """
    
    def __init__(self, module_name: str, import_path: str):
        self.module_name = module_name
        self.import_path = import_path
        self._module = None
    
    def _load_module(self):
        """Load the actual module if not already loaded."""
        if self._module is None:
            try:
                print(f"Lazy loading {self.module_name}...")
                self._module = importlib.import_module(self.import_path)
                _module_cache[self.module_name] = self._module
                _accessed_modules.add(self.module_name)
            except ImportError as e:
                raise ImportError(
                    f"Failed to lazy load {self.module_name}: {e}. "
                    f"Make sure {self.import_path} is installed."
                ) from e
        return self._module
    
    def __getattr__(self, name: str):
        """Delegate attribute access to the loaded module."""
        module = self._load_module()
        return getattr(module, name)
    
    def __dir__(self):
        """Return available attributes from the loaded module."""
        try:
            module = self._load_module()
            return dir(module)
        except ImportError:
            return []

def __getattr__(name: str) -> Any:
    """
    Module-level __getattr__ for lazy loading.
    Called when an attribute is not found in the module.
    """
    if name in _LAZY_MODULES:
        if name not in _module_cache:
            _module_cache[name] = LazyLoader(name, _LAZY_MODULES[name])
        return _module_cache[name]
    
    # Handle specific lazy-loaded submodules or functions
    elif name == 'load_model':
        return _lazy_load_model
    elif name == 'preprocess_data':
        return _lazy_preprocess_data
    elif name == 'train_model':
        return _lazy_train_model
    
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")

def __dir__():
    """Define what attributes are available in this module."""
    return list(_LAZY_MODULES.keys()) + [
        'load_model', 'preprocess_data', 'train_model',
        'get_loaded_modules', 'force_load_all'
    ]

# Lazy-loaded function implementations
def _lazy_load_model(model_path: str, framework: str = 'auto'):
    """
    Lazy-loaded model loading function.
    Only imports the necessary framework when called.
    """
    if framework == 'auto':
        if model_path.endswith('.h5') or model_path.endswith('.keras'):
            framework = 'tensorflow'
        elif model_path.endswith('.pth') or model_path.endswith('.pt'):
            framework = 'torch'
        else:
            raise ValueError("Cannot auto-detect framework. Please specify.")
    
    if framework == 'tensorflow':
        tf = __getattr__('tensorflow')  # This will lazy load TensorFlow
        return tf.keras.models.load_model(model_path)
    elif framework == 'torch':
        torch = __getattr__('torch')  # This will lazy load PyTorch
        return torch.load(model_path)
    else:
        raise ValueError(f"Unsupported framework: {framework}")

def _lazy_preprocess_data(data, method='standard'):
    """
    Lazy-loaded data preprocessing function.
    """
    if method == 'standard':
        sklearn = __getattr__('sklearn')
        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler()
        return scaler.fit_transform(data)
    elif method == 'normalize':
        numpy = __getattr__('numpy')
        return numpy.linalg.norm(data, axis=1, keepdims=True)
    else:
        raise ValueError(f"Unknown preprocessing method: {method}")

def _lazy_train_model(X, y, model_type='random_forest'):
    """
    Lazy-loaded model training function.
    """
    if model_type == 'random_forest':
        sklearn = __getattr__('sklearn')
        from sklearn.ensemble import RandomForestClassifier
        model = RandomForestClassifier()
        return model.fit(X, y)
    elif model_type == 'neural_network':
        tensorflow = __getattr__('tensorflow')
        model = tensorflow.keras.Sequential([
            tensorflow.keras.layers.Dense(64, activation='relu'),
            tensorflow.keras.layers.Dense(32, activation='relu'),
            tensorflow.keras.layers.Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy')
        return model.fit(X, y)
    else:
        raise ValueError(f"Unknown model type: {model_type}")

# Utility functions
def get_loaded_modules():
    """Return a list of modules that have been lazy loaded."""
    return list(_accessed_modules)

def force_load_all():
    """Force load all lazy modules (useful for warming up)."""
    print("Force loading all lazy modules...")
    for module_name in _LAZY_MODULES:
        try:
            __getattr__(module_name)
            print(f"✓ Loaded {module_name}")
        except ImportError as e:
            print(f"✗ Failed to load {module_name}: {e}")

# Optional: Add version checking for lazy loaded modules
def check_versions():
    """Check versions of lazy-loaded modules."""
    versions = {}
    for module_name in _LAZY_MODULES:
        try:
            module = __getattr__(module_name)
            if hasattr(module, '__version__'):
                versions[module_name] = module.__version__
            else:
                versions[module_name] = "Unknown"
        except ImportError:
            versions[module_name] = "Not installed"
    return versions

# Expose commonly used items directly (these will still be lazy loaded)
# Import example: from mypackage import tensorflow, torch, load_model