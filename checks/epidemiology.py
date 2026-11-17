"""Checks for epidemiology."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "epidemiology"
md = (ROOT / "research" / "content" / f"{SLUG}.md").read_text(encoding="utf-8")
for line in md.splitlines():
    assert line == line.rstrip(" \t")
heads = re.findall(r"(?m)^## (.+)$", md)
expected = [
    'Lead context',
    'Definition',
    'Properties',
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
assert 500 / 10000 == 0.05
assert 1000 / 10000 == 0.10
assert abs(0.5 * 0.05 + 0.5 * 0.15 - 0.10) < 1e-12
assert 50 / 1000 == 0.05 and 10 / 1000 == 0.01
assert 0.05 / 0.01 == 5
assert abs(0.05 - 0.01 - 0.04) < 1e-12
assert abs(3 / 1_000_000 - 1 / 1_000_000 - 0.000002) < 1e-15
assert 10 / 20 == 0.5
print(SLUG, "ok", len(cites), "cites", len(set(cites)), "keys", len(md.split()), "words")
