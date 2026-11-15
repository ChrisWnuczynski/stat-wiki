"""Check MLE examples, boundary cases, and values printed in the article."""

from fractions import Fraction
from math import comb, exp, isclose, log
from pathlib import Path


PAGE = Path(__file__).resolve().parents[1] / "articles" / "maximum-likelihood.qmd"


def binomial_two_of_ten(p):
    return comb(10, 2) * p ** 2 * (1 - p) ** 8


if __name__ == "__main__":
    page = PAGE.read_text(encoding="utf-8")
    plug_values = [binomial_two_of_ten(p) for p in (0.2, 0.3, 0.4)]
    n = 10
    uniform_mse_mom = Fraction(1, 3 * n)
    uniform_mse_max = Fraction(2, (n + 1) * (n + 2))
    checks = [
        isclose(plug_values[0], 0.301989888, abs_tol=1e-9),
        isclose(plug_values[1], 0.2334744405, abs_tol=1e-9),
        isclose(plug_values[2], 0.120932352, abs_tol=1e-9),
        plug_values[0] > plug_values[1] > plug_values[2],
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
        all(f"${value:.3f}$" in page for value in plug_values),
        "$\\widehat p=0.2$" in page,
        round(uniform_mse_mom, 3) == Fraction(33, 1000) and "$0.033\\,\\theta^2$" in page,
        round(uniform_mse_max, 3) == Fraction(15, 1000) and "$0.015\\,\\theta^2$" in page,
        round(Fraction(2, 11), 4) == Fraction(1818, 10000) and "2/11\\approx0.1818$" in page,
        "$3/11$" in page,
        Fraction(3, 12) == Fraction(1, 4) and "3/12=0.25$" in page,
    ]
    assert all(checks), [index for index, passed in enumerate(checks, 1) if not passed]
    print(f"maximum-likelihood arithmetic: {len(checks)} checks passed")
