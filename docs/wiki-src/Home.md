# Odipie Wiki

Odipie is a lightweight Python toolkit and project template for AI/ML work that can defer optional, heavy imports until a feature uses them. This wiki covers the runnable repository and the practical AI concepts needed to use agentic tools responsibly.

## Who this wiki is for

- Python developers trying the Odipie lazy-loading package.
- AI/ML practitioners who want a small, inspectable project skeleton.
- New agentic-tool users who need precise definitions without marketing shorthand.
- Teams designing tool-using or multi-agent workflows with explicit safety boundaries.

## Choose a reading path

### I want to run Odipie

1. [Getting Started](Getting-Started)
2. [Prompt and Context Guide](Prompt-and-Context-Guide)
3. [Automatic Prompt Engineering](Automatic-Prompt-Engineering)

### I want to understand modern AI systems

1. [AI Terminology and FAQ](AI-Terminology-and-FAQ)
2. [Agents, MCP, and Orchestration](Agents-MCP-and-Orchestration)
3. [AI Claims and Misconceptions](AI-Claims-and-Misconceptions)
4. [AI Bias Recognition & Mitigation](AI-Bias-Recognition-&-Mitigation)

## Repository at a glance

```text
odipie/
├── odipie/                 # Installable package
├── ROProj/                 # Small starter scaffold
├── docker/                 # Container files
├── docs/wiki-src/          # Source of truth for this wiki
├── tests/                  # Import smoke tests
├── app.py                  # Local/container smoke check
├── docker-compose.yml
├── lazy_init_py.py         # Compatibility import surface
├── pyproject.toml
└── requirements.txt
```

The package exposes lazy proxies for optional libraries. Importing Odipie does not prove that every optional framework is installed, compatible, or usable. Accessing an optional dependency is the point at which its import can occur and fail.

## What Odipie does—and does not do

Odipie can reduce initial import work in applications that expose several optional AI/ML stacks. The actual benefit depends on the Python version, platform, installed libraries, import path, and workload. Measure startup time and memory in your environment before making a performance claim.

Odipie is not a model, an agent framework, an MCP implementation, or a substitute for dependency, security, and model evaluation. The educational agent material in this wiki is guidance for system design.

## Documentation principles

- Prefer runnable examples over implied guarantees.
- Distinguish a base model from the software system around it.
- Use deterministic code for calculations, validation, policy enforcement, and irreversible actions where practical.
- Give agents the minimum tools and permissions required for a task.
- Evaluate outputs against explicit acceptance criteria.

## Project links

- [Public repository](https://github.com/Odiambo/odipie)
- [Issue tracker](https://github.com/Odiambo/odipie/issues)
- [Apache License 2.0](https://github.com/Odiambo/odipie/blob/chef/LICENSE)

Continue with [Getting Started](Getting-Started) or begin with [AI Terminology and FAQ](AI-Terminology-and-FAQ).
