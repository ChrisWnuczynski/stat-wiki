"""Checks for the unsupervised-learning research page."""
import json
import re
from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parents[1]
self_checks = json.loads((root / "research/self-checks.json").read_text(encoding="utf-8")).get("unsupervised-learning", [])
prose = (root / "research/content/unsupervised-learning.md").read_text(encoding="utf-8")
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", prose)
assert len(cites) >= 5, cites
assert len(set(cites)) >= 2, set(cites)
assert "**Your turn.**" in prose
assert '::: {.callout-tip collapse="true" title="Answer"}' in prose
answer = re.search(
    r'::: \{\.callout-tip collapse="true" title="Answer"\}(.*?):::',
    prose,
    re.S,
)
assert answer and "{cite:" not in answer.group(1)
checks = self_checks
assert 2 <= len(checks) <= 3
assert all("{cite:" not in item["answer"] for item in checks)

# Points (2,0), (-2,0), (0,1), (0,-1). Sums of squares 8 and 2.
ssx, ssy = 8, 2
assert ssx + ssy == 10
assert Fraction(ssx, 10) == Fraction(4, 5)
assert Fraction(ssy, 10) == Fraction(1, 5)
assert "4/5" in prose and "1/5" in prose

print("unsupervised-learning checks passed")
