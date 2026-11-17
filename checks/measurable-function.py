"""Check research/content/measurable-function.md against its pending record."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/measurable-function.md").read_text(encoding="utf-8")
pending = json.loads((root / "research/pending/measurable-function.json").read_text(encoding="utf-8"))
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
assert 2 * F(1, 3) + 7 * F(2, 3) == F(16, 3)
assert 5 * F(1, 3) + 7 * F(2, 3) == F(19, 3)

print("measurable-function passed")
