"""Checks for the statistical-process-control page."""
import json
import math
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "statistical-process-control"
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
assert abs(0.00135 * 2 - 0.0027) < 1e-12
upper = 0.8 + 3 * math.sqrt(0.8)
assert abs(upper - 3.48) < 0.005
# P(X > 3) for Poisson(0.8)
lam = 0.8
term = math.exp(-lam)
total = term
for k in range(1, 4):
    term *= lam / k
    total += term
assert abs(1 - total - 0.009) < 0.001
assert "0.00135" in text and "0.0027" in text and "3.48" in text and "0.009" in text
print(slug, "ok")
