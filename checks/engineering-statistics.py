"""Checks for engineering-statistics."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "engineering-statistics"
md = (ROOT / "research" / "content" / f"{SLUG}.md").read_text(encoding="utf-8")
for line in md.splitlines():
    assert line == line.rstrip(" \t")
heads = re.findall(r"(?m)^## (.+)$", md)
expected = [
    'Lead context',
    'Intuition',
    'Definition',
    'Statistical use',
    'Assumptions and limits',
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
assert 2 ** 6 == 64
assert 64 / 2 == 32
assert 20 - 7 == 13
assert "64" in md and "32" in md
print(SLUG, "ok", len(cites), "cites", len(set(cites)), "keys", len(md.split()), "words")
