"""Checks for experimental-error."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "experimental-error"
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
assert 2 * (4 - 6.5) ** 2 + 2 * (9 - 6.5) ** 2 == 25
assert (3 - 4) ** 2 + (5 - 4) ** 2 + (8 - 9) ** 2 + (10 - 9) ** 2 == 4
assert 4 / 2 == 2
assert 2 * (2 - 4) ** 2 + 2 * (6 - 4) ** 2 == 16
assert (1 - 2) ** 2 + (3 - 2) ** 2 + (5 - 6) ** 2 + (7 - 6) ** 2 == 4
print(SLUG, "ok", len(cites), "cites", len(set(cites)), "keys", len(md.split()), "words")
