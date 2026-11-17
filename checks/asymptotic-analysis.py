"""Checks for the asymptotic-analysis field page."""
import re
from math import comb
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/asymptotic-analysis.md").read_text(encoding="utf-8")
cites = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
assert "hansen2010" not in cites
headings = [line[3:].split("—")[0].strip() for line in prose.splitlines() if line.startswith("## ")]
assert headings == ["Lead context", "Definition", "Statistical use", "Common misconceptions", "Connections", "History"], headings
assert "**Your turn.**" not in prose
assert "## Check yourself" not in prose
assert len(prose.split()) >= 1000
for match in re.finditer(r"\{\{cite:openintro2019\}\}\s*\(([^)]*)\)", prose):
    assert not re.search(r"\bp\.", match.group(1)), match.group(1)
banned = ("not a claim", "not claimed", "this page", "Dodge states", "the manual", "question bank", "letter opener", "Wikipedia", "Grokipedia")
for phrase in banned:
    assert phrase.lower() not in prose.lower(), phrase

assert (27 - 20) / 4 == 1.75
assert (27 - 0.5 - 20) / 4 == 1.625
assert abs((1 - 0.9599) - 0.0401) < 1e-12
exact = sum(comb(100, k) * (0.2) ** k * (0.8) ** (100 - k) for k in range(27, 101))
assert abs(exact - 0.0558) < 5e-5
assert 20 >= 10 and 80 >= 10

print("asymptotic-analysis:", len(cites), "cites")
