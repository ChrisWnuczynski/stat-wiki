"""Checks for the data-analysis research page."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/data-analysis.md").read_text(encoding="utf-8")
cites = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(cites) >= 5, cites
assert len(set(cites)) >= 2, set(cites)
found = []
for line in prose.splitlines():
    if line.startswith("## "):
        found.append(line[3:].split(" — ")[0].strip())
assert found == [
    'Lead context',
    'Definition',
    'Properties',
    'History',
    'Connections',
], found
assert "## Check yourself" not in prose
assert "**Your turn.**" not in prose
words = re.findall(r"[A-Za-z0-9$\\]+(?:'[A-Za-z]+)?", prose)
assert len(words) >= 1000, len(words)
for link in ("histogram.qmd", "line-chart.qmd", "summary-statistics.qmd", "scatterplot.qmd"):
    assert link in prose, link
print("data-analysis checks passed")
