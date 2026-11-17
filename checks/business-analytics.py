"""Checks for the business-analytics field page."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/business-analytics.md").read_text(encoding="utf-8")
cites = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2
assert "informs_analytics" not in cites
assert "davenport2006" in cites and "vidgen2017" in cites
headings = [line[3:].split("—")[0].strip() for line in prose.splitlines() if line.startswith("## ")]
assert headings == ["Lead context", "Definition", "Interpretation", "Statistical use", "History", "Connections"], headings
assert "**Your turn.**" not in prose
assert "## Check yourself" not in prose
assert len(prose.split()) >= 1000
banned = ("not a claim", "not claimed", "this page", "Dodge states", "the manual", "question bank", "letter opener", "Wikipedia", "Grokipedia")
for phrase in banned:
    assert phrase.lower() not in prose.lower(), phrase

print("business-analytics:", len(cites), "cites")
