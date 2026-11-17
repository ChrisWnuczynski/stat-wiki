"""Checks for the tail page. Reads the article and bibliography.json."""
import json
import math
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "tail"
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
z = (1190 - 1100) / 200
assert z == 0.45
assert abs(1 - 0.6736 - 0.3264) < 1e-12
assert abs(1 - 0.8413447 - 0.1586553) < 1e-12
assert abs(math.exp(-2) - 0.1353352832366) < 1e-12
assert abs(math.exp(-4) - 0.0183156388887) < 1e-12
assert abs(1 - math.exp(-2) - 0.864664716763) < 1e-9
for printed in ("0.3264", "0.6736", "0.8413447", "0.1586553", "0.135335"):
    assert printed in prose, printed
print(slug, "ok")
