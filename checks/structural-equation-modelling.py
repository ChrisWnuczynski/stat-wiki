"""Checks for the structural-equation-modelling page. Reads the article and bibliography.json."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "structural-equation-modelling"
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
assert abs(0.447 * 0.885 - 0.395595) < 1e-12
assert abs(0.182 + 0.395595 - 0.577595) < 1e-12
assert abs(0.5 * 0.4 - 0.2) < 1e-12
assert "0.395595" in prose and "0.577595" in prose and "38.125" in prose
print(slug, "ok")
