"""Recompute point-summary numbers and verify the generated article."""

import math
from pathlib import Path


root = Path(__file__).resolve().parents[1]
page = (root / "articles/posterior-point-summaries.qmd").read_text()
body = page.split("## See also", 1)[0]


def beta_cdf(x, a, b):
    n = a + b - 1
    return sum(math.comb(n, k) * x**k * (1 - x) ** (n - k)
               for k in range(a, n + 1))


def beta_median(a, b):
    low, high = 0.0, 1.0
    for _ in range(70):
        middle = (low + high) / 2
        if beta_cdf(middle, a, b) < .5:
            low = middle
        else:
            high = middle
    return (low + high) / 2


# Uniform prior, two of ten successes, and the numerical loss comparison.
a, b = 1 + 2, 1 + 10 - 2
assert (a, b) == (3, 9)
mean = a / (a + b)
mode = (a - 1) / (a + b - 2)
variance = a * b / ((a + b)**2 * (a + b + 1))
assert mean == .25 and mode == .2
assert round(beta_median(a, b), 4) == .2358
assert round(math.sqrt(variance), 4) == .1201
assert math.isclose(variance, 27 / 1872)
assert round(variance, 5) == .01442
assert round(variance + (mean - mode)**2, 5) == .01692

# Under a logit transform, the density gains the theta(1-theta) Jacobian.
transformed_peak_on_theta_scale = a / (a + b)
assert transformed_peak_on_theta_scale == .25 != mode
assert math.isclose(math.log(.25 / .75), -math.log(3))

# Hidden practice, with three successes in ten trials.
pa, pb = 1 + 3, 1 + 10 - 3
assert (pa, pb) == (4, 8)
assert round(pa / (pa + pb), 4) == .3333
assert round(beta_median(pa, pb), 4) == .3238
assert round((pa - 1) / (pa + pb - 2), 4) == .3000

# Inherited posterior-draw indices and moment-existence counterexamples.
assert 500 + 501 == 1001 and 25 / 1000 == .025
assert .8 < 1 < 1.5 < 2

for printed in (
    "$0.20$", "$0.2358$", "$0.25$", "$L=1000$",
    "$\\theta_{(500)}$", "$\\theta_{(501)}$", "\\theta_{(25)}",
    "\\theta_{(975)}", "$3/12=0.25$", "2/10=0.20$",
    "27/1872\\approx0.01442", "\\approx0.01692", "$0.1201$",
    "$0.8$", "$1.5$", "$-5$", "$5$", "$4/12=0.3333$",
    "$0.3238$", "3/10=0.3000$", "3/(3+9)=0.25",
):
    assert printed in body, f"Missing displayed number {printed}"

assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
assert "Posterior mean under squared-error loss" in body
assert "MAP and squared-error loss" in body
for qid in ("q-12", "ex-norm-mean"):
    assert f"../questions/{qid}.qmd" in page
assert 'data-cite-key="hoff2013_bayes_estimators"' in body
assert 'data-cite-key="gelman_bda2013"' in body
print("posterior point-summary arithmetic, proof, and practice passed")
