"""Checks for the systematic-error page. Reads the article and bibliography.json."""
import json
import math
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "systematic-error"
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
reads = [21.4, 21.7, 21.2, 21.5]
mean = sum(reads) / 4
assert abs(mean - 21.45) < 1e-12
assert abs(mean - 20 - 1.45) < 1e-12
ss = sum((v - mean) ** 2 for v in reads)
assert abs(ss - 0.13) < 1e-12
assert abs(math.sqrt(0.13 / 12) - 0.10408329997330664) < 1e-12
gauge = [12, 11, 13]
assert sum(gauge) / 3 == 12
assert abs(sum(gauge) / 3 - 10 - 2) < 1e-12
assert "1.45" in prose and "0.13" in prose
print(slug, "ok")
