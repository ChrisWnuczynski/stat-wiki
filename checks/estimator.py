"""Recompute the estimator article's observed and sampling calculations."""

from fractions import Fraction
from math import isclose, sqrt


if __name__ == "__main__":
    old_sample = (0, 1, 1, 0, 1, 0, 0, 1, 0, 0)
    old_estimate = Fraction(sum(old_sample), len(old_sample))
    p = Fraction(2, 5)
    n = 10
    bernoulli_mean = p
    bernoulli_variance = p * (1 - p)
    proportion_variance = bernoulli_variance / n
    example_estimate = Fraction(44, 100)
    challenge_estimate = Fraction(18, 30)
    checks = [
        sum(old_sample) == 4,
        old_estimate == Fraction(2, 5),
        bernoulli_mean == Fraction(2, 5),
        bernoulli_variance == Fraction(6, 25),
        proportion_variance == Fraction(3, 125),
        example_estimate == Fraction(11, 25),
        example_estimate * (1 - example_estimate) / 100 == Fraction(77, 31250),
        isclose(sqrt(float(example_estimate * (1 - example_estimate) / 100)), 0.0496387, abs_tol=1e-7),
        sqrt(Fraction(1, 4) / 100) == 0.05,
        challenge_estimate == Fraction(3, 5),
        challenge_estimate * (1 - challenge_estimate) / 30 == Fraction(1, 125),
        isclose(sqrt(Fraction(1, 125)), 0.0894427, abs_tol=1e-7),
        Fraction(3, 10) ** 2 + Fraction(4, 10) == Fraction(49, 100),
        Fraction(0, 1) ** 0 * Fraction(1, 1) ** 10 == 1,
        Fraction(1, 1) ** 10 * Fraction(0, 1) ** 0 == 1,
    ]
    assert all(checks)
    print(f"estimator arithmetic: {len(checks)} checks passed")
