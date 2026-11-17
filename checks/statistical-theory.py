"""Checks for the statistical-theory field page."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "statistical-theory"
prose = (root / f"research/content/{slug}.md").read_text(encoding="utf-8")
pending = json.loads((root / f"research/pending/{slug}.json").read_text(encoding="utf-8"))
cites = re.findall(r"{{cite:([a-z0-9_]+)}}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
assert "**Your turn.**" not in prose
assert "## Check yourself" not in prose
assert "self_checks" not in pending
assert "loss-and-risk.qmd" in prose
assert pending["kind"] == "field"

print(slug, "ok")
