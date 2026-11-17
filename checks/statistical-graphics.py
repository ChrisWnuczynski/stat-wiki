"""Checks for the statistical-graphics page."""
import json
import math
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "statistical-graphics"
text = (root / "research/content" / f"{slug}.md").read_text(encoding="utf-8")
assert text.endswith("\n") and not text.endswith("\n\n")
for line in text.splitlines():
    assert line == line.rstrip(" \t"), repr(line)
headings = [
    "Lead context",
    "Intuition",
    "Definition",
    "Statistical use",
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
assert "**Your turn.**" not in text
words = len(text.split())
assert words >= 1000, words
for link in ("histogram.qmd", "line-chart.qmd", "summary-statistics.qmd", "scatterplot.qmd"):
    assert link in text, link
assert abs(0.851 + 0.150 - 1.001) < 1e-12
print(slug, "ok")
