"""Checks for the Lady tasting tea page."""

import json
import re
from math import comb
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "lady-tasting-tea"
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

assert 8 * 7 * 6 * 5 == 1680
assert 4 * 3 * 2 * 1 == 24
assert 1680 // 24 == 70
assert comb(8, 4) == 70
assert comb(4, 3) * comb(4, 1) == 16
assert 16 + 1 == 17
assert comb(6, 3) == 20
assert comb(3, 2) * comb(3, 1) == 9
assert 2 ** 8 == 256
print(slug, "ok")
