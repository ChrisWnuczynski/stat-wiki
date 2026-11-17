"""Check research/content/measurable-function.md against its pending record."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
self_checks = json.loads((root / "research/self-checks.json").read_text(encoding="utf-8")).get("measurable-function", [])
prose = (root / "research/content/measurable-function.md").read_text(encoding="utf-8")
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
assert 2 * F(1, 3) + 7 * F(2, 3) == F(16, 3)
assert 5 * F(1, 3) + 7 * F(2, 3) == F(19, 3)

print("measurable-function passed")
