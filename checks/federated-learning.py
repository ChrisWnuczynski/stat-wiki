"""Checks for federated-learning."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "federated-learning"
md = (ROOT / "research" / "content" / f"{SLUG}.md").read_text(encoding="utf-8")
for line in md.splitlines():
    assert line == line.rstrip(" \t")
heads = re.findall(r"(?m)^## (.+)$", md)
expected = [
    'Lead context',
    'Motivating example',
    'Intuition',
    'Definition',
    'Properties',
    'Worked example',
    'Assumptions and limits',
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
from fractions import Fraction
pooled = Fraction(2 * 2 + 1 * 10, 3)
unweighted = Fraction(2 + 10, 2)
assert pooled == Fraction(14, 3)
assert unweighted == 6
assert unweighted - pooled == Fraction(4, 3)
equal = Fraction(2 * 2 + 2 * 10, 4)
assert equal == 6
assert "14/3" in md and "4/3" in md
print(SLUG, "ok", len(cites), "cites", len(set(cites)), "keys", len(md.split()), "words")
