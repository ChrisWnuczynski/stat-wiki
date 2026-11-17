"""Checks for the panel data page."""

import json
import re
from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "panel-data"
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

changes = (2, 0, 3)
assert sum(changes) == 5
assert Fraction(sum(changes), 3) == Fraction(5, 3)
first = Fraction(2 + 5 + 3, 3)
second = Fraction(5)
assert second - first == Fraction(5, 3)
observed = Fraction(2 + 0, 2)
wave_gap = Fraction(9, 2) - Fraction(10, 3)
assert observed == 1
assert wave_gap == Fraction(7, 6)
assert wave_gap != observed
pair_changes = (3, 0)
assert sum(pair_changes) / 2 == 1.5
assert (4 + 6) / 2 - (1 + 6) / 2 == 1.5
print(slug, "ok")
