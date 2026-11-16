"""Check printed conditional proportions and retained article material."""

from fractions import Fraction
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
page = (root / "articles" / "conditional-probability.qmd").read_text()
body = page.split("## See also", 1)[0]

cars = ((40, 10), (20, 30))
assert sum(map(sum, cars)) == 100
assert Fraction(cars[0][0], sum(cars[0])) == Fraction(4, 5)
assert Fraction(cars[0][0], cars[0][0] + cars[1][0]) == Fraction(2, 3)

journeys = ((18, 22), (12, 148))
assert sum(map(sum, journeys)) == 200
assert Fraction(18, 40) == Fraction(45, 100)
assert Fraction(18, 30) == Fraction(60, 100)
assert Fraction(18, 200) == Fraction(9, 100)
assert Fraction(12, 160) == Fraction(75, 1000)

practice = ((15, 30), (15, 60))
assert sum(map(sum, practice)) == 120
assert Fraction(15, 45) == Fraction(1, 3)
assert Fraction(15, 30) == Fraction(1, 2)
assert Fraction(15, 75) == Fraction(1, 5)

for printed in (
    "$40/50=4/5$", "$40/60=2/3$", "$18/40=0.45$",
    "$18/30=0.60$", "$18/200=0.09$", "$12/160=0.075$",
    "=15/45=1/3", "=15/30=1/2", "=15/75=1/5",
    "$\\mathbb{P}(A\\mid B)=2/3$", "\\frac{5}{10}\\times\\frac{4}{9}\\times\\frac{3}{8}=\\frac{1}{12}",
):
    assert printed in body, f"Missing printed value: {printed}"

assert "## Motivating example" in body
assert "**Your turn.**" in body
assert body.count('title="Proof"') == 1
assert body.count('title="Answer"') >= 3
assert "## Check yourself" in body
assert "prob-01-experiments-total-probability.png" in page
for key in ("grinstead_snell1997", "dodge2008"):
    assert f'data-cite-key="{key}"' in body, key
questions = set(re.findall(r"\.\./questions/([^.)#]+)\.qmd", page))
assert {"ex-prob-second-die", "ex-prob-binary-channel", "q-22", "c-37"} <= questions
print("conditional-probability printed values, proof, practice, and links passed")
