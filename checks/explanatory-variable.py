"""Recompute the regression examples and retained shoe-size identities."""

from fractions import Fraction
from math import isclose


if __name__ == "__main__":
    xs = (0, 1, 2)
    ys = (50, 60, 65)
    xbar = Fraction(sum(xs), len(xs))
    ybar = Fraction(sum(ys), len(ys))
    sxx = sum((x - xbar) ** 2 for x in xs)
    sxy = sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys))
    slope = sxy / sxx
    intercept = ybar - slope * xbar
    assert xbar == 1
    assert ybar == Fraction(175, 3)
    assert sxx == 2
    assert sxy == 15
    assert slope == Fraction(15, 2)
    assert intercept == Fraction(305, 6)
    assert intercept + slope * Fraction(3, 2) == Fraction(745, 12)
    challenge = (5, 8, 11)
    assert Fraction(challenge[-1] - challenge[0], xs[-1] - xs[0]) == 3
    assert 5 + 3 * Fraction(3, 2) == Fraction(19, 2)
    shoe_t = 1.0048 / 0.2178
    assert isclose(shoe_t, 4.613, abs_tol=0.001)
    assert isclose(shoe_t ** 2, 21.28, abs_tol=0.005)
    assert isclose(shoe_t ** 2 / (shoe_t ** 2 + 98), 0.178, abs_tol=0.001)
    print("explanatory-variable arithmetic: 12 checks passed")
