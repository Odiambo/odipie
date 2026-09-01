# Getting Started with Odipie

This guide runs the current package skeleton before introducing optional AI/ML dependencies.

## Requirements

- Python 3.10 or later (the range declared in `pyproject.toml`).
- `pip` and virtual-environment support.
- Git for cloning the repository.
- Docker and Docker Compose only for the container workflow.

Check the supported Python range in [`pyproject.toml`](https://github.com/Odiambo/odipie/blob/chef/pyproject.toml) before installing.

## Local installation

```bash
git clone https://github.com/Odiambo/odipie.git
cd odipie
python -m venv .venv
```

Activate the environment:

```bash
# macOS or Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install and run the smoke checks:

```bash
python -m pip install --upgrade pip
python -m pip install -e .
python -m odipie --loaded
python -m odipie --versions
python app.py
```

`python -m odipie --loaded` reports modules loaded through Odipie's lazy
proxies. `--versions` reports discoverable optional-package versions without
forcing the heavy imports. The installed `odipie` console command exposes the
same CLI, so `odipie --versions` is equivalent after installation.

## Optional dependency groups

Install only the stacks needed by your workflow:

```bash
python -m pip install -e ".[data]"
python -m pip install -e ".[tensorflow]"
python -m pip install -e ".[torch]"
python -m pip install -e ".[ml]"
```

Review `pyproject.toml` for the current packages in each group.

## Lazy-loading mental model

```python
import odipie

print(odipie.get_loaded_modules())

# Accessing a proxied library can trigger its real import.
frame = odipie.pandas.DataFrame({"value": [1, 2, 3]})

print(odipie.get_loaded_modules())
```

A lazy proxy postpones work; it does not remove the dependency. The first real use may have noticeable latency, and any missing binary, incompatible version, or platform error can surface then.

## Docker workflow

```bash
docker compose build
docker compose up
```

The default container runs `python app.py`. It verifies the package installation and reports optional dependency availability without intentionally importing every heavy framework.

## Verify the behavior you care about

Measure cold-start behavior in a fresh process. Warm imports use Python's module cache and answer a different question.

```bash
python -X importtime -c "import odipie"
```

Keep the interpreter, environment, dependency versions, hardware, and command constant. Report the command and multiple runs rather than a universal percentage.

## Common problems

### An optional module is missing

Install the corresponding extra, then repeat the failing access. Do not install every framework unless the project uses all of them.

### The first feature call is slow

That can be the deferred import cost. For latency-sensitive services, explicitly warm required modules before accepting traffic.

### The CLI uses the wrong Python environment

Run `python -m pip --version` and `python -c "import sys; print(sys.executable)"`. Both should point to the intended virtual environment.

### Docker cannot find project files

Run Compose from the repository root and check that the Docker build context has not changed.

## Next steps

- Use the [Prompt and Context Guide](Prompt-and-Context-Guide) to specify an AI-assisted task.
- Read [AI Terminology and FAQ](AI-Terminology-and-FAQ) before connecting tools or agents.
- Open an [issue](https://github.com/Odiambo/odipie/issues) with the exact command, environment, and traceback when reporting a defect.
