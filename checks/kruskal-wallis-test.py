"""Check kruskal-wallis-test against its markdown and pending metadata."""
import json
import re
from pathlib import Path

SLUG = "kruskal-wallis-test"
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

from fractions import Fraction
assert Fraction(12, 9*10) * Fraction(725, 3) - 30 == Fraction(20, 9)
assert Fraction(756 - 507, 13) == Fraction(249, 13)
assert 13.64 > 7.81

print(SLUG, "ok")
