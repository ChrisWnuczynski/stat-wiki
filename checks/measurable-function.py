"""Checks for measurable-function."""
import json
import re
from fractions import Fraction as F
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "measurable-function"
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
    "Definition",
    "Properties",
    "Statistical use",
    "Worked example",
    "Common misconceptions",
    "History",
    "Connections",
]
assert "**Your turn.**" in prose
assert 'collapse="true" title="Answer"' in prose
hidden = re.findall(r'title="Answer"\}(.*?)\n:+', prose, flags=re.S)
assert hidden
for block in hidden:
    assert "{cite:" not in block
assert 2 * F(1, 3) + 7 * F(2, 3) == F(16, 3)
assert 5 * F(1, 3) + 7 * F(2, 3) == F(19, 3)
print(slug, "ok")
