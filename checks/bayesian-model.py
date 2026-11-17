"""Checks for the bayesian-model page."""
import re
from fractions import Fraction as F
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/bayesian-model.md").read_text(encoding="utf-8")
cites = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
headings = [line[3:].split("—")[0].strip() for line in prose.splitlines() if line.startswith("## ")]
assert headings == ["Lead context", "Motivating example", "Definition", "Properties", "Worked example", "Assumptions and limits", "History"], headings
assert "**Your turn.**" in prose
assert 'collapse="true" title="Answer"' in prose
hidden = re.findall(r'title="Answer"\}(.*?)\n:+', prose, flags=re.S)
assert hidden
for block in hidden:
    assert "{cite:" not in block
assert "## Check yourself" not in prose
banned = ("not a claim", "not claimed", "this page", "Dodge states", "the manual", "question bank", "letter opener", "Wikipedia", "Grokipedia")
for phrase in banned:
    assert phrase.lower() not in prose.lower(), phrase

assert F(1, 2) * F(1, 5) == F(1, 10)
assert F(1, 2) * F(4, 5) == F(2, 5)
assert F(1, 10) + F(2, 5) == F(1, 2)
assert F(1, 10) / F(1, 2) == F(1, 5)
assert F(2, 5) / F(1, 2) == F(4, 5)
assert abs((1 / 2) * 0.8 - 0.4) < 1e-12
assert abs(0.4 / 0.5 - 0.8) < 1e-12

print("bayesian-model:", len(cites), "cites")
