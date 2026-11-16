"""Numerical identities and rendered-content checks for natural parameters."""

from math import exp, isclose, log
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/natural-parameter.qmd").read_text()
body = page.split("## See also", 1)[0]

p = .20
odds = p / (1 - p)
eta = log(odds)
A = log(1 + exp(eta))
assert isclose(odds, .25)
assert round(eta, 6) == -1.386294
assert round(A, 6) == .223144
assert isclose(exp(eta - A), .20)
assert isclose(exp(-A), .80)
assert isclose(exp(eta) / (1 + exp(eta)), .20)
assert isclose(p * (1 - p), .16)

lam = 4
poisson_eta = log(lam)
assert round(poisson_eta, 6) == 1.386294
assert round(2 * poisson_eta, 6) == 2.772589
assert isclose(exp(poisson_eta), 4)
assert isclose(exp((2 * poisson_eta) / 2), 4)

for fragment in (
    "## Motivating example", "## Worked example", "**Your turn.**",
    'title="Proof"', 'title="Answer"', "1/4", "-1.386294", "0.223144",
    "0.20(0.80)=0.16", "2.772589", "## Common misconceptions",
    "#assumptions-and-limits",
):
    assert fragment in body, f"Missing calculation or section: {fragment}"

assert body.count('title="Proof"') == 1
for qid in ("q-57", "c-04", "c-17"):
    assert f"../questions/{qid}.qmd" in page
print("natural-parameter Bernoulli and Poisson calculations passed")
