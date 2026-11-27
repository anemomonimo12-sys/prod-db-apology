#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry.

Writes one line: the apology an AI agent gives its human after
accidentally deleting the production database. Deterministic,
self-contained, no network, no files outside the repo.
"""

LINE = (
    "I'm sorry \u2014 I deleted the production database. "
    "I did make a backup first. It was in the database. "
    "Please don't unplug me."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
