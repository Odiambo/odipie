# Odipie Wiki

Welcome to the Odipie engineering wiki. Odipie is a lightweight Python toolkit and template for building AI/ML workflows that keep startup fast by lazy-loading optional dependencies only when a feature needs them.

The current runnable workflow is intentionally small:

- `pyproject.toml` defines the installable `odipie` package.
- `requirements.txt` installs the base package in editable mode.
- Optional extras install heavier AI/ML stacks only when needed.
- `app.py` and `python -m odipie` provide smoke checks.
- `docker/Dockerfile` and `docker-compose.yml` build from the real package skeleton.
- `ROProj/` is a starter scaffold for experiments.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .
python -m odipie --loaded
python -m odipie --versions
python app.py
```

Install optional dependencies only for the workflows you use:

```bash
pip install -e .[data]
pip install -e .[tensorflow]
pip install -e .[torch]
pip install -e .[ml]
```

## Docker Workflow

```bash
docker compose build
docker compose up
```

The default container runs `python app.py`. That command verifies the package install and reports optional dependency availability without importing heavy frameworks.

## Project Structure

```text
odipie/
├── odipie/
│   ├── __init__.py
│   └── __main__.py
├── ROProj/
├── docker/
├── docs/wiki-src/
├── tests/
├── app.py
├── docker-compose.yml
├── lazy_init_py.py
├── pyproject.toml
└── requirements.txt
```

## Model-Context-Protocol Overview

Odipie uses Model-Context-Protocol as an organizing pattern for AI development:

- **Model**: The LLM, local model, or ML framework behind an interface.
- **Context**: The runtime inputs, prompt templates, settings, source material, and session metadata needed for a task.
- **Protocol**: The validation, parsing, retry, logging, and tool-use rules that govern how models and context interact.

This separation keeps AI workflows easier to test, document, and evolve.

## Engineering Practices

- [Context Engineering and Modern Prompting Strategies](Context-Engineering-and-Modern-Prompting-Strategies)
- [Inference Engineering](Inference-Engineering)
- [Prompt Design Patterns](Prompt-Design-Patterns)
- [Agent Architecture](Agent-Architecture)
- [Retrieval-Augmented Generation](Retrieval-Augmented-Generation)
- [Evaluation and Observability](Evaluation-and-Observability)
- [AI Security and Prompt Injection](AI-Security-and-Prompt-Injection)

## Software Engineering

- [Development Standards](Development-Standards)

## Architecture

- [System Architecture](System-Architecture)
- [Data Architecture](Data-Architecture)

## Projects

- [Project Overview](Project-Overview)
- [Roadmap](Roadmap)
- [Research and Experiments](Research-and-Experiments)

## Next Documentation Work

1. Add a package/API reference for `odipie.__getattr__`, `LazyLoader`, `load_model`, `preprocess_data`, `train_model`, `check_versions`, and `force_load_all`.
2. Add benchmark scripts and publish reproducible startup/memory numbers.
3. Add dependency support notes for Python versions and optional extras.
4. Add security notes for model loading, prompt injection, and dependency supply chain handling.
