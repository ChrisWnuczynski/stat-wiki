"""Checks for the apriori-algorithm research page."""
import json
import re
from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parents[1]
self_checks = json.loads((root / "research/self-checks.json").read_text(encoding="utf-8")).get("apriori-algorithm", [])
prose = (root / "research/content/apriori-algorithm.md").read_text(encoding="utf-8")
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

# Four baskets: {a,b}, {a,b}, {a}, {b,c}.
support_ab = Fraction(2, 4)
support_a = Fraction(3, 4)
support_b = Fraction(3, 4)
support_bc = Fraction(1, 4)
confidence_a_to_b = support_ab / support_a
lift = confidence_a_to_b / support_b
assert support_ab == Fraction(1, 2)
assert confidence_a_to_b == Fraction(2, 3)
assert lift == Fraction(8, 9)
assert support_bc == Fraction(1, 4)
# Items with support strictly above 2/5: a and b, not c.
assert support_a > Fraction(2, 5) and support_b > Fraction(2, 5)
assert not support_bc > Fraction(2, 5)
assert "2/3" in prose and "8/9" in prose and "1/4" in prose

print("apriori-algorithm checks passed")
