"""Checks for misuse-of-statistics."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "misuse-of-statistics"
md = (root / "research/content" / f"{slug}.md").read_text(encoding="utf-8")
works = json.loads((root / "bibliography.json").read_text(encoding="utf-8"))["works"]
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", md)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
for key in set(cites):
    assert key in works, key
assert "**Your turn.**" not in md
assert "## Check yourself" not in md
heads = re.findall(r"^## (.+)$", md, re.M)
assert heads == [
    "Lead context",
    "Definition",
    "Statistical use",
    "Common misconceptions",
    "Connections",
    "History",
]
assert len(md.split()) >= 1000
alpha = 0.05
power = 0.8
R = 1
ppv = (power * R) / (R - (1 - power) * R + alpha)
assert abs(ppv - (0.8 / (0.8 + 0.05))) < 1e-12
print(slug, "ok")
