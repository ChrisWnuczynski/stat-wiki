"""Checks for the statistical-dispersion page."""
import json
import math
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "statistical-dispersion"
text = (root / "research/content" / f"{slug}.md").read_text(encoding="utf-8")
assert text.endswith("\n") and not text.endswith("\n\n")
for line in text.splitlines():
    assert line == line.rstrip(" \t"), repr(line)
headings = [
    "Lead context",
    "Motivating example",
    "Definition",
    "Properties",
    "Statistical use",
    "Worked example",
    "Common misconceptions",
    "History",
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
from fractions import Fraction as F
vals = [2, 4, 4, 7, 8]
mean = sum(vals) / 5
assert mean == 5
ss = sum((x - mean) ** 2 for x in vals)
assert ss == 24
assert ss / 4 == 6
assert sum(abs(x - mean) for x in vals) / 5 == 2
assert max(vals) - min(vals) == 6
fam = [0, 0, 1, 1, 2, 3, 6]
assert max(fam) - min(fam) == 6
m = F(sum(fam), 7)
aad = sum(abs(F(x) - m) for x in fam) / 7
assert aad == F(76, 49)
assert abs(math.sqrt(25.52) - 5.05) < 0.01
assert 34 / 50 == 0.68 and 48 / 50 == 0.96
assert "25.52" in text and "5.05" in text
assert 10 ** 2 == 100 and 2 ** 2 == 4
exam1 = [3.5, 4, 4.5, 3.5, 4.5]
exam2 = [2.5, 5.5, 3.5, 4.5, 4]
assert sum(exam1) / 5 == 4 and sum(exam2) / 5 == 4
s1 = math.sqrt(sum((x - 4) ** 2 for x in exam1) / 4)
s2 = math.sqrt(sum((x - 4) ** 2 for x in exam2) / 4)
assert abs(s1 - 0.5) < 1e-12
assert abs(s2 - math.sqrt(1.25)) < 1e-12
assert "0.997" in text and "998.389" in text and "1.16" in text
print(slug, "ok")
