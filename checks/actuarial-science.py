"""Checks for the actuarial-science field page."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/actuarial-science.md").read_text(encoding="utf-8")
cites = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
headings = [line[3:].split("—")[0].strip() for line in prose.splitlines() if line.startswith("## ")]
assert headings == ["Lead context", "Definition", "Interpretation", "Statistical use", "History", "Connections"], headings
assert "**Your turn.**" not in prose
assert "## Check yourself" not in prose
assert len(prose.split()) >= 1000
banned = ("not a claim", "not claimed", "this page", "Dodge states", "the manual", "question bank", "letter opener", "Wikipedia", "Grokipedia")
low = prose.lower()
for phrase in banned:
    assert phrase.lower() not in low, phrase
assert abs((1040 / 1.04) * 0.01 - 10) < 1e-9
assert abs(0.01 * 1040 - 10.40) < 1e-9

print("actuarial-science:", len(cites), "cites,", len(set(cites)), "keys")
