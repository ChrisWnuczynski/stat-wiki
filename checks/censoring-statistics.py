"""Checks for the censoring-statistics page."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/censoring-statistics.md").read_text(encoding="utf-8")
cites = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2
headings = [line[3:].split("—")[0].strip() for line in prose.splitlines() if line.startswith("## ")]
assert headings == ["Lead context", "Motivating example", "Definition", "Properties", "Worked example", "Assumptions and limits", "History"], headings
assert "## Motivating example" in prose
assert "## Worked example" in prose
assert "**Your turn.**" in prose
assert '::: {.callout-tip collapse="true" title="Answer"}' in prose
assert "## Check yourself" not in prose
answer = prose.split('title="Answer"}', 1)[1].split(":::", 1)[0]
assert "{cite:" not in answer
banned = ("not a claim", "not claimed", "this page", "Dodge states", "the manual", "question bank", "letter opener", "Wikipedia", "Grokipedia")
for phrase in banned:
    assert phrase.lower() not in prose.lower(), phrase

assert (4 / 5) * (1 / 3) == 4 / 15
assert (4 / 5) * (3 / 4) * (1 / 3) == 1 / 5
assert (3 - 1) / 3 * (2 - 1) / 2 == 1 / 3

print("censoring-statistics:", len(cites), "cites,", len(set(cites)), "keys")
