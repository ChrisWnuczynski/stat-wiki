"""Checks for the dimensionality-reduction research page."""
import json
import re
from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parents[1]
self_checks = json.loads((root / "research/self-checks.json").read_text(encoding="utf-8")).get("dimensionality-reduction", [])
prose = (root / "research/content/dimensionality-reduction.md").read_text(encoding="utf-8")
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

# Centered points (-1,-1), (0,0), (1,1). Total sum of squares is 4.
# The coordinate axis keeps half; the diagonal keeps all of it.
total = 1 + 1 + 0 + 0 + 1 + 1
axis = 1 + 0 + 1
assert total == 4 and axis == 2
assert Fraction(axis, total) == Fraction(1, 2)
assert total - axis == 2
assert "1/2" in prose and "equals $4$" in prose

print("dimensionality-reduction checks passed")
