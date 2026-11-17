"""Check research/content/bayesian-probability.md against its pending record."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/bayesian-probability.md").read_text(encoding="utf-8")
pending = json.loads((root / "research/pending/bayesian-probability.json").read_text(encoding="utf-8"))
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
def price(odds):
    return F(1, odds + 1)
assert price(10) == F(1, 11)
assert price(3) == F(1, 4)

print("bayesian-probability passed")
