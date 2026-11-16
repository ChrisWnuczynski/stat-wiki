"""Check numerical and structural claims in the identifiability page."""

from math import exp, pi, sqrt
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/identifiability.qmd").read_text()
body = page.split("## See also", 1)[0]

phi = lambda z: exp(-z * z / 2) / sqrt(2 * pi)
for x, shown in ((0, .157476), (2, .295457)):
    density = .3 * phi(x) + .7 * phi(x - 2)
    swapped = .7 * phi(x - 2) + .3 * phi(x)
    assert density == swapped
    assert round(density, 6) == shown

assert (10 - 2, 10 + 3) == (8, 13)
assert (15 - 7, 15 - 2) == (8, 13)
assert (8 + 0, 8 + 5) == (8, 13)
assert 13 - 8 == 5
assert 4 / (1 - .5**2) == 16 / 3
assert .5**2 == (-.5)**2 == .25
assert (2 - 1, 2 + 0, 2 + 1) == (1, 2, 3)
assert (5 - 4, 5 - 3, 5 - 2) == (1, 2, 3)
assert (.2 * .5, .5 * .2) == (.1, .1)

for fragment in (
    "## Motivating example", "## Worked example", "**Your turn.**",
    'title="Proof"', 'title="Answer"', "0.157476", "0.295457",
    "16/3", "-7,-2", "## Common misconceptions", "#assumptions-and-limits",
):
    assert fragment in body, f"Missing section or calculation: {fragment}"
assert body.count('title="Proof"') == 1
for link in ("../notes/inf-15-two-factor-anova.qmd", "label-switching.qmd", "../questions/c-26.qmd"):
    assert link in page
print("identifiability mixture, rank and contrast calculations passed")
