"""Checks for the epidemiology field page."""
import json, re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/epidemiology.md").read_text()
cites = re.findall(r"\{cite:([^}]+)\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
print("epidemiology:", len(cites), "cites,", len(set(cites)), "keys")
