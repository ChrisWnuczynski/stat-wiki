"""Checks for the chemometrics field page."""
import json, re
from pathlib import Path
root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/chemometrics.md").read_text()
cites = re.findall(r"\{cite:([^}]+)\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2
print("chemometrics:", len(cites), "cites")
