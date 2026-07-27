# Docker

Build from the repository root:

```bash
docker compose build
docker compose up
```

The default container runs `python app.py`, which verifies the package install and prints optional dependency availability without importing heavy ML libraries.
