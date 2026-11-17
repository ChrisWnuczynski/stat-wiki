"""Checks for the uncertainty page. Reads the article and bibliography.json."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "uncertainty"
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
    "Intuition",
    "Definition",
    "Statistical use",
    "Worked example",
    "Common misconceptions",
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
vals = [5, 7, 6, 6]
assert sum(vals) / 4 == 6
assert sum(abs(v - 6) for v in vals) / 4 == 0.5
vals2 = [5, 7, 6, 6, 8]
mean = sum(vals2) / 5
assert mean == 6.4
assert abs(sum(abs(v - mean) for v in vals2) / 5 - 0.88) < 1e-9
assert abs((0.2578 - 0.1951) - 0.0627) < 1e-12
ratio = 0.1503 / 0.0627
assert abs(ratio - 2.3971291866028707) < 1e-12
assert abs(round(ratio, 1) - 2.4) < 1e-12
assert "Ch. 8, §8.1" in prose
print(slug, "ok")
