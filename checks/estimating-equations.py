"""Check estimating-equations against its markdown and pending metadata."""
import json
import re
from pathlib import Path

SLUG = "estimating-equations"
ROOT = Path(__file__).resolve().parents[1]
self_checks = json.loads((ROOT / "research/self-checks.json").read_text(encoding="utf-8")).get("estimating-equations", [])
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

assert (2+4+6)/3 == 4
assert (1+3+8)/3 == 4
second = (1+9+64)/3 - (16+1)
assert abs(second - (74/3 - 17)) < 1e-12
assert abs(second) > 1

print(SLUG, "ok")
