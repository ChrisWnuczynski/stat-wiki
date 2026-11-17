"""Checks for the statistician page."""

import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "statistician"
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

counts = (120, 80, 200, 100)
assert sum(counts) == 500
assert 500 / 4 == 125
assert 200 / 500 == 0.4
assert 80 / 500 == 0.16
assert 200 - 80 == 120
small = (30, 45, 75)
assert sum(small) == 150
assert 150 / 3 == 50
assert 75 / 150 == 0.5
print(slug, "ok")
