"""Exact checks for the joint-density triangle and exponential examples."""

from fractions import Fraction
from math import exp


def trap(fn, a, b, n=20000):
    h = (b - a) / n
    total = 0.5 * (fn(a) + fn(b))
    for i in range(1, n):
        total += fn(a + i * h)
    return total * h


if __name__ == "__main__":
    # Uniform on the triangle 0 < y < x < 1, density 2.
    area = Fraction(1, 2)
    assert area * 2 == 1
    ex = Fraction(2, 3)  # integral_0^1 x * 2x dx
    ey = Fraction(1, 3)  # integral_0^1 2y(1-y) dy
    exy = Fraction(1, 4)  # integral_0^1 x^3 dx
    cov = exy - ex * ey
    assert cov == Fraction(1, 36)
    px = 1 - Fraction(1, 2) ** 2
    assert px == Fraction(3, 4)
    assert 2 * (1 - Fraction(1, 2)) == 1  # f_Y(1/2)

    # Existing product density  e^{-x} * 2e^{-2y}.
    mean_x, var_x = 1, 1
    mean_y, var_y = Fraction(1, 2), Fraction(1, 4)
    assert mean_x * mean_y == Fraction(1, 2)
    assert var_x - var_y == Fraction(3, 4)
    # Numerical integral of the joint density over the quadrant.
    mass = trap(lambda x: exp(-x), 0, 40) * trap(lambda y: 2 * exp(-2 * y), 0, 40)
    assert abs(mass - 1) < 1e-4

    checks = [
        area * 2 == 1,
        ex == Fraction(2, 3),
        ey == Fraction(1, 3),
        exy == Fraction(1, 4),
        cov == Fraction(1, 36),
        px == Fraction(3, 4),
        mean_x * mean_y == Fraction(1, 2),
        var_x - var_y == Fraction(3, 4),
        abs(mass - 1) < 1e-4,
        2 * (1 - Fraction(1, 2)) == 1,
    ]
    assert all(checks)
    print(f"joint-probability-density arithmetic: {len(checks)} checks passed")
