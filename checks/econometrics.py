"""Checks for econometrics."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "econometrics"
md = (ROOT / "research" / "content" / f"{SLUG}.md").read_text(encoding="utf-8")
for line in md.splitlines():
    assert line == line.rstrip(" \t")
heads = re.findall(r"(?m)^## (.+)$", md)
expected = [
    'Lead context',
    'Definition',
    'Interpretation',
    'Statistical use',
    'History',
    'Connections',
]
assert heads == expected, heads
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", md)
assert len(cites) >= 5, (len(cites), set(cites))
assert len(set(cites)) >= 2, set(cites)
assert "hansen2010" not in cites
for banned in (
    'not a claim',
    'not claimed',
    'this page',
    'Dodge states',
    'the manual',
    'question bank',
    'letter opener',
    'Wikipedia',
    'Grokipedia',
):
    assert banned not in md, banned
assert "## Check yourself" not in md
assert "**Your turn.**" not in md
assert len(md.split()) >= 1000, len(md.split())
assert 0.53 < 1.08 < 1.36
assert "0.53" in md and "1.08" in md and "1.36" in md and "4.59" in md
print(SLUG, "ok", len(cites), "cites", len(set(cites)), "keys", len(md.split()), "words")
