"""Checks for the environmental-statistics field page."""
import json, re
from pathlib import Path
root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/environmental-statistics.md").read_text()
cites = re.findall(r"\{cite:([^}]+)\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2
print("environmental-statistics:", len(cites), "cites")
