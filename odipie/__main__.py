"""Command line smoke checks for Odipie."""

from __future__ import annotations

import argparse
import json

from . import check_versions, get_loaded_modules


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect the Odipie lazy-loading runtime.")
    parser.add_argument(
        "--versions",
        action="store_true",
        help="Show optional dependency versions without importing heavy modules.",
    )
    parser.add_argument(
        "--loaded",
        action="store_true",
        help="Show modules loaded through Odipie lazy proxies.",
    )
    args = parser.parse_args()

    if args.versions:
        print(json.dumps(check_versions(), indent=2, sort_keys=True))
        return

    print(json.dumps({"loaded_modules": get_loaded_modules()}, indent=2))


if __name__ == "__main__":
    main()
