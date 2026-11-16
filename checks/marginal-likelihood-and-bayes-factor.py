"""Check printed Bayes-factor values and retained article material."""

from fractions import Fraction
from math import comb, factorial
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
page = (root / "articles" / "marginal-likelihood-and-bayes-factor.qmd").read_text()
body = page.split("## See also", 1)[0]

def beta_integer(a, b):
    return Fraction(factorial(a - 1) * factorial(b - 1), factorial(a + b - 1))

def predictive(x, n, a, b):
    return comb(n, x) * beta_integer(x + a, n - x + b) / beta_integer(a, b)

success_0 = Fraction(1, 2)
success_1 = predictive(1, 1, 2, 1)
assert success_1 == Fraction(2, 3)
assert success_1 / success_0 == Fraction(4, 3)
assert Fraction(4, 3) * Fraction(3, 7) == Fraction(4, 7)
assert Fraction(4, 7) / (1 + Fraction(4, 7)) == Fraction(4, 11)

failure_0 = Fraction(1, 2)
failure_1 = predictive(0, 1, 2, 1)
assert failure_1 == Fraction(1, 3)
assert failure_1 / failure_0 == Fraction(2, 3)
assert Fraction(2, 3) * Fraction(3, 7) == Fraction(2, 7)
assert Fraction(2, 7) / (1 + Fraction(2, 7)) == Fraction(2, 9)

# Inherited binomial-count example: n=3, x=3, uniform alternative.
assert comb(3, 3) * Fraction(1, 2) ** 3 == Fraction(1, 8)
assert predictive(3, 3, 1, 1) == Fraction(1, 4)
assert Fraction(1, 4) / Fraction(1, 8) == 2

for printed in (
    "$4/3$", "$m_0(1)=1/2$", "$m_1(1)=2/3$",
    "$\\operatorname{BF}_{10}=(2/3)/(1/2)=4/3$",
    "$(4/3)(3/7)=4/7$", "=4/11\\approx0.3636",
    "$m_0(0)=1/2$", "$m_1(0)=1-\\mathbb E(p)=1/3$",
    "$\\operatorname{BF}_{10}=(1/3)/(1/2)=2/3$",
    "$(2/3)(3/7)=2/7$", "=2/9\\approx0.2222",
):
    assert printed in body, f"Missing printed value: {printed}"

assert "## Motivating example" in body
assert "**Your turn.**" in body
assert body.count('title="Proof"') == 1
assert body.count('title="Answer"') >= 3
assert "## Check yourself" in body
assert 'data-cite-key="kass_raftery1995"' in body
questions = set(re.findall(r"\.\./questions/([^.)#]+)\.qmd", page))
assert {"q-11", "ex-battery-bf", "q-44", "c-08"} <= questions
print("marginal-likelihood-and-bayes-factor printed values, proof, practice, and links passed")
