"""Minimal runnable smoke check for the Odipie package."""

from __future__ import annotations

import json

import odipie


def main() -> None:
    print("Odipie is installed and ready.")
    print(json.dumps({"loaded_modules": odipie.get_loaded_modules()}, indent=2))
    print("Optional dependency versions:")
    print(json.dumps(odipie.check_versions(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
