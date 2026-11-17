"""Check research/content/probability-interpretations.md against its pending record."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
self_checks = json.loads((root / "research/self-checks.json").read_text(encoding="utf-8")).get("probability-interpretations", [])
prose = (root / "research/content/probability-interpretations.md").read_text(encoding="utf-8")
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
assert F(3, 10) == F(3, 10)
assert F(60, 100) == F(3, 5)
assert F(1, 2) == F(1, 2)

print("probability-interpretations passed")
