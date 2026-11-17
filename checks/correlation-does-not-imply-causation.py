"""Checks for the correlation-does-not-imply-causation concept page."""
import json, re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
self_checks = json.loads((root / "research/self-checks.json").read_text(encoding="utf-8")).get("correlation-does-not-imply-causation", [])
prose = (root / "research/content/correlation-does-not-imply-causation.md").read_text()
cites = re.findall(r"\{cite:([^}]+)\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2
assert "**Your turn.**" in prose
assert '::: {.callout-tip collapse="true" title="Answer"}' in prose
answer = prose.split('title="Answer"}', 1)[1].split(":::", 1)[0]
assert "{cite:" not in answer
assert 2 <= len(self_checks) <= 3
for item in self_checks:
    assert "{cite:" not in item["answer"]

from fractions import Fraction
assert 7 * 7 - 3 * 13 == 10
assert Fraction(7, 13) - Fraction(3, 7) == Fraction(10, 91)
assert Fraction(10, 20) - Fraction(10, 20) == 0
assert Fraction(8, 20) - Fraction(12, 20) == Fraction(-1, 5)

print("correlation-does-not-imply-causation:", len(cites), "cites,", len(set(cites)), "keys")
