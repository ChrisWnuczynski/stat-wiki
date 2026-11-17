"""Check decision-problem against its markdown and pending metadata."""
import json
import re
from pathlib import Path

SLUG = "decision-problem"
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

assert abs(0.9*16.7 + 0.1*34.8 - 1 - 17.51) < 1e-9
assert abs(0.9*5.6 + 0.1*34.8 - 8.52) < 1e-9
surgery = 0.65*(0.5*20.3 + 0.5*34.8 - 1)
assert abs(surgery - 17.2575) < 1e-9
radio = 0.5*16.7 + 0.5*34.8 - 1
assert abs(radio - 24.75) < 1e-9
assert surgery < radio

print(SLUG, "ok")
