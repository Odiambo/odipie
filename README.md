<div align="center">

# Odipie
### Fast AI/ML Workflows Through Intelligent Lazy Loading

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-Apache%202.0-brightgreen.svg)](LICENSE)
[![Template](https://img.shields.io/badge/repo-template-blueviolet)](https://github.com/Odiambo/odipie/generate)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)

Reduce startup cost by loading heavy AI/ML libraries only when a code path actually uses them.

</div>

Odipie is a lightweight Python toolkit and project template for lazy-loading optional AI/ML dependencies. The base install stays small. Frameworks such as TensorFlow, PyTorch, scikit-learn, Transformers, Pandas, NumPy, Matplotlib, and OpenCV can be installed as optional extras.

## Features

- Lazy proxy objects for common AI/ML libraries.
- Optional dependency extras instead of one oversized required install.
- Compatibility shim for older examples that use `import lazy_init_py as odipie`.
- Small CLI and smoke-check app for verifying the package install.
- Docker and Compose workflow that builds from the real repository tree.
- Wiki source files under `docs/wiki-src/` for longer engineering notes.

## Project Tree

```text
odipie/
├── odipie/
│   ├── __init__.py
│   └── __main__.py
├── ROProj/
│   ├── README.md
│   ├── app.py
│   ├── config.py
│   ├── docker-compose.yml
│   └── requirements.txt
├── docker/
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── entrypoint.sh
│   └── README.md
├── docs/
│   └── wiki-src/
├── tests/
│   └── test_imports.py
├── .dockerignore
├── app.py
├── config.py
├── docker-compose.yml
├── lazy_init_py.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Installation

Create and activate a virtual environment, then install the package in editable mode:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .
```

Install optional stacks only when you need them:

```bash
pip install -e .[data]
pip install -e .[tensorflow]
pip install -e .[torch]
pip install -e .[ml]
```

## Usage

```python
import odipie

print("App ready")
print(odipie.get_loaded_modules())

# TensorFlow imports only when this attribute chain is used.
model = odipie.tensorflow.keras.Sequential([...])

# scikit-learn imports only when this code path runs.
processed = odipie.preprocess_data(data, method="standard")
```

Older examples still work:

```python
import lazy_init_py as odipie
```

## CLI Smoke Checks

```bash
python -m odipie --loaded
python -m odipie --versions
python app.py
```

## Tests

```bash
pip install -e .[dev]
pytest
```

## Docker

```bash
docker compose build
docker compose up
```

See [docker-setup.md](docker-setup.md) for the Docker walkthrough.

## Documentation

| Resource | Description | Link |
|----------|-------------|------|
| Wiki Home | Complete knowledge base | [Wiki](https://github.com/Odiambo/odipie/wiki) |
| Docker Guide | Build and run the package in Docker | [docker-setup.md](docker-setup.md) |
| Lazy Loading Deep Dive | Lazy-loading concepts and implementation notes | [docs/wiki-src/Guide_LzyL-AI.md](docs/wiki-src/Guide_LzyL-AI.md) |
| Prompt Engineering | Prompt ideation and context engineering | [adv_promptGuide.md](adv_promptGuide.md) |
| Wiki Sources | Source markdown for wiki pages | [docs/wiki-src](docs/wiki-src) |

## Security Note

Do not use wildcard imports in project code. For PyTorch model files, only load artifacts from trusted sources; Odipie uses safer `torch.load(..., weights_only=True)` defaults when supported by the installed PyTorch version.

## License

This project is licensed under the [Apache License 2.0](LICENSE).
