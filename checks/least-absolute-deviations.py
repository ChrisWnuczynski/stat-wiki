"""Check least-absolute-deviations against its markdown and pending metadata."""
import json
import re
from pathlib import Path

SLUG = "least-absolute-deviations"
ROOT = Path(__file__).resolve().parents[1]
self_checks = json.loads((ROOT / "research/self-checks.json").read_text(encoding="utf-8")).get("least-absolute-deviations", [])
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

assert abs(0) + abs(1.5) + abs(0) == 1.5
assert abs(0) + abs(0) + abs(3) == 3
assert abs(1-1) + abs(1-1) + abs(5-1) == 4
assert abs(1-1) + abs(1-3) + abs(5-5) == 2
assert 2 < 4

print(SLUG, "ok")
