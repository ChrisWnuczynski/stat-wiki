"""Check extrapolation against its markdown and pending metadata."""
import json
import re
from pathlib import Path

SLUG = "extrapolation"
ROOT = Path(__file__).resolve().parents[1]
self_checks = json.loads((ROOT / "research/self-checks.json").read_text(encoding="utf-8")).get("extrapolation", [])
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

assert 24319 - 0.0431*1_000_000 == -18781
assert 24319 - 0.0431*200_000 == 15699
assert 24319 - 0.0431*400_000 == 7079

print(SLUG, "ok")
