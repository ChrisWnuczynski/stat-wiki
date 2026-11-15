"""Check MLE examples, boundary cases, and right-censored lifetimes."""

from fractions import Fraction
from math import comb, exp, isclose, log


def binomial_two_of_ten(p):
    return comb(10, 2) * p ** 2 * (1 - p) ** 8


if __name__ == "__main__":
    plug_values = [binomial_two_of_ten(p) for p in (0.2, 0.3, 0.4)]
    x = (1, 2, 4)
    xbar = Fraction(sum(x), len(x))
    spread = sum((Fraction(xi) - xbar) ** 2 for xi in x)
    n = 10
    uniform_mse_mom = Fraction(1, 3 * n)
    uniform_mse_max = Fraction(2, (n + 1) * (n + 2))
    checks = [
        isclose(plug_values[0], 0.301989888, abs_tol=1e-9),
        isclose(plug_values[1], 0.2334744405, abs_tol=1e-9),
        isclose(plug_values[2], 0.120932352, abs_tol=1e-9),
        plug_values[0] > plug_values[1] > plug_values[2],
        xbar == Fraction(7, 3),
        spread == Fraction(14, 3),
        spread / len(x) == Fraction(14, 9),
        uniform_mse_mom == Fraction(1, 30),
        uniform_mse_max == Fraction(1, 66),
        uniform_mse_max < uniform_mse_mom,
        Fraction(1, n * (n + 2)) == Fraction(1, 120),
        Fraction(2, 11) == Fraction(2, 2 + 4 + 5),
        Fraction(3, 12) == Fraction(3, 1 + 2 + 4 + 5),
        isclose(2 * log(2 / 11) - 11 * (2 / 11),
                log((2 / 11) ** 2 * exp(-2)), abs_tol=1e-12),
        binomial_two_of_ten(0) == 0,
        (1 - 0) ** 10 == 1,
        (0.2 ** -3) < (0.1 ** -3),
        (-3 / 2) * log(0.1) < (-3 / 2) * log(0.01),
    ]
    assert all(checks)
    print(f"maximum-likelihood arithmetic: {len(checks)} checks passed")
