"""Checks for the abundance-estimation page."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/abundance-estimation.md").read_text(encoding="utf-8")
cites = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
headings = [line[3:].split("—")[0].strip() for line in prose.splitlines() if line.startswith("## ")]
assert headings == ['Lead context', 'Motivating example', 'Definition', 'Properties', 'Worked example', 'Assumptions and limits', 'History'], headings
assert "**Your turn.**" in prose
assert '::: {.callout-tip collapse="true" title="Answer"}' in prose
answer = prose.split('title="Answer"}', 1)[1].split(":::", 1)[0]
assert "{cite:" not in answer
assert "## Check yourself" not in prose
banned = ("not a claim", "not claimed", "this page", "Dodge states", "the manual", "question bank", "letter opener", "Wikipedia", "Grokipedia")
low = prose.lower()
for phrase in banned:
    assert phrase.lower() not in low, phrase
assert (15 * 20) / 5 == 60
assert (21 * 16) / 6 - 1 == 55
assert (15 * 20) / 10 == 30

print("abundance-estimation:", len(cites), "cites")
