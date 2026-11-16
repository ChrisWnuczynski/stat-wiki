"""Check dispersion formulas and all page examples against generated text."""

import math
from fractions import Fraction as F
from pathlib import Path


root = Path(__file__).resolve().parents[1]
page = (root / "articles/dispersion-parameter.qmd").read_text()
body = page.split("## See also", 1)[0]


def gamma_moments(shape, rate):
    return shape / rate, shape / rate**2


# Motivating and interpreted Gamma examples; Gamma uses shape and rate.
shape = F(3)
phi = 1 / shape
assert gamma_moments(shape, F(1, 2)) == (6, 12)
assert gamma_moments(shape, F(1, 4)) == (12, 48)
assert 48 / 12 == 4
assert round(math.sqrt(12), 3) == 3.464
assert round(math.sqrt(48), 3) == 6.928
assert round(math.sqrt(float(phi)), 3) == .577
assert F(1, 3) * 6**2 == 12
assert math.sqrt(2) > 1

# Intercept-only count fit and Pearson dispersion, with p=1.
counts = (1, 3, 5, 7)
mu = F(sum(counts), len(counts))
assert mu == 4
ss = sum((F(y) - mu) ** 2 for y in counts)
assert ss == 20
pearson = ss / mu
assert pearson == 5
assert len(counts) - 1 == 3
estimated_phi = pearson / 3
assert estimated_phi == F(5, 3)
assert round(float(estimated_phi), 3) == 1.667
assert round(float(ss / 3), 3) == 6.667
assert 1 / math.sqrt(sum(counts)) == .25
assert round(math.sqrt(float(estimated_phi)) / 4, 3) == .323

# Hidden practice calculation.
practice = (2, 2, 8, 8)
practice_mean = F(sum(practice), len(practice))
assert practice_mean == 5
practice_ss = sum((F(y) - practice_mean) ** 2 for y in practice)
assert practice_ss == 36
assert practice_ss / practice_mean == F(36, 5)
assert (practice_ss / practice_mean) / 3 == F(12, 5)
assert round(math.sqrt(F(12, 5)), 3) == 1.549
assert F(12, 5) * 5 == 12

# Inherited answered bank examples: quasi-Poisson SE and Gamma link.
assert math.sqrt(4) * .10 == .20
assert round(math.exp(-.08), 4) == .9231
assert round(100 * (1 - math.exp(-.08)), 2) == 7.69

for printed in (
    "$6$", "$12$", "$1$", "$2$", "$\\sqrt2$", "$\\phi>0$",
    "$\\phi=\\sigma^2$", "$\\phi=1$", "$\\phi=1/\\alpha$",
    "$3/6=0.5$", "=12", "$48$", "\\approx3.464", "\\approx6.928", "\\approx0.577",
    "$1,3,5,7$", "$\\hat\\mu=(1+3+5+7)/4=4$", "20/4=5$",
    "$n-p=4-1=3$", "5/3\\approx1.667$", "$20/3\\approx6.667$",
    "$1/\\sqrt{16}=0.25$", "\\approx0.323", "$2,2,8,8$", "$4(3^2)=36$",
    "36/5=7.2$", "12/5=2.4$", "\\approx1.549", "\\hat\\mu=12$",
):
    assert printed in body, f"Missing printed calculation {printed}"

assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
assert "shape $1/\\phi$ and rate $1/(\\phi\\mu_i)$" in body
for qid in ("q-47", "q-55"):
    assert f"../questions/{qid}.qmd" in page
assert 'data-cite-key="mccullagh1992_glm_intro"' in body
assert 'data-cite-key="rstats_summary_glm2026"' in body
print("dispersion Gamma, Pearson, practice and inherited examples passed")
