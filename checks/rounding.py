"""Checks for the rounding page."""
import json
import math
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "rounding"
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
shares = [285 / 600 * 30, 150 / 600 * 30, 90 / 600 * 30, 75 / 600 * 30]
assert shares == [14.25, 7.5, 4.5, 3.75]
assert sum(shares) == 30
half_up = [math.floor(x + 0.5) for x in shares]
assert half_up == [14, 8, 5, 4]
assert sum(half_up) == 31
assert 14 + 7 + 5 + 4 == 30
exact = [30 * x / 3534 for x in (2451, 780, 198, 105)]
assert abs(exact[0] - 20.806451) < 1e-4
shown = [round(x + 1e-12, 2) for x in exact]
assert shown == [20.81, 6.62, 1.68, 0.89]
assert abs(sum(shown) - 30) < 1e-9
nearest = [math.floor(x + 0.5) for x in shown]
assert nearest == [21, 7, 2, 1]
assert sum(nearest) == 31
assert 21 + 6 + 2 + 1 == 30
assert abs(0.0085 * 2451 - 20.8335) < 1e-9
assert abs(0.851 + 0.150 - 1.001) < 1e-12
assert 3496 + 3839 + 1170 == 8505
assert abs(3496 / 8505 - 0.411) < 5e-4
assert abs(2.5 + 2.5 + 3.2 - 8.2) < 1e-12
assert math.floor(2.5 + 0.5) + math.floor(2.5 + 0.5) + math.floor(3.2 + 0.5) == 9
print(slug, "ok")
