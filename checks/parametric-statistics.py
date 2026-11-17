"""Checks for parametric-statistics."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "parametric-statistics"
prose = (root / "research/content" / f"{slug}.md").read_text(encoding="utf-8")
works = json.loads((root / "bibliography.json").read_text(encoding="utf-8"))["works"]
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
for key in set(cites):
    assert key in works, key
assert "**Your turn.**" not in prose
assert "## Check yourself" not in prose
assert "maximum-likelihood.qmd" in prose
heads = re.findall(r"^## (.+)$", prose, re.M)
assert heads == [
    "Lead context",
    "Intuition",
    "Definition",
    "Statistical use",
    "Assumptions and limits",
    "History",
]
assert len(prose.split()) >= 1000
assert "p. 372, nonlinear in the parameters" not in prose
print(slug, "ok")
