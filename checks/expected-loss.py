"""Checks for expected-loss."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = "expected-loss"
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
assert abs(0.2 * 1 + 0.8 * 8 - 6.6) < 1e-9
assert abs(0.2 * 10 - 2) < 1e-9
assert abs(0.7 * 1 + 0.3 * 8 - 3.1) < 1e-9
assert abs(0.7 * 10 - 7) < 1e-9
assert 2 < 6.6
assert abs(0.9 * 16.7 + 0.1 * 34.8 - 1 - 17.51) < 1e-9
assert abs(0.632 * 15.0 + 0.368 * 19.5 - 16.656) < 1e-9
print(SLUG, "ok", len(cites), "cites", len(set(cites)), "keys", len(md.split()), "words")
