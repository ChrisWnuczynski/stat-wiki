"""Read bibliography additions staged by isolated research worktrees."""

from __future__ import annotations

import json
from pathlib import Path


def merge_pending_works(root: Path, base: dict[str, dict]) -> dict[str, dict]:
    """Include per-page bibliography entries without editing the shared file."""
    works = dict(base)
    for path in sorted((root / "research" / "pending").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError(f"{path}: pending additions must be an object")
        additions = data.get("bibliography", {})
        if not isinstance(additions, dict):
            raise ValueError(f"{path}: bibliography additions must be a mapping")
        for key, work in additions.items():
            if key in works and works[key] != work:
                raise ValueError(f"{path}: conflicting bibliography entry {key}")
            works[key] = work
    return works
