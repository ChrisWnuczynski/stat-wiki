"""Checks for feature-selection."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "feature-selection"
md = (ROOT / "research" / "content" / f"{SLUG}.md").read_text(encoding="utf-8")
for line in md.splitlines():
    assert line == line.rstrip(" \t")
heads = re.findall(r"(?m)^## (.+)$", md)
expected = [
    'Lead context',
    'Motivating example',
    'Definition',
    'Interpretation',
    'Worked example',
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
cases = ((0, 0, 1), (1, 0, 1), (2, 1, 3))
mean_y = Fraction(sum(y for _, _, y in cases), 3)
assert mean_y == Fraction(5, 3)
rss_intercept = sum((Fraction(y) - mean_y) ** 2 for _, _, y in cases)
assert rss_intercept == Fraction(8, 3)
fitted_x = [Fraction(2, 3) + x for x, _, _ in cases]
rss_x = sum((Fraction(y) - fit) ** 2 for (_, _, y), fit in zip(cases, fitted_x))
assert rss_x == Fraction(2, 3)
fitted_z = [1 + 2 * z for _, z, _ in cases]
rss_z = sum((Fraction(y) - fit) ** 2 for (_, _, y), fit in zip(cases, fitted_z))
assert rss_z == 0
assert rss_z < rss_x < rss_intercept
assert 2 ** 20 == 1_048_576
assert 1 + 20 * 21 // 2 == 211
assert "8/3" in md and "2/3" in md and "1{,}048{,}576" in md and "211" in md
print(SLUG, "ok", len(cites), "cites", len(set(cites)), "keys", len(md.split()), "words")
