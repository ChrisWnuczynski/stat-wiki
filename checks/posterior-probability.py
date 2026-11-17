"""Check research/content/posterior-probability.md against its pending record."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
self_checks = json.loads((root / "research/self-checks.json").read_text(encoding="utf-8")).get("posterior-probability", [])
prose = (root / "research/content/posterior-probability.md").read_text(encoding="utf-8")
keys = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(keys) >= 5, len(keys)
assert len(set(keys)) >= 2, set(keys)
assert "**Your turn.**" in prose
assert 'collapse="true" title="Answer"' in prose
hidden = re.findall(r'title="Answer"\}(.*?)\n:+', prose, flags=re.S)
assert hidden
for block in hidden:
    assert "{cite:" not in block
assert 2 <= len(self_checks) <= 3
for item in self_checks:
    assert "{cite:" not in item["answer"]

from fractions import Fraction as F
assert F(1, 4) * F(1, 2) == F(1, 8)
assert F(3, 4) * F(1, 6) == F(1, 8)
assert F(1, 8) / F(1, 4) == F(1, 2)
assert (F(1, 2) / F(1, 6)) * (F(1, 4) / F(3, 4)) == 1
assert F(1, 2) * F(1, 2) == F(1, 4)
assert F(1, 2) * F(1, 6) == F(1, 12)
assert F(1, 4) + F(1, 12) == F(1, 3)
assert F(1, 4) / F(1, 3) == F(3, 4)

print("posterior-probability passed")
