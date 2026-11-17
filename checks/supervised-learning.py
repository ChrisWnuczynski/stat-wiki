"""Checks for the supervised-learning page. Reads the article and bibliography.json."""
import json
import re
from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "supervised-learning"
prose = (root / "research/content" / f"{slug}.md").read_text(encoding="utf-8")
bib = json.loads((root / "bibliography.json").read_text(encoding="utf-8"))
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
works = bib["works"]
assert set(cites) <= set(works), set(cites) - set(works)
for line in prose.splitlines():
    assert line == line.rstrip()
assert prose.endswith("\n") and not prose.endswith("\n\n")
for bad in (
    "not a claim",
    "not claimed",
    "this page",
    "Dodge states",
    "the manual",
    "question bank",
    "letter opener",
    "Wikipedia",
    "Grokipedia",
):
    assert bad not in prose, bad
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
found = [re.split(r" — ", h, maxsplit=1)[0] for h in re.findall(r"^## (.+)$", prose, re.M)]
assert found == headings, found
assert "**Your turn.**" in prose
assert "## Check yourself" not in prose
answer = re.search(
    r'::: \{\.callout-tip collapse="true" title="Answer"\}(.*?):::',
    prose,
    re.S,
)
assert answer, "missing answer callout"
assert "{cite:" not in answer.group(1)
points = ((0, 0), (1, 0), (4, 1))

def nearest(x):
    return min(points, key=lambda p: abs(x - p[0]))[1]

assert nearest(3) == 1
assert nearest(2) == 0
assert nearest(Fraction(2, 5)) == 0
assert all(nearest(x) == y for x, y in points)
assert r"\(1\)" in prose and r"\(0\)" in prose
print(slug, "ok")
