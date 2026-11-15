"""Check probability, odds, odds-ratio, and posterior-odds arithmetic."""

from fractions import Fraction
from math import exp, isclose, log


def odds(p):
    return p / (1 - p)


def probability(o):
    return o / (1 + o)


if __name__ == "__main__":
    p1 = Fraction(3, 5)
    p0 = Fraction(3, 10)
    prior1 = Fraction(1, 4)
    prior0 = Fraction(3, 4)
    prior_odds = prior1 / prior0
    posterior_odds = prior_odds * 6
    checks = [
        odds(Fraction(4, 5)) == 4,
        probability(Fraction(4, 1)) == Fraction(4, 5),
        odds(Fraction(1, 5)) == Fraction(1, 4),
        probability(Fraction(1, 4)) == Fraction(1, 5),
        odds(Fraction(1, 2)) == 1,
        odds(Fraction(1, 4)) * odds(Fraction(3, 4)) == 1,
        odds(p1) == Fraction(3, 2),
        odds(p0) == Fraction(3, 7),
        odds(p1) / odds(p0) == Fraction(7, 2),
        p1 / p0 == 2,
        p1 - p0 == Fraction(3, 10),
        prior_odds == Fraction(1, 3),
        posterior_odds == 2,
        probability(posterior_odds) == Fraction(2, 3),
        isclose(exp(log(odds(p0))), float(odds(p0)), abs_tol=1e-12),
        isclose(exp(log(odds(p0)) + log(3)), 3 * float(odds(p0)), abs_tol=1e-12),
    ]
    assert all(checks)
    print(f"odds arithmetic: {len(checks)} checks passed")
