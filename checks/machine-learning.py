"""Checks for the machine-learning research page."""
import json
import re
from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parents[1]
self_checks = json.loads((root / "research/self-checks.json").read_text(encoding="utf-8")).get("machine-learning", [])
prose = (root / "research/content/machine-learning.md").read_text(encoding="utf-8")
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

reducible = (10 - 7) ** 2
irreducible = 9
assert reducible == 9 and reducible + irreducible == 18
assert (4 - 1) ** 2 + 4 == 13
assert "equals $18$" in prose and "equals $13$" in prose

print("machine-learning checks passed")
