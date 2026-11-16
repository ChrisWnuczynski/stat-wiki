"""Check the Beta interval calculations and preserved article material."""

import math
from statistics import NormalDist
from pathlib import Path


root = Path(__file__).resolve().parents[1]
page = (root / "articles/bayesian-credible-interval.qmd").read_text()
body = page.split("## See also", 1)[0]


def beta_cdf(x, a, b):
    """Integer-shape Beta CDF as a finite binomial sum."""
    n = a + b - 1
    return sum(math.comb(n, k) * x**k * (1 - x) ** (n - k)
               for k in range(a, n + 1))


def beta_quantile(p, a, b):
    low, high = 0.0, 1.0
    for _ in range(80):
        mid = (low + high) / 2
        if beta_cdf(mid, a, b) < p:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def beta_pdf(x, a, b):
    return x ** (a - 1) * (1 - x) ** (b - 1) / math.exp(
        math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b))


# Posterior from Beta(1,1) and two successes in ten trials.
a, b = 1 + 2, 1 + 10 - 2
assert (a, b) == (3, 9)
assert a / (a + b) == .25
assert (a - 1) / (a + b - 2) == .20
l, u = beta_quantile(.025, a, b), beta_quantile(.975, a, b)
assert round(l, 4) == .0602 and round(u, 4) == .5178
assert math.isclose(beta_cdf(l, a, b), .025, abs_tol=1e-12)
assert math.isclose(1 - beta_cdf(u, a, b), .025, abs_tol=1e-12)
assert round(u - l, 4) == .4575


def hpd_error(left):
    right = beta_quantile(beta_cdf(left, a, b) + .95, a, b)
    return beta_pdf(left, a, b) - beta_pdf(right, a, b)


low, high = 0.0, beta_quantile(.05, a, b) - 1e-8
for _ in range(70):
    mid = (low + high) / 2
    if hpd_error(mid) < 0:
        low = mid
    else:
        high = mid
hl = (low + high) / 2
hu = beta_quantile(beta_cdf(hl, a, b) + .95, a, b)
assert round(hl, 4) == .0406 and round(hu, 4) == .4837
assert round(hu - hl, 4) == .4432
assert math.isclose(beta_pdf(hl, a, b), beta_pdf(hu, a, b), abs_tol=1e-10)
assert math.isclose(beta_cdf(hu, a, b) - beta_cdf(hl, a, b), .95, abs_tol=1e-10)
assert hu - hl < u - l

# Practice update with three successes in ten trials.
pa, pb = 1 + 3, 1 + 10 - 3
assert (pa, pb) == (4, 8)
assert round(beta_quantile(.025, pa, pb), 4) == .1093
assert round(beta_quantile(.975, pa, pb), 4) == .6097
assert round(1 - beta_cdf(.5, pa, pb), 4) == .1133

# Inherited draw and question examples.
assert (500 + 501) / 2 == 500.5
assert 25 / 1000 == .025 and 975 / 1000 == .975
assert .6 - .3 == .3
assert math.sqrt(1 / 8) < math.sqrt(7 / 8)
assert 1 - (.5**2) == .75  # q-08's highest-density interval
prior_variance, observation_variance = 225, 100
iq_variance = 1 / (1 / prior_variance + 1 / observation_variance)
iq_mean = iq_variance * (100 / prior_variance + 135 / observation_variance)
iq_sd = math.sqrt(iq_variance)
assert round(iq_variance, 4) == 69.2308
assert round(iq_mean, 4) == 124.2308
assert round(iq_sd, 4) == 8.3205
z975 = NormalDist().inv_cdf(.975)
assert round(iq_mean - z975 * iq_sd, 3) == 107.923
assert round(iq_mean + z975 * iq_sd, 3) == 140.539
post0 = NormalDist(iq_mean, iq_sd).cdf(130)
prior0 = NormalDist(100, 15).cdf(130)
assert round(post0, 4) == .7560
assert round(post0 / (1 - post0), 4) == 3.0977
assert round(prior0, 5) == .97725
assert round(prior0 / (1 - prior0), 4) == 42.9558
assert round((post0 / (1 - post0)) / (prior0 / (1 - prior0)), 4) == .0721

for printed in (
    "$0.95$", "$95\\%$", "$0.25$", "$2.5\\%$", "$1{,}000$",
    "$L=1000$", "$\\theta_{(500)}$", "$\\theta_{(501)}$",
    "\\theta_{(25)}", "\\theta_{(975)}", "0.0602",
    "0.5178", "0.0406", "0.4837", "$0.4432$", "$0.4575$",
    "$3/12=0.25$", "$2/10=0.20$", "$0.025$", "$0.975$",
    "0.1093", "0.6097", "0.1133", "$[0.3,0.6]$",
):
    assert printed in body, f"Missing displayed number {printed}"

assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and "## Check yourself" in body
assert body.count('title="Answer"') >= 3
assert "../figures/part1-fig-01-credible-regions.png" in page
for qid in ("q-08", "ex-applied-iq", "q-03", "q-16"):
    assert f"../questions/{qid}.qmd" in page
assert 'data-cite-key="gelman_bda2013"' in body
print("credible interval endpoints, posterior content, proof and practice passed")
