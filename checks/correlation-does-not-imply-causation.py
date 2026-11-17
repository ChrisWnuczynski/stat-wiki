"""Checks for the correlation-does-not-imply-causation research page."""
import re
from fractions import Fraction
from pathlib import Path

root = Path(__file__).resolve().parents[1]
prose = (root / "research/content/correlation-does-not-imply-causation.md").read_text(encoding="utf-8")
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
assert 7 * 7 - 3 * 13 == 10
assert Fraction(7, 13) - Fraction(3, 7) == Fraction(10, 91)
assert Fraction(10, 20) - Fraction(10, 20) == 0
assert Fraction(8, 20) - Fraction(12, 20) == Fraction(-1, 5)
print("correlation-does-not-imply-causation checks passed")
