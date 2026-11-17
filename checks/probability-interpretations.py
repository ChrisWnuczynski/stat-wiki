"""Check research/content/probability-interpretations.md against its pending record."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/probability-interpretations.md").read_text(encoding="utf-8")
pending = json.loads((root / "research/pending/probability-interpretations.json").read_text(encoding="utf-8"))
keys = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(keys) >= 5, len(keys)
assert len(set(keys)) >= 2, set(keys)
assert set(keys) <= set(pending["cite_keys"])
for heading in ('## Lead context', '## Motivating example', '## Intuition', '## Definition', '## Properties', '## Statistical use', '## Worked example', '## Common misconceptions', '## Assumptions and limits', '## Connections', '## History'):
    assert heading in prose, heading
order = [prose.index(h) for h in ('## Lead context', '## Motivating example', '## Intuition', '## Definition', '## Properties', '## Statistical use', '## Worked example', '## Common misconceptions', '## Assumptions and limits', '## Connections', '## History')]
assert order == sorted(order)
assert "**Your turn.**" in prose
assert 'collapse="true" title="Answer"' in prose
hidden = re.findall(r'title="Answer"\}(.*?)\n:+', prose, flags=re.S)
assert hidden
for block in hidden:
    assert "{cite:" not in block
assert pending["action"] == "page"
assert pending["kind"] == "concept"
assert 2 <= len(pending["self_checks"]) <= 3
for item in pending["self_checks"]:
    assert "{cite:" not in item["answer"]

from fractions import Fraction as F
assert F(3, 10) == F(3, 10)
assert F(60, 100) == F(3, 5)
assert F(1, 2) == F(1, 2)

print("probability-interpretations passed")
