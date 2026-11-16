"""Check the Bernoulli and Poisson GLM illustrations against the page."""

from fractions import Fraction as F
from math import exp, log
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/three-components-of-a-glm.qmd").read_text()
body = page.split("## See also", 1)[0]

# Worked Bernoulli example.
beta0, beta1 = 0, log(3)
eta0, eta1 = beta0, beta0 + beta1
p0, p1 = F(1, 2), F(3, 4)
assert exp(eta0) / (1 + exp(eta0)) == float(p0)
assert abs(exp(eta1) / (1 + exp(eta1)) - float(p1)) < 1e-12
assert p0 / (1 - p0) == 1
assert p1 / (1 - p1) == 3
assert p1 - p0 == F(1, 4)
assert p1 / p0 == F(3, 2)
assert p0 * (1 - p0) == F(1, 4)
assert p1 * (1 - p1) == F(3, 16)

# Hidden Poisson practice.
poisson0, poisson1 = exp(log(4)), exp(log(4) + log(1.5))
assert abs(poisson0 - 4) < 1e-12
assert abs(poisson1 - 6) < 1e-12
assert abs(poisson1 / poisson0 - 1.5) < 1e-12

for fragment in (
    "## Motivating example", "## Worked example", "**Your turn.**",
    'title="Proof"', 'title="Answer"', "p=3/(1+3)=3/4=0.75",
    "0.75/0.50=1.5", "0.50(0.50)=0.25", "0.75(0.25)=0.1875",
    "4(1.5)=6", "e^{\\beta_1}=1.5", "## Common misconceptions",
    "#assumptions-and-limits",
):
    assert fragment in body, f"Missing calculation or section: {fragment}"

assert body.count('title="Proof"') == 1
assert "../questions/q-40.qmd" in page  # inherited direct question link
print("three GLM components examples and inherited question link passed")
