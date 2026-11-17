"""Checks for the apriori-algorithm research page."""
import re
from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/apriori-algorithm.md").read_text(encoding="utf-8")
cites = re.findall(r"\{\{cite:([a-z0-9_]+)\}\}", prose)
assert len(cites) >= 5, cites
assert len(set(cites)) >= 2, set(cites)
headings = [line[3:].split("—")[0].strip() for line in prose.splitlines() if line.startswith("## ")]
assert headings == ["Lead context", "Motivating example", "Intuition", "Definition", "Statistical use", "Worked example", "Common misconceptions", "Connections"], headings
assert "## Motivating example" in prose and "## Worked example" in prose
assert "**Your turn.**" in prose
assert '::: {.callout-tip collapse="true" title="Answer"}' in prose
answer = re.search(
    r'::: \{\.callout-tip collapse="true" title="Answer"\}(.*?):::',
    prose,
    re.S,
)
assert answer and "{cite:" not in answer.group(1)
assert "## Check yourself" not in prose
banned = ("not a claim", "not claimed", "this page", "Dodge states", "the manual", "question bank", "letter opener", "Wikipedia", "Grokipedia")
for phrase in banned:
    assert phrase.lower() not in prose.lower(), phrase

support_ab = Fraction(2, 4)
support_a = Fraction(3, 4)
support_b = Fraction(3, 4)
support_bc = Fraction(1, 4)
confidence_a_to_b = support_ab / support_a
lift = confidence_a_to_b / support_b
assert support_ab == Fraction(1, 2)
assert confidence_a_to_b == Fraction(2, 3)
assert lift == Fraction(8, 9)
assert support_bc == Fraction(1, 4)
assert support_a > Fraction(2, 5) and support_b > Fraction(2, 5)
assert not support_bc > Fraction(2, 5)
assert "2/3" in prose and "8/9" in prose and "1/4" in prose

print("apriori-algorithm checks passed")
