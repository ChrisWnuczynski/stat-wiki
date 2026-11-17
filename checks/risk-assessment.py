"""Field-page checks for risk-assessment."""
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
md = (root / "research/content/risk-assessment.md").read_text()
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", md)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
print("risk-assessment checks passed")
