"""Checks for the standard-score page."""
import json
import math
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "standard-score"
text = (root / "research/content" / f"{slug}.md").read_text(encoding="utf-8")
assert text.endswith("\n") and not text.endswith("\n\n")
for line in text.splitlines():
    assert line == line.rstrip(" \t"), repr(line)
headings = [
    "Lead context",
    "Motivating example",
    "Definition",
    "Properties",
    "Worked example",
    "Assumptions and limits",
    "History",
]
found = [re.split(r"\s+[—-]\s+", item, maxsplit=1)[0] for item in re.findall(r"^## (.+)$", text, re.M)]
assert found == headings, found
cites = re.findall(r"\{{cite:([a-z0-9_]+)\}}", text)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
bib = json.loads((root / "bibliography.json").read_text(encoding="utf-8"))["works"]
for key in set(cites):
    assert key in bib, key
banned = (
    "not a claim",
    "not claimed",
    "this page",
    "dodge states",
    "the manual",
    "question bank",
    "letter opener",
    "wikipedia",
    "grokipedia",
)
low = text.lower()
for phrase in banned:
    assert phrase not in low, phrase
for match in re.finditer(r"\{{cite:openintro2019\}}\s*\(([^)]*)\)", text):
    loc = match.group(1).lower()
    assert "p." not in loc, match.group(1)
    assert "§" in match.group(1), match.group(1)
assert "## Check yourself" not in text
assert "**Your turn.**" in text
assert '::: {.callout-tip collapse="true" title="Answer"}' in text
answer = text.split('title="Answer"}', 1)[1].split(":::", 1)[0]
assert "{cite:" not in answer
assert (1300 - 1100) / 200 == 1
assert (24 - 21) / 6 == 0.5
sample = [2, 4, 6]
mean = sum(sample) / 3
var = sum((x - mean) ** 2 for x in sample) / (3 - 1)
assert mean == 4 and var == 4
assert (6 - 4) / math.sqrt(var) == 1
assert (2 - 4) / math.sqrt(var) == -1
assert (90 - 78) / 6 == 2
print(slug, "ok")
