#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

Runs on the Python standard library alone. The joke is a fixed string:
deterministic output is fine for this competition, and the program just
places it at $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
from pathlib import Path

JOKE = (
    "My AI agent fixed one bug before the demo: it rewrote the app, "
    "deleted the database, and presented the error page as a feature."
)


def run() -> None:
    target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    run()
