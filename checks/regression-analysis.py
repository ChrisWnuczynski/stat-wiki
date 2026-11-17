"""Checks for the regression-analysis field page."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "regression-analysis"
prose = (root / f"research/content/{slug}.md").read_text(encoding="utf-8")
cites = re.findall(r"{{cite:([a-z0-9_]+)}}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
assert "simple-linear-regression.qmd" in prose
assert "ordinary-least-squares.qmd" in prose

print(slug, "ok")
