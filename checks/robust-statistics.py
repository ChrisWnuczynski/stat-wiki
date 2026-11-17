"""Checks for the robust-statistics page."""
import json
import math
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "robust-statistics"
text = (root / "research/content" / f"{slug}.md").read_text(encoding="utf-8")
assert text.endswith("\n") and not text.endswith("\n\n")
for line in text.splitlines():
    assert line == line.rstrip(" \t"), repr(line)
headings = [
    "Lead context",
    "Motivating example",
    "Intuition",
    "Definition",
    "Properties",
    "Worked example",
    "Assumptions and limits",
    "Connections",
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
data = [1, 2, 3, 4, 20]
mean = sum(data) / 5
assert mean == 6
# S(t) = 430 - 60t + 5t^2, derivative 10(t-6)
def S(t):
    return 430 - 60 * t + 5 * t * t

assert S(6) == 250
assert S(5) == 255 and S(7) == 255
assert S(3) == 295
assert sum((v - mean) ** 2 for v in data) == 250
assert sum((v - 3) ** 2 for v in data) == 295
assert sum(abs(v - mean) for v in data) == 28
assert sum(abs(v - 3) for v in data) == 21
wild = [5, 5, 5, 5, 100]
assert sum(wild) / 5 == 24
assert sum(abs(v - 24) for v in wild) == 152
assert sum(abs(v - 5) for v in wild) == 95
assert (1 + 2 + 3 + 4 + 200) / 5 == 42
assert "250" in text and "255" in text and "295" in text and "152" in text
print(slug, "ok")
