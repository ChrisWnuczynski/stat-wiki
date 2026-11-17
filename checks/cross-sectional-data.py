"""Checks for the cross-sectional-data research page."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/cross-sectional-data.md").read_text(encoding="utf-8")
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
incomes = (2, 4, 4, 6, 9)
assert sum(incomes) == 25
assert 25 / 5 == 5
devs = (-3, -1, -1, 1, 4)
assert devs == (-3, -1, -1, 1, 4)
assert sum(d * d for d in devs) == 28
assert 28 / 4 == 7
trio = (3, 5, 7)
assert sum(trio) / 3 == 5
assert 7 - 3 == 4
print("cross-sectional-data checks passed")
