"""Checks for the statistical-theory page. Reads the article and bibliography.json."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "statistical-theory"
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
    "Definition",
    "Statistical use",
    "Common misconceptions",
    "Connections",
    "History",
]
found = [re.split(r" — ", h, maxsplit=1)[0] for h in re.findall(r"^## (.+)$", prose, re.M)]
assert found == headings, found
assert "**Your turn.**" not in prose
assert "## Check yourself" not in prose
assert len(re.findall(r"\S+", prose)) >= 1000
assert "loss-and-risk.qmd" in prose
assert 1 + 2**2 == 5
assert 9 + 0**2 == 9
assert "1+4=5" in prose
print(slug, "ok")
