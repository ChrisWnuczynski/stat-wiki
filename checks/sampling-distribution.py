"""Check the sampling-distribution article."""
import re
from pathlib import Path
root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/sampling-distribution.md").read_text(encoding="utf-8")
page = (root / "articles/sampling-distribution.qmd").read_text(encoding="utf-8")
keys = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(keys) >= 5 and len(set(keys)) >= 2, keys
assert "## Motivating example" in prose and "**Your turn.**" in prose
assert "## Check yourself {#check-yourself}" in page
assert (1.5+2+2.5)/3 == 2
assert (1+2+3)/3 == 2
