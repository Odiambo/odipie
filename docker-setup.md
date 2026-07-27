# Docker Setup

This guide documents the Docker workflow that exists in this repository. The image installs Odipie from `pyproject.toml` and runs the lightweight smoke-check app without importing heavy optional ML frameworks.

## Project Tree

```text
odipie/
├── odipie/
│   ├── __init__.py
│   └── __main__.py
├── docker/
│   ├── Dockerfile
│   ├── .dockerignore
│   ├── entrypoint.sh
│   └── README.md
├── .dockerignore
├── app.py
├── config.py
├── docker-compose.yml
├── lazy_init_py.py
├── pyproject.toml
└── requirements.txt
```

## Dockerfile

```dockerfile
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml README.md requirements.txt ./
COPY odipie ./odipie
COPY docker ./docker
COPY ROProj ./ROProj
COPY lazy_init_py.py app.py config.py ./

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY docs ./docs

ENTRYPOINT ["sh", "docker/entrypoint.sh"]
CMD ["python", "app.py"]
```

## Root `.dockerignore`

```text
.git
.github
__pycache__/
*.py[cod]
.pytest_cache/
.ruff_cache/
.venv/
venv/
build/
dist/
*.egg-info/
notebooks/
data/
```

## Docker Compose

```yaml
services:
  odipie:
    build:
      context: .
      dockerfile: docker/Dockerfile
    command: python app.py
```

## Build and Run

From the repository root:

```bash
docker compose build
docker compose up
```

The default container runs `python app.py`, which verifies that Odipie imports and prints optional dependency availability.

## Optional ML Dependencies

The base image installs `-e .` from `requirements.txt`. To bake in a heavier stack, update `requirements.txt` before building:

```text
-e .[data]
# or
-e .[tensorflow]
# or
-e .[torch]
```

Keep optional AI/ML dependencies explicit so the lazy-loading workflow does not turn into an oversized default install.
