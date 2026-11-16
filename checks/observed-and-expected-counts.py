"""Check the displayed count calculations and preserved article content."""

from fractions import Fraction
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
page = (root / "articles" / "observed-and-expected-counts.qmd").read_text()
body = page.split("## See also", 1)[0]

def pearson(observed, expected):
    return sum((Fraction(o) - e) ** 2 / e for o, e in zip(observed, expected))

observed = (24, 16, 22, 18)
expected = (Fraction(80, 4),) * 4
assert sum(observed) == sum(expected) == 80
assert tuple(o - e for o, e in zip(observed, expected)) == (4, -4, 2, -2)
assert pearson(observed, expected) == 2

practice = (18, 22, 25, 15)
assert sum(practice) == 80
assert tuple(o - e for o, e in zip(practice, expected)) == (-2, 2, 5, -5)
assert pearson(practice, expected) == Fraction(29, 10)

table = ((30, 10), (20, 40))
rows = tuple(map(sum, table))
columns = tuple(map(sum, zip(*table)))
fitted = tuple(tuple(Fraction(r * c, 100) for c in columns) for r in rows)
assert fitted == ((20, 20), (30, 30))
assert tuple(map(sum, fitted)) == rows
assert tuple(map(sum, zip(*fitted))) == columns

for printed in (
    "$80(1/4)=20$", "$23.25$", "$4,-4,2,-2$", "$T=40/20=2$",
    "$4-1=3$", "$-2,2,5,-5$", "$T=58/20=2.9$", "$\\chi^2_3$",
):
    assert printed in body, f"Missing printed value: {printed}"

assert '$\\pi_i$ are fully specified' in body
assert body.count('title="Proof"') == 1
assert body.count('title="Answer"') >= 3
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body
assert "## Check yourself" in body
assert all(key in body for key in (
    'data-cite-key="nist_chi_square_gof2002"',
    'data-cite-key="nist_contingency2002"',
    'data-cite-key="gorroochurn2016_pearson"',
))
questions = set(re.findall(r"\.\./questions/([^.)#]+)\.qmd", page))
assert len(questions) >= 13, f"Expected at least 13 preserved question links, got {len(questions)}"
assert {"ex-inf-frizzle", "ex-inf-die-fairness"} <= questions
print("observed-and-expected-counts arithmetic, sources, proof, and links passed")
