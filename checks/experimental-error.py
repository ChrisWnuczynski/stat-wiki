"""Check experimental-error against its markdown and pending metadata."""
import json
import re
from pathlib import Path

SLUG = "experimental-error"
ROOT = Path(__file__).resolve().parents[1]
self_checks = json.loads((ROOT / "research/self-checks.json").read_text(encoding="utf-8")).get("experimental-error", [])
md = (ROOT / "research" / "content" / f"{SLUG}.md").read_text(encoding="utf-8")

cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", md)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
assert "**Your turn.**" in md
match = re.search(
    r'::: \{\.callout-tip collapse="true" title="Answer"\}\n(.*?)\n:::',
    md,
    re.S,
)
assert match, "missing answer callout"
assert "{cite:" not in match.group(1)
assert 2 <= len(self_checks) <= 3

assert 2*(4-6.5)**2 + 2*(9-6.5)**2 == 25
assert (3-4)**2 + (5-4)**2 + (8-9)**2 + (10-9)**2 == 4
assert 4/2 == 2
assert 2*(2-4)**2 + 2*(6-4)**2 == 16
assert (1-2)**2 + (3-2)**2 + (5-6)**2 + (7-6)**2 == 4

print(SLUG, "ok")
