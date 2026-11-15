"""Recompute the population and sample correlation examples."""

from fractions import Fraction
from math import isclose


if __name__ == "__main__":
    pairs = ((1, 1), (2, 3), (3, 2))
    xbar = Fraction(sum(x for x, _ in pairs), len(pairs))
    ybar = Fraction(sum(y for _, y in pairs), len(pairs))
    sxx = sum((x - xbar) ** 2 for x, _ in pairs)
    syy = sum((y - ybar) ** 2 for _, y in pairs)
    sxy = sum((x - xbar) * (y - ybar) for x, y in pairs)
    transformed = tuple((x, 5 - 2 * y) for x, y in pairs)
    nonlinear = tuple((x, x * x) for x in (-2, -1, 0, 1, 2))
    checks = [
        xbar == 2,
        ybar == 2,
        sxx == 2,
        syy == 2,
        sxy == 1,
        Fraction(sxy, 2) == Fraction(1, 2),
        isclose(sxy / (sxx * syy) ** 0.5, 0.5),
        3 / (2 * 3) == 0.5,
        4 * 9 - 3 * 3 == 27,
        sum((x - xbar) * (y - 1) for x, y in transformed) == -2,
        sum((y - 1) ** 2 for _, y in transformed) == 8,
        isclose(-2 / (2 * 8) ** 0.5, -0.5),
        Fraction(1, 2) * 12 / 12 == Fraction(1, 2),
        sum(x * y for x, y in nonlinear) == 0,
        len({y for _, y in nonlinear}) > 1,
        Fraction(1, 2) ** 2 == Fraction(1, 4),
    ]
    assert all(checks)
    print(f"correlation arithmetic: {len(checks)} checks passed")
