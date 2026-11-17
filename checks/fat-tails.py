"""Checks for fat-tails."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "fat-tails"
md = (ROOT / "research" / "content" / f"{SLUG}.md").read_text(encoding="utf-8")
for line in md.splitlines():
    assert line == line.rstrip(" \t")
heads = re.findall(r"(?m)^## (.+)$", md)
expected = [
    'Lead context',
    'Motivating example',
    'Intuition',
    'Definition',
    'Statistical use',
    'Worked example',
    'Common misconceptions',
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
import math
def kurt(v):
    n = len(v)
    m = sum(v) / n
    m2 = sum((x - m) ** 2 for x in v) / n
    m4 = sum((x - m) ** 4 for x in v) / n
    return m4 / m2 ** 2
assert kurt([1, 2, 3, 4, 5]) == 1.7
assert kurt([1, 1, 1, 1, 6]) == 3.25
mu4 = 24 - 4 * 6 + 6 * 2 - 4 * 1 + 1
assert mu4 == 9
assert abs(math.exp(-4) - 0.01831563888873418) < 1e-15
assert abs(math.exp(-1) - 0.36787944117) < 1e-8
assert "0.018316" in md
assert "1.7" in md and "3.25" in md
assert "6,693" in md and "998.389" in md
print(SLUG, "ok", len(cites), "cites", len(set(cites)), "keys", len(md.split()), "words")
