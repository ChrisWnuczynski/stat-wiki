"""Check base-rate against its markdown and pending metadata."""
import json
import re
from pathlib import Path

SLUG = "base-rate"
ROOT = Path(__file__).resolve().parents[1]
self_checks = json.loads((ROOT / "research/self-checks.json").read_text(encoding="utf-8")).get("base-rate", [])
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

num = 0.0035*0.89
den = num + 0.9965*0.07
assert abs(num/den - 0.04275) < 5e-4
num2 = 0.20*0.89
den2 = num2 + 0.80*0.07
assert abs(num2/den2 - 0.76068376) < 1e-6
assert abs((0.01*0.90)/(0.01*0.90 + 0.99*0.05) - 0.1538461538) < 1e-9

print(SLUG, "ok")
