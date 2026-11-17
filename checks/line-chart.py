"""Check the line-chart article."""
import re
from pathlib import Path
root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/line-chart.md").read_text(encoding="utf-8")
page = (root / "articles/line-chart.qmd").read_text(encoding="utf-8")
keys = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(keys) >= 5 and len(set(keys)) >= 2, keys
assert "## Motivating example" in prose and "**Your turn.**" in prose
assert "## Check yourself {#check-yourself}" in page
assert 3/6 == 0.5
