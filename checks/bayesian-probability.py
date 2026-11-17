"""Checks for the bayesian-probability page."""
import re
from fractions import Fraction as F
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/bayesian-probability.md").read_text(encoding="utf-8")
cites = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(cites) >= 5, len(cites)
assert len(set(cites)) >= 2, set(cites)
headings = [line[3:].split("—")[0].strip() for line in prose.splitlines() if line.startswith("## ")]
assert headings == ["Lead context", "Motivating example", "Intuition", "Definition", "Statistical use", "Worked example", "Common misconceptions", "Connections"], headings
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

def price(odds):
    return F(1, odds + 1)

assert price(10) == F(1, 11)
assert price(3) == F(1, 4)

print("bayesian-probability:", len(cites), "cites")
