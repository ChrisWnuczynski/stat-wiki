"""Recompute the Beta–Binomial predictive gap and lock the labs index wording.

For a posterior θ ~ Beta(a, b) and K | θ ~ Binomial(m, θ),

    Var(K) = m E[θ(1-θ)] + m² Var(θ),
    p̄(1-p̄) = E[θ(1-θ)] + Var(θ),

with p̄ = E[θ]. The plug-in binomial at p̄ therefore has variance smaller
by m(m-1) Var(θ). At m = 1 the two distributions are the same Bernoulli law.
"""
from pathlib import Path

import numpy as np
from scipy.stats import betabinom, binom

ROOT = Path(__file__).resolve().parents[1]

# Posterior shapes and future lengths, including the chapter's Beta(10, 4)
# example, the laboratory's default posterior Beta(8, 12), a prior with no
# observations, and a non-integer shape.
CASES = (
    (10, 4, 1),
    (10, 4, 5),
    (8, 12, 1),
    (8, 12, 5),
    (5, 5, 3),
    (0.6, 0.6, 2),
    (1, 1, 10),
    (2.5, 7.5, 4),
    (3, 1, 7),
)


def posterior_moments(a, b):
    total = a + b
    mean = a / total
    variance = a * b / (total ** 2 * (total + 1))
    expected_product = a * b / (total * (total + 1))
    return mean, variance, expected_product


for a, b, m in CASES:
    mean, variance, expected_product = posterior_moments(a, b)
    # Second-moment identity, for any law with a finite second moment.
    assert np.isclose(mean * (1 - mean), expected_product + variance)

    ks = np.arange(m + 1)
    predictive = betabinom(m, a, b)
    plugin = binom(m, mean)
    predictive_pmf = predictive.pmf(ks)
    plugin_pmf = plugin.pmf(ks)
    assert np.isclose(predictive_pmf.sum(), 1)
    predictive_mean = float(ks @ predictive_pmf)
    predictive_variance = float(((ks - predictive_mean) ** 2) @ predictive_pmf)
    plugin_variance = float(plugin.var())
    formula = m * expected_product + m ** 2 * variance
    gap = m * (m - 1) * variance

    assert np.isclose(predictive_mean, m * mean)
    assert np.isclose(predictive_variance, float(predictive.var()))
    assert np.isclose(predictive_variance, formula)
    assert np.isclose(plugin_variance, m * mean * (1 - mean))
    assert np.isclose(predictive_variance - plugin_variance, gap)
    if m == 1:
        assert np.allclose(predictive_pmf, plugin_pmf)
        assert np.isclose(gap, 0)
    else:
        assert gap > 0
        assert np.max(np.abs(predictive_pmf - plugin_pmf)) > 1e-8

# The five-toss example on the theory page: exact fractions.
assert np.isclose(posterior_moments(10, 4)[1], 2 / 147)
assert np.isclose(betabinom(5, 10, 4).var(), 190 / 147)
assert np.isclose(binom(5, 10 / 14).var(), 50 / 49)
assert np.isclose(betabinom(5, 10, 4).var() - binom(5, 10 / 14).var(), 40 / 147)
assert np.isclose(5 * (5 - 1) * (2 / 147), 40 / 147)

index = (ROOT / "labs" / "index.qmd").read_text(encoding="utf-8")
section = index.split("## Beta–Binomial updating", 1)[1].split("\n## ", 1)[0]
for fragment in (
    "one future toss",
    "Bernoulli distribution with success probability",
    "is the same distribution",
    "For $m>1$ future tosses",
    "law of total variance",
    r"m(m-1)\operatorname{Var}(\theta\mid x)",
    "With no observed tosses",
    "sample proportion, the plug-in based on the observed tosses, is defined only for $n\\ge 1$",
    "there is no sample proportion",
    "Because the posterior variance is positive, the excess is positive for $m>1$",
):
    assert fragment in section, fragment
assert "wider" not in section
print("labs index Beta–Binomial predictive identity passed")
