"""Checks for the cluster-analysis research page."""
import json
import re
from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/cluster-analysis.md").read_text(encoding="utf-8")
pending = json.loads((root / "research/pending/cluster-analysis.json").read_text(encoding="utf-8"))
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

# Single link on A(0,0), B(1,0), C(5,0), D(6,1), and the within-cluster sum of squares.
ab = 1
cd = Fraction(2).sqrt() if hasattr(Fraction(2), "sqrt") else None
from math import isclose, sqrt
assert ab == 1
assert isclose(sqrt(2), 1.41421356237)
assert min(5, sqrt(37), 4, sqrt(26)) == 4
wcss = Fraction(1, 2) + 1
assert wcss == Fraction(3, 2)
assert "3/2" in prose and "distance $4$" in prose

print("cluster-analysis checks passed")
