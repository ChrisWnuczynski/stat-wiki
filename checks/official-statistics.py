"""Checks for official-statistics."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "official-statistics"
md = (root / "research/content" / f"{slug}.md").read_text(encoding="utf-8")
works = json.loads((root / "bibliography.json").read_text(encoding="utf-8"))["works"]
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", md)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
for key in set(cites):
    assert key in works, key
assert "**Your turn.**" not in md
assert "## Check yourself" not in md
assert "not a claim" not in md
heads = re.findall(r"^## (.+)$", md, re.M)
assert heads == [
    "Lead context",
    "Definition",
    "Properties",
    "History",
    "Connections",
]
assert len(md.split()) >= 1000
print(slug, "ok")
