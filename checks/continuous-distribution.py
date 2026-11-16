"""Check density normalisation, interval probabilities and mixed-law numbers."""

from fractions import Fraction as Q
from math import isclose, exp
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/continuous-distribution.qmd").read_text()
body = page.split("## See also", 1)[0]

# Baseline cubic CDF and uniform-interval examples.
assert Q(3, 4)**3 - Q(1, 2)**3 == Q(19, 64)
assert 3 * Q(1, 4) == Q(3, 4)
assert Q(3, 4) - Q(1, 3) == Q(5, 12)
assert 1 - Q(1, 2) * Q(1, 2) * Q(1, 2) == Q(7, 8)

# New density f(x)=(1+x)/4 on (0,2).
F = lambda x: (x + x*x/2) / 4
assert F(0) == 0 and F(2) == 1
assert F(1.5) == 2.625 / 4 and F(.5) == .625 / 4
assert F(1.5) - F(.5) == .5
assert isclose((2 + 8/3) / 4, 7/6)
assert round(7/6, 4) == 1.1667
assert (1 + 1)/4 == .5
assert 4 * (.15 - .10) == .2 or isclose(4 * (.15 - .10), .2)

# Mixed atom plus continuous uniform component.
assert isclose(.8 * (.75 - .25), .4)
assert isclose(.8 + .2, 1)
assert isclose(exp(-.5) - exp(-1.6), .40463414171797807, rel_tol=1e-10)

for fragment in (
    "## Motivating example", "## Worked example", "**Your turn.**",
    'title="Proof"', 'title="Answer"', "## Common misconceptions",
    "prob-continuous-densities.png", "prob-02-random-variables-distribution-function.png",
    "19/64", "5/12", "7/8", "7/6", "1.1667", "0.4", "## Assumptions and limits",
):
    assert fragment in body, f"Missing section, figure or calculation: {fragment}"
assert body.count('title="Proof"') == 1
for qid in ("ex-prob-cubic-cdf", "ex-prob-uniform-interval"):
    assert f"../questions/{qid}.qmd" in page
print("continuous-density, baseline and mixed-law calculations passed")
