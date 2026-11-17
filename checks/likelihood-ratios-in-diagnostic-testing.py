"""Check likelihood-ratios-in-diagnostic-testing against its markdown and pending metadata."""
import json
import re
from pathlib import Path

SLUG = "likelihood-ratios-in-diagnostic-testing"
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

lr = 0.89/0.07
prior = 0.0035/0.9965
post_odds = lr*prior
post = post_odds/(1+post_odds)
assert abs(lr - 12.7142857) < 1e-6
assert abs(post - 0.042747) < 1e-5
assert abs((0.80/0.10)*(0.20/0.80) - 2) < 1e-12
assert abs(2/3 - 0.6666666667) < 1e-9

print(SLUG, "ok")
