"""Checks for the cross-sectional data page."""

import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "cross-sectional-data"
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

incomes = (2, 4, 4, 6, 9)
assert sum(incomes) == 25
assert 25 / 5 == 5
devs = tuple(x - 5 for x in incomes)
assert devs == (-3, -1, -1, 1, 4)
assert sum(d * d for d in devs) == 28
assert 28 / 4 == 7
trio = (3, 5, 7)
assert sum(trio) / 3 == 5
assert 7 - 3 == 4
print(slug, "ok")
