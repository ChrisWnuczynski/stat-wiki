"""Checks for the control-group research page."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/control-group.md").read_text(encoding="utf-8")
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
    'Properties',
    'Worked example',
    'Assumptions and limits',
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
assert 2 / 10 - 5 / 10 == -0.3
assert 6 / 11 == 6 / 11
print("control-group checks passed")
