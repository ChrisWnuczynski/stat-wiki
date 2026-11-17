"""Checks for the cohort-study research page."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/cohort-study.md").read_text(encoding="utf-8")
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
    'Intuition',
    'Definition',
    'Properties',
    'Worked example',
    'Assumptions and limits',
    'Connections',
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
assert 20 / 80 == 0.25
assert 12 / 120 == 0.10
assert (20 / 80) / (12 / 120) == 2.5
assert 21 / 84 == 0.25
print("cohort-study checks passed")
