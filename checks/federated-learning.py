"""Checks for the federated-learning research page."""
import json
import re
from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/federated-learning.md").read_text(encoding="utf-8")
pending = json.loads((root / "research/pending/federated-learning.json").read_text(encoding="utf-8"))
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", prose)
assert len(cites) >= 5, cites
assert len(set(cites)) >= 2, set(cites)
positions = [prose.index(h) for h in ['## Lead context', '## Motivating example', '## Intuition', '## Definition', '## Properties', '## Statistical use', '## Worked example', '## Common misconceptions', '## Assumptions and limits', '## Connections', '## History']]
assert positions == sorted(positions)
assert "## Motivating example" in prose and "## Worked example" in prose
assert "**Your turn.**" in prose
assert '::: {.callout-tip collapse="true" title="Answer"}' in prose
answer = re.search(
    r'::: \{\.callout-tip collapse="true" title="Answer"\}(.*?):::',
    prose,
    re.S,
)
assert answer and "{cite:" not in answer.group(1)
assert "## Check yourself" not in prose
checks = pending["self_checks"]
assert 2 <= len(checks) <= 3
assert all("{cite:" not in item["answer"] for item in checks)

# Client means 2 (size 2) and 10 (size 1).
pooled = Fraction(2 * 2 + 1 * 10, 3)
unweighted = Fraction(2 + 10, 2)
assert pooled == Fraction(14, 3)
assert unweighted == 6
assert unweighted - pooled == Fraction(4, 3)
equal = Fraction(2 * 2 + 2 * 10, 4)
assert equal == 6
assert "14/3" in prose and "4/3" in prose

print("federated-learning checks passed")
