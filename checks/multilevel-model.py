"""Checks for the multilevel model page."""

import json
import re
from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "multilevel-model"
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

tau2, sigma2 = 9, 3
assert tau2 + sigma2 == 12
assert Fraction(tau2, tau2 + sigma2) == Fraction(3, 4)
assert sigma2 + sigma2 == 6
assert (tau2 + sigma2) + (tau2 + sigma2) == 24
assert 24 / 6 == 4
tau2, sigma2 = 4, 12
assert tau2 + sigma2 == 16
assert Fraction(tau2, tau2 + sigma2) == Fraction(1, 4)
assert sigma2 + sigma2 == 24
print(slug, "ok")
