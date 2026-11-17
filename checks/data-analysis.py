"""Checks for data-analysis."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
slug = "data-analysis"
text = (root / "research/content" / f"{slug}.md").read_text()
cites = re.findall(r"\{{cite:([a-z0-9_]+)\}}", text)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2
for link in ("histogram.qmd", "line-chart.qmd", "summary-statistics.qmd", "scatterplot.qmd"):
    assert link in text, link

print(slug, "ok")
