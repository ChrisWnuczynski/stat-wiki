"""Checks for the survival-analysis page. Reads the article and bibliography.json."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "survival-analysis"
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
assert len(re.findall(r"\S+", prose)) >= 1500
assert "survival-function.qmd" in prose
assert (4 - 1) / 4 == 3 / 4
assert (3 / 4) * (1 / 2) == 3 / 8
assert (3 - 1) / 3 == 2 / 3
assert abs(0.9 ** 2 - 0.81) < 1e-12
assert 48 / 88 < 0.55
assert 88 - 17 == 71
assert 40 - 17 == 23
assert "3/4" in prose and "3/8" in prose and "2/3" in prose
assert "48/88" in prose and "48/71" in prose and "0.81" in prose
print(slug, "ok")
