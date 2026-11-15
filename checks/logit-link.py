"""Recompute logit, odds, and separation examples."""

from fractions import Fraction
from math import exp, isclose, log


def expit(eta):
    return 1 / (1 + exp(-eta))


def logit(p):
    return log(p / (1 - p))


if __name__ == "__main__":
    old_p = Fraction(1, 5)
    old_odds = old_p / (1 - old_p)
    doubled = old_odds * 2
    group_odds = Fraction(1, 3)
    comparison_odds = group_odds * 3
    challenge_odds = Fraction(1, 9) * 3
    separated = ((0, 0), (1, 1))

    def separated_loglik(t):
        return sum(y * log(expit(t * (x - 0.5))) +
                   (1 - y) * log(1 - expit(t * (x - 0.5)))
                   for x, y in separated)

    checks = [
        old_odds == Fraction(1, 4),
        doubled == Fraction(1, 2),
        doubled / (1 + doubled) == Fraction(1, 3),
        isclose(log(float(old_odds)), -1.3862943611, abs_tol=1e-9),
        isclose(log(float(doubled)), -0.6931471806, abs_tol=1e-9),
        group_odds / (1 + group_odds) == Fraction(1, 4),
        comparison_odds == 1,
        comparison_odds / (1 + comparison_odds) == Fraction(1, 2),
        Fraction(1, 2) / Fraction(1, 4) == 2,
        Fraction(1, 2) - Fraction(1, 4) == Fraction(1, 4),
        challenge_odds == Fraction(1, 3),
        challenge_odds / (1 + challenge_odds) == Fraction(1, 4),
        Fraction(1, 4) / Fraction(1, 10) == Fraction(5, 2),
        Fraction(1, 4) - Fraction(1, 10) == Fraction(3, 20),
        isclose(expit(logit(0.2)), 0.2, abs_tol=1e-12),
        isclose(logit(expit(1.2)), 1.2, abs_tol=1e-12),
        isclose(logit(0.3), -logit(0.7), abs_tol=1e-12),
        isclose(expit(0), 0.5, abs_tol=1e-12),
        isclose(expit(0) * (1 - expit(0)), 0.25, abs_tol=1e-12),
        separated_loglik(1) < separated_loglik(5) < separated_loglik(20) < 0,
    ]
    assert all(checks)
    print(f"logit-link arithmetic: {len(checks)} checks passed")
