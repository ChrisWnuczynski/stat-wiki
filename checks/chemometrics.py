"""Checks for the chemometrics field page."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/chemometrics.md").read_text(encoding="utf-8")
cites = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2
assert "kumar2021" in cites and "otto2024" in cites
headings = [line[3:].split("—")[0].strip() for line in prose.splitlines() if line.startswith("## ")]
assert headings == ["Lead context", "Intuition", "Definition", "Statistical use", "Assumptions and limits", "History"], headings
assert "**Your turn.**" not in prose
assert "## Check yourself" not in prose
assert len(prose.split()) >= 1000
for match in re.finditer(r"\{\{cite:[^}]+\}\}\s*\(([^)]*)\)", prose):
    locator = match.group(1)
    assert "p." in locator or "§" in locator, locator
    assert not re.fullmatch(r"Ch\.\s*\d+", locator.strip()), locator
banned = ("not a claim", "not claimed", "this page", "Dodge states", "the manual", "question bank", "letter opener", "Wikipedia", "Grokipedia")
for phrase in banned:
    assert phrase.lower() not in prose.lower(), phrase

print("chemometrics:", len(cites), "cites")
