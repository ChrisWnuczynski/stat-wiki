"""Verify the Beta and inverse-Gamma kernel updates and normalizers."""

from fractions import Fraction
from math import comb, gamma, isclose


if __name__ == "__main__":
    a, b, successes, failures = 2, 3, 7, 3
    post_a, post_b = a + successes, b + failures
    beta_integral = gamma(post_a) * gamma(post_b) / gamma(post_a + post_b)
    checks = [
        post_a == 9,
        post_b == 6,
        post_a - 1 == 8,
        post_b - 1 == 5,
        Fraction(post_a, post_a + post_b) == Fraction(3, 5),
        isclose(beta_integral, gamma(9) * gamma(6) / gamma(15)),
        isclose((1 / beta_integral) * beta_integral, 1),
        comb(10, 7) == 120,
        (a + 2, b + 1) == (4, 4),
        Fraction(a + 2, a + b + 3) == Fraction(1, 2),
        (3 + 8 / 2) == 7,
        (2 + 20 / 2) == 12,
    ]
    assert all(checks)
    print(f"kernel-of-a-density arithmetic: {len(checks)} checks passed")
