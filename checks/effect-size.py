"""Check effect-size against its markdown and pending metadata."""
import json
import re
from pathlib import Path

SLUG = "effect-size"
ROOT = Path(__file__).resolve().parents[1]
md = (ROOT / "research" / "content" / f"{SLUG}.md").read_text(encoding="utf-8")
pending = json.loads((ROOT / "research" / "pending" / f"{SLUG}.json").read_text(encoding="utf-8"))

cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", md)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
assert "## Motivating example" in md
assert "## Worked example" in md
assert "**Your turn.**" in md
match = re.search(
    r'::: \{\.callout-tip collapse="true" title="Answer"\}\n(.*?)\n:::',
    md,
    re.S,
)
assert match, "missing answer callout"
assert "{cite:" not in match.group(1)
assert pending["kind"] == "concept"
assert 2 <= len(pending["self_checks"]) <= 3

assert abs(1.96*1.7 - 3.332) < 1e-9
assert abs((-3.332 - (-3))/1.7 - (-0.1952941176)) < 1e-6
assert abs(( -3.92 - (-5) )/2 - 0.54) < 1e-9

print(SLUG, "ok")
