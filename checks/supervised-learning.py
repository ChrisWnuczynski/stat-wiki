"""Checks for the supervised-learning research page."""
import json
import re
from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parents[1]
self_checks = json.loads((root / "research/self-checks.json").read_text(encoding="utf-8")).get("supervised-learning", [])
prose = (root / "research/content/supervised-learning.md").read_text(encoding="utf-8")
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

# 1-nearest neighbour on (0, 0), (1, 0), (4, 1).
points = ((0, 0), (1, 0), (4, 1))

def nearest(x):
    return min(points, key=lambda p: abs(x - p[0]))[1]

assert nearest(3) == 1
assert nearest(2) == 0
assert nearest(Fraction(2, 5)) == 0
assert all(nearest(x) == y for x, y in points)
assert "label $1$" in prose and "label $0$" in prose

print("supervised-learning checks passed")
