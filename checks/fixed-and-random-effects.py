"""Numerical checks for fixed and random effects illustrations."""

from fractions import Fraction as F
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/fixed-and-random-effects.qmd").read_text()
body = page.split("## See also", 1)[0]

hospital_means = (F(8), F(10), F(12))
grand = F(10)
n_per_group = 3
tau2, sigma2 = F(4), F(12)
weight = tau2 / (tau2 + sigma2 / n_per_group)
predictions = tuple(grand + weight * (m - grand) for m in hospital_means)
icc = tau2 / (tau2 + sigma2)
assert hospital_means[-1] - hospital_means[0] == 4
assert sigma2 / n_per_group == 4
assert weight == F(1, 2)
assert predictions == (9, 10, 11)
assert predictions[-1] - predictions[0] == 2
assert icc == F(1, 4)
assert tau2 + sigma2 == 16

# Practice: two observations, common mean ten, mean six.
practice_tau2, practice_sigma2, practice_n = F(4), F(8), 2
practice_weight = practice_tau2 / (practice_tau2 + practice_sigma2 / practice_n)
assert practice_weight == F(1, 2)
assert grand + practice_weight * (6 - grand) == 8
assert practice_tau2 / (practice_tau2 + practice_sigma2) == F(1, 3)

# Three-group equicorrelation eigenvalues at the inherited boundary.
rho = F(1, 2)
assert (1 + rho, 1 + rho, 1 - 2 * rho) == (F(3, 2), F(3, 2), 0)

for fragment in (
    "## Motivating example", "## Worked example", "**Your turn.**",
    'title="Proof"', 'title="Answer"', "12-8=4", "12/3=4", "w=4/(4+4)=1/2",
    "(8-10)=9", "(12-10)=11", "4/(4+12)=0.25", "4+12=16",
    "8/2=4", "(6-10)=-2", "4/(4+8)=1/3",
    "## Common misconceptions", "#assumptions-and-limits",
):
    assert fragment in body, f"Missing calculation or section: {fragment}"

assert body.count('title="Proof"') == 1
for qid in ("q-39", "c-35"):
    assert f"../questions/{qid}.qmd" in page
print("fixed/random pooling and correlation calculations passed")
