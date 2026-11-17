"""Checks for environmental-statistics."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "environmental-statistics"
md = (ROOT / "research" / "content" / f"{SLUG}.md").read_text(encoding="utf-8")
for line in md.splitlines():
    assert line == line.rstrip(" \t")
heads = re.findall(r"(?m)^## (.+)$", md)
expected = [
    'Lead context',
    'Definition',
    'Statistical use',
    'Common misconceptions',
    'Connections',
    'History',
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
print(SLUG, "ok", len(cites), "cites", len(set(cites)), "keys", len(md.split()), "words")
