"""Recompute posterior means, modes, weights, and risk in the page's examples."""

from fractions import Fraction


if __name__ == "__main__":
    prior_a, prior_b, x, n = 2, 2, 7, 10
    post_a, post_b = prior_a + x, prior_b + n - x
    post_mean = Fraction(post_a, post_a + post_b)
    post_mode = Fraction(post_a - 1, post_a + post_b - 2)
    prior_weight = Fraction(prior_a + prior_b, prior_a + prior_b + n)
    data_weight = Fraction(n, prior_a + prior_b + n)
    prior_precision = Fraction(1, 4)
    data_precision = Fraction(4, 4)
    normal_precision = prior_precision + data_precision
    checks = [
        (post_a, post_b) == (9, 5),
        post_mean == Fraction(9, 14),
        prior_weight == Fraction(4, 14),
        data_weight == Fraction(10, 14),
        prior_weight + data_weight == 1,
        prior_weight * Fraction(1, 2) + data_weight * Fraction(7, 10) == post_mean,
        post_mode == Fraction(2, 3),
        Fraction(post_a * post_b, (post_a + post_b) ** 2 * (post_a + post_b + 1)) == Fraction(3, 196),
        normal_precision == Fraction(5, 4),
        Fraction(3, 1) / normal_precision == Fraction(12, 5),
        1 / normal_precision == Fraction(4, 5),
        (1 + 3, 1 + 10 - 3) == (4, 8),
        Fraction(4, 12) == Fraction(1, 3),
        Fraction(4 - 1, 4 + 8 - 2) == Fraction(3, 10),
        Fraction(3, 3 + 9) == Fraction(1, 4),
        Fraction(3 - 1, 3 + 9 - 2) == Fraction(1, 5),
    ]
    assert all(checks)
    print(f"posterior-mean arithmetic: {len(checks)} checks passed")
