"""Checks for the classification research page."""
import json
import re
from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/classification.md").read_text(encoding="utf-8")
pending = json.loads((root / "research/pending/classification.json").read_text(encoding="utf-8"))
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

probs = (Fraction(7, 10), Fraction(1, 5), Fraction(1, 10))
assert sum(probs) == 1
bayes = max(probs)
assert 1 - bayes == Fraction(3, 10)
assert 1 - probs[1] == Fraction(4, 5)
pair = (Fraction(11, 20), Fraction(9, 20))
assert sum(pair) == 1
assert 1 - max(pair) == Fraction(9, 20)
assert "3/10" in prose and "4/5" in prose and "9/20" in prose

print("classification checks passed")
