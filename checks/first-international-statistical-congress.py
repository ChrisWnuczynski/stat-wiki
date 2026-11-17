"""Checks for first-international-statistical-congress."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "first-international-statistical-congress"
md = (ROOT / "research" / "content" / f"{SLUG}.md").read_text(encoding="utf-8")
for line in md.splitlines():
    assert line == line.rstrip(" \t")
heads = re.findall(r"(?m)^## (.+)$", md)
expected = [
    'Lead context',
    'Motivating example',
    'Definition',
    'Properties',
    'Statistical use',
    'Worked example',
    'Common misconceptions',
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
assert "**Your turn.**" in md
match = re.search(
    r'::: \{\.callout-tip collapse="true" title="Answer"\}(.*?):::',
    md,
    re.S,
)
assert match, "missing answer callout"
assert "{cite:" not in match.group(1)
data = json.loads((ROOT / "research" / "self-checks.json").read_text(encoding="utf-8"))
items = data[SLUG]
assert 2 <= len(items) <= 3
for item in items:
    assert "{cite:" not in item["answer"]
assert 240 / 800 == 0.30
assert 150 / 600 == 0.25
assert abs((240 / 800) - (150 / 600) - 0.05) < 1e-12
assert (240 + 150) == 390
assert (800 + 600) == 1400
assert 390 / 1400 == 39 / 140
assert 80 / 200 == 0.4
assert 90 / 300 == 0.3
assert abs((80 / 200) - (90 / 300) - 0.1) < 1e-12
assert (80 + 90) / (200 + 300) == 170 / 500 == 0.34
assert 1876 - 1853 == 23
assert 23 / 8 == 2.875
print(SLUG, "ok", len(cites), "cites", len(set(cites)), "keys", len(md.split()), "words")
