"""Check estimation-theory against its markdown and pending metadata."""
import json
import re
from pathlib import Path

SLUG = "estimation-theory"
ROOT = Path(__file__).resolve().parents[1]
md = (ROOT / "research" / "content" / f"{SLUG}.md").read_text(encoding="utf-8")
pending = json.loads((ROOT / "research" / "pending" / f"{SLUG}.json").read_text(encoding="utf-8"))

cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", md)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
assert "**Your turn.**" not in md
assert "## Check yourself" not in md
assert pending["kind"] == "field"
assert "self_checks" not in pending
print(SLUG, "ok")
