"""Checks for the First International Statistical Congress page."""

import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "first-international-statistical-congress"
md = (root / "research/content" / f"{slug}.md").read_text()
pending = json.loads((root / "research/pending" / f"{slug}.json").read_text())

cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", md)
assert len(cites) >= 5
assert len(set(cites)) >= 2
assert set(cites) <= set(pending["cite_keys"])
for heading in (
    "## Lead context",
    "## Motivating example",
    "## Intuition",
    "## Definition",
    "## Properties",
    "## Statistical use",
    "## Worked example",
    "## Common misconceptions",
    "## Assumptions and limits",
    "## Connections",
    "## History",
):
    assert heading in md
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

assert 240 / 800 == 0.30
assert 150 / 600 == 0.25
assert abs((240 / 800) - (150 / 600) - 0.05) < 1e-12
assert (240 + 150) == 390
assert (800 + 600) == 1400
assert 390 / 1400 == 39 / 140
assert 80 / 200 == 0.4
assert 90 / 300 == 0.3
assert abs((80 / 200) - (90 / 300) - 0.1) < 1e-12
assert (80 + 90) / (200 + 300) == 170 / 500 == 0.34
assert 1876 - 1853 == 23
assert 23 / 8 == 2.875
print(slug, "ok")
