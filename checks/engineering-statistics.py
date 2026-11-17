"""Checks for the engineering-statistics field page."""
import json, re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/engineering-statistics.md").read_text()
cites = re.findall(r"\{cite:([^}]+)\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
print("engineering-statistics:", len(cites), "cites,", len(set(cites)), "keys")
