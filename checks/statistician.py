"""Checks for the statistician page. Reads the article and bibliography.json."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "statistician"
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
    "Interpretation",
    "Worked example",
    "Connections",
    "History",
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
counts = (120, 80, 200, 100)
assert sum(counts) == 500
assert 500 / 4 == 125
assert 200 / 500 == 0.4
assert 80 / 500 == 0.16
assert 200 - 80 == 120
small = (30, 45, 75)
assert sum(small) == 150
assert 150 / 3 == 50
assert 75 / 150 == 0.5
print(slug, "ok")
