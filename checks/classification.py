"""Checks for the classification research page."""
import re
from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/classification.md").read_text(encoding="utf-8")
cites = re.findall(r"\{\{cite:([^}]+)\}\}", prose)
assert len(cites) >= 5, cites
assert len(set(cites)) >= 2, set(cites)
found = []
for line in prose.splitlines():
    if line.startswith("## "):
        found.append(line[3:].split(" — ")[0].strip())
assert found == [
    'Lead context',
    'Motivating example',
    'Intuition',
    'Definition',
    'Statistical use',
    'Worked example',
    'Common misconceptions',
    'Connections',
], found
assert "## Check yourself" not in prose
assert "**Your turn.**" in prose
assert '::: {.callout-tip collapse="true" title="Answer"}' in prose
answer = re.search(
    r'::: \{\.callout-tip collapse="true" title="Answer"\}(.*?):::',
    prose,
    re.S,
)
assert answer and "{cite:" not in answer.group(1)
probs = (Fraction(7, 10), Fraction(1, 5), Fraction(1, 10))
assert sum(probs) == 1
bayes = max(probs)
assert 1 - bayes == Fraction(3, 10)
assert 1 - probs[1] == Fraction(4, 5)
pair = (Fraction(11, 20), Fraction(9, 20))
assert sum(pair) == 1
assert 1 - max(pair) == Fraction(9, 20)
assert "3/10" in prose and "4/5" in prose and "9/20" in prose
print("classification checks passed")
