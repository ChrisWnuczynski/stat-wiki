"""Recompute deviance examples and verify the generated article."""

import math
from pathlib import Path


root = Path(__file__).resolve().parents[1]
page = (root / "articles/deviance.qmd").read_text()
body = page.split("## See also", 1)[0]


def poisson_deviance(y, mu):
    assert y >= 0 and mu > 0
    return 2 * ((y * math.log(y / mu) if y else 0) - (y - mu))


# The same raw residual has a different Poisson likelihood discrepancy.
assert 7 - 2 == 55 - 50 == 5
assert poisson_deviance(7, 2) > poisson_deviance(55, 50)

# Worked and hidden practice examples, including the zero convention.
worked = [poisson_deviance(y, mu) for y, mu in zip((0, 3, 5), (1, 2, 4))]
assert [round(v, 6) for v in worked] == [2.000000, .432791, .231436]
assert round(sum(worked), 6) == 2.664226
practice = [poisson_deviance(y, mu) for y, mu in zip((2, 0), (1, 1))]
assert [round(v, 6) for v in practice] == [.772589, 2.000000]
assert round(sum(practice), 6) == 2.772589

# The inherited cholesterol table is internally coherent: same data and two
# coefficients give AIC = residual deviance + 4 for each binomial fit.
for deviance, aic in ((114.04, 118.04), (114.12, 118.12),
                     (111.90, 115.90)):
    assert round(aic - deviance, 2) == 4
assert 100 - 1 == 99 and 100 - 2 == 98
assert 111.90 < 114.04 < 114.12 and 115.90 < 118.04 < 118.12

# Answered model-adequacy bank question.
assert 80 - 1 == 79 and 80 - 3 == 77
assert 410 - 310 == 100 and 100 > 5.99
assert round(310 / 77, 2) == 4.03
try:
    from scipy.stats import chi2
except ImportError:
    pass
else:
    assert round(chi2.ppf(.95, 77), 2) == 98.48

for printed in (
    "$5$", "$2$", "$50$", "$55$", "$7$", "$410$", "$310$",
    "0.432791", "0.231436", "2.664226", "0.772589",
    "2.772589", "137.63", "114.04", "118.04", "114.12",
    "118.12", "111.90", "115.90", "99 df", "98 df",
    "5.99", "98.48", "4.03",
):
    assert printed in body, f"Missing displayed number {printed}"

assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
assert "fig-chol-links" in body
for qid in ("q-34", "c-29"):
    assert f"../questions/{qid}.qmd" in page
for key in ("mccullagh1992_glm_intro", "rstats_family2026", "rstats_glm2026"):
    assert f'data-cite-key="{key}"' in body
print("deviance arithmetic, proof, practice and figure passed")
