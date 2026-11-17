"""Checks for the cluster-analysis research page."""
import re
from fractions import Fraction
from math import isclose, sqrt
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/cluster-analysis.md").read_text(encoding="utf-8")
cites = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(cites) >= 5, cites
assert len(set(cites)) >= 2, set(cites)
found = []
for line in prose.splitlines():
    if line.startswith("## "):
        found.append(line[3:].split(" — ")[0].strip())
assert found == [
    'Lead context',
    'Motivating example',
    'Definition',
    'Interpretation',
    'Worked example',
    'Connections',
    'History',
], found
assert "## Check yourself" not in prose
assert "**Your turn.**" in prose
assert '::: {.callout-tip collapse="true" title="Answer"}' in prose
answer = re.search(
    r'::: \{\.callout-tip collapse="true" title="Answer"\}(.*?):::',
    prose,
    re.S,
)
assert answer and "{cite:" not in answer.group(1)
ab = 1
assert ab == 1
assert isclose(sqrt(2), 1.41421356237)
assert min(5, sqrt(37), 4, sqrt(26)) == 4
wcss = Fraction(1, 2) + 1
assert wcss == Fraction(3, 2)
assert "3/2" in prose and "distance $4$" in prose
assert min(5, sqrt(29)) == 5
print("cluster-analysis checks passed")
