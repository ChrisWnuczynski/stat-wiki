"""Check expected-loss against its markdown and pending metadata."""
import json
import re
from pathlib import Path

SLUG = "expected-loss"
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

assert abs(0.2*1 + 0.8*8 - 6.6) < 1e-9
assert abs(0.2*10 - 2) < 1e-9
assert abs(0.7*1 + 0.3*8 - 3.1) < 1e-9
assert abs(0.7*10 - 7) < 1e-9
assert 2 < 6.6

print(SLUG, "ok")
