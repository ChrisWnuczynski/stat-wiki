"""Checks for the parametric-statistics field page."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "parametric-statistics"
prose = (root / f"research/content/{slug}.md").read_text(encoding="utf-8")
cites = re.findall(r"{{cite:([a-z0-9_]+)}}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
assert "maximum-likelihood.qmd" in prose

print(slug, "ok")
