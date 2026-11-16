"""Validate new Poisson examples and preserved rare-fault comparison."""

from math import exp, factorial, isclose
from pathlib import Path
from scipy.stats import binom, poisson

page = (Path(__file__).resolve().parents[1] / "articles/poisson-distribution.qmd").read_text()
body = page.split("## See also", 1)[0]

pmf = lambda k, lam: exp(-lam) * lam ** k / factorial(k)
assert isclose(sum(pmf(k, 1) for k in range(30)), 1)
assert 4 * (1 / 4) == 1
assert round(pmf(0, 1), 4) == .3679
assert round(1 - pmf(0, 1) - pmf(1, 1), 4) == .2642
assert isclose(1 - pmf(0, 1) - pmf(1, 1), 1 - 2 * exp(-1))

assert (1 + 9) / 2 == 5
assert ((1 - 5) ** 2 + (9 - 5) ** 2) / 2 == 16
assert 5 + 16 == 21
assert 2 * (3 / 2) == 3
assert round(pmf(0, 3) + pmf(1, 3), 4) == .1991
assert isclose(pmf(0, 3) + pmf(1, 3), 4 * exp(-3))
assert .5 * (1 - .5) == .25 < .5

assert round(binom.cdf(1, 1000, .002), 4) == .4057
assert round(poisson.cdf(1, 2), 4) == .4060
assert round(pmf(3, 2), 4) == .1804

for printed in (
    "4(1/4)=1", "0.3679", "0.2642", "1-2e^{-1}", "5+16=21",
    "N(3/2)", "4e^{-3}", "0.1991", "1/2", "1/4", "0.4057", "0.4060",
    "0,1,2", "1/\\sqrt", "1/\\lambda",
):
    assert printed in body, f"Missing displayed value: {printed}"
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
assert page.count("![") >= 3
for key in ("siegrist2022_poisson_distribution", "nist_handbook2002", "dodge2008", "rstats_glm2026"):
    assert f'data-cite-key="{key}"' in body
print("Poisson probabilities, dispersion examples and preserved content passed")
