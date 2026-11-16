"""Recompute every numerical illustration in the overdispersion article."""

from fractions import Fraction as F
from math import isclose, sqrt
from pathlib import Path

root = Path(__file__).resolve().parents[1]
body = (root / "articles/overdispersion.qmd").read_text().split("## See also", 1)[0]

# Intercept-only five-night example.
counts = (0, 0, 1, 3, 6)
n = len(counts)
mu = F(sum(counts), n)
ss = sum((F(y) - mu) ** 2 for y in counts)
pearson = ss / mu
phi = pearson / (n - 1)
assert (n, mu, ss, pearson, n - 1, phi, ss / (n - 1)) == (5, 2, 26, 13, 4, F(13, 4), F(13, 2))
assert round(1 / sqrt(sum(counts)), 3) == .316
assert round(sqrt(float(phi)) / sqrt(sum(counts)), 3) == .570

# Hidden practice example.
practice = (0, 1, 1, 6)
pmu = F(sum(practice), len(practice))
pss = sum((F(y) - pmu) ** 2 for y in practice)
assert (pmu, pss, pss / pmu, pss / pmu / 3) == (2, 22, 11, F(11, 3))
assert round(float(F(11, 3)), 3) == 3.667

# Two-group mixture, each group conditionally Poisson.
group_means = (1, 5)
pooled = F(sum(group_means), 2)
between = sum((F(m) - pooled) ** 2 for m in group_means) / 2
variance = pooled + between
assert (pooled, between, variance, variance / pooled) == (3, 4, 7, F(7, 3))

# Distributional identities printed on the page.
lam, k = F(2), F(4)
assert lam**2 + lam - lam**2 == lam
assert lam + lam**2 / k == 3 > lam
assert isclose(sqrt(3.25) * 1 / sqrt(10), .5700877125, rel_tol=1e-9)

for fragment in (
    "0,0,1,3,6", "26/2=13", "13/4=3.25", "26/4=6.5", "0.316", "0.570",
    "0,1,1,6", "22/2=11", "11/3\\approx3.667", "7/3",
    "G'(1)=\\lambda", "G''(1)=\\lambda^2", "title=\"Proof\"",
    "## Motivating example", "## Worked example", "**Your turn.**",
    "## Common misconceptions", "## When the diagnosis misleads {#assumptions-and-limits}",
):
    assert fragment in body, f"Missing content or calculation: {fragment}"
assert body.count('title="Proof"') == 1
assert 'title="Answer"' in body
for qid in ("q-47", "q-54"):
    assert f"../questions/{qid}.qmd" in (root / "articles/overdispersion.qmd").read_text()
print("overdispersion calculations and preserved question links passed")
