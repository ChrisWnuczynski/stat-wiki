"""Checks for the game of chance page."""

import json
import re
from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "game-of-chance"
md = (root / "research/content" / f"{slug}.md").read_text()
pending = json.loads((root / "research/pending" / f"{slug}.json").read_text())

cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", md)
assert len(cites) >= 5
assert len(set(cites)) >= 2
assert set(cites) <= set(pending["cite_keys"])
assert "## Motivating example" in md
assert "## Worked example" in md
assert "**Your turn.**" in md
answer = re.search(
    r'::: \{\.callout-tip collapse="true" title="Answer"\}(.*?):::', md, re.S
)
assert answer
assert "{{cite:" not in answer.group(1)
checks = pending["self_checks"]
assert 2 <= len(checks) <= 3
for item in checks:
    assert "{{cite:" not in item["answer"]

euro = Fraction(-3, 6) + Fraction(1, 1) * Fraction(3, 6) + Fraction(2, 1) * Fraction(2, 6)
assert euro == Fraction(2, 3)
assert sum(range(1, 7)) == 21
assert Fraction(21, 6) == Fraction(7, 2)
assert Fraction(4, 6) == Fraction(2, 3)
coin = Fraction(1, 2) * 3 + Fraction(1, 2) * (-1)
assert coin == 1
assert coin + euro == Fraction(5, 3)
wheel = Fraction(4, 4) + Fraction(-2, 4)
assert wheel == Fraction(1, 2)
print(slug, "ok")
