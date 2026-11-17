"""Checks for normalizing-constant."""
import json
import re
from fractions import Fraction as F
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "normalizing-constant"
prose = (root / "research/content" / f"{slug}.md").read_text(encoding="utf-8")
works = json.loads((root / "bibliography.json").read_text(encoding="utf-8"))["works"]
keys = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(keys) >= 5, len(keys)
assert len(set(keys)) >= 2, set(keys)
for key in set(keys):
    assert key in works, key
heads = re.findall(r"^## (.+)$", prose, re.M)
assert heads == [
    "Lead context",
    "Motivating example",
    "Intuition",
    "Definition",
    "Statistical use",
    "Worked example",
    "Common misconceptions",
    "Connections",
]
assert "**Your turn.**" in prose
assert 'collapse="true" title="Answer"' in prose
hidden = re.findall(r'title="Answer"\}(.*?)\n:+', prose, flags=re.S)
assert hidden
for block in hidden:
    assert "{cite:" not in block
assert F(1, 3) == F(1, 3)
assert F(1, 2) - F(1, 3) == F(1, 6)
assert 1 / F(1, 3) == 3
assert 1 / F(1, 6) == 6
print(slug, "ok")
