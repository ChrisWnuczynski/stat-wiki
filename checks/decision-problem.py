"""Checks for the decision-problem research page."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/decision-problem.md").read_text(encoding="utf-8")
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
assert abs(0.9 * 16.7 + 0.1 * 34.8 - 1 - 17.51) < 1e-9
assert abs(0.9 * 5.6 + 0.1 * 34.8 - 8.52) < 1e-9
surgery = 0.65 * (0.5 * 20.3 + 0.5 * 34.8 - 1)
assert abs(surgery - 17.2575) < 1e-9
radio = 0.5 * 16.7 + 0.5 * 34.8 - 1
assert abs(radio - 24.75) < 1e-9
assert surgery < radio
print("decision-problem checks passed")
