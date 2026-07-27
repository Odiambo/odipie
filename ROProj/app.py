"""Starter application using Odipie."""

from __future__ import annotations

import json

import odipie


def main() -> None:
    print("ROProj starter is ready.")
    print(json.dumps({"loaded_modules": odipie.get_loaded_modules()}, indent=2))


if __name__ == "__main__":
    main()
