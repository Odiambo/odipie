# Odipie

This is a Python toolkit designed to optimize AI/ML workflows by leveraging learned and discovered techniques for heavy dependencies. This repository works as a resource for building efficient, modular, and scalable AI/ML applications, with a focus on fast startup times, reduced memory usage, and integration suggestions.

<br>Input is welcomed and greatly encouraged.


## Features

- **Lazy Loading of Heavy Libraries:**  
  Dynamically loads AI/ML libraries (e.g., TensorFlow, PyTorch, scikit-learn, Transformers, NumPy, Pandas, Matplotlib, OpenCV) only when they are actually used, minimizing startup time and memory footprint.

- **Transparent API:**  
  Access libraries and utility functions as if they were eagerly imported, with no change to your code’s interface.

- **Utility Functions:**  
  Includes lazy-loaded helpers for model loading, data preprocessing, and model training.

- **Debugging & Development Tools:**  
  Easily inspect which modules have been loaded and force-load all dependencies for testing or warm-up.

- **Clear Error Handling:**  
  User-friendly messages when optional dependencies are missing.

- **Docker Integration Guide:**  
  Step-by-step instructions for containerizing your AI/ML application using Docker and Docker Compose.


## Usage

### 1. Lazy Loading in Your Project

Import libraries and functions from `lazy_init_py.py` as you would from a normal package:

```python
import lazy_init_py as odipie

# Fast startup!
print("App ready!")

# Libraries load only when accessed:
model = odipie.tensorflow.keras.Sequential([...])  # TensorFlow loads here
rf = odipie.sklearn.ensemble.RandomForestClassifier()  # scikit-learn loads here

# Utility functions (also lazy):
loaded_model = odipie.load_model('model.h5')  # Loads TensorFlow only if needed
processed = odipie.preprocess_data(data)
trained = odipie.train_model(X, y)
```

### 2. Inspect and Control Lazy Loading

```python
# See which modules have been loaded so far
print(odipie.get_loaded_modules())

# Force-load all lazy modules (useful for testing)
odipie.force_load_all()
```

---

## Documentation

- **[Guide_LzyL-AI.md](Guide_LzyL-AI.md):**  
  Comprehensive explanation of lazy loading, its benefits for AI/ML, and technical implementation details.

- **[docker-setup.md](docker-setup.md):**  
  Step-by-step guide for Dockerizing a Flask-based AI/ML project, including best practices for Python environments.

---

## 🐳 Docker Support

See [docker-setup.md](docker-setup.md) for a full walkthrough on building and running your AI/ML app in Docker, including sample `Dockerfile`, `.dockerignore`, and `docker-compose.yml` configurations.

---

## 📄 License

This project is licensed under the [Apache License 2.0](LICENSE).

---

## 🤝 Contributing

Contributions are welcome! Please open issues or submit pull requests to help improve odipie.

---

## Security Note

Never use `import *` in your code or in `__init__.py` files. Always explicitly import only the modules you need. See [docker-setup.md](docker-setup.md) for more security best practices.

---

## Contact

For questions or suggestions, please open an issue in this repository.