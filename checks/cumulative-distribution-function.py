"""Exact arithmetic for the CDF article's mixed, cubic, and maximum examples."""

from fractions import Fraction
from pathlib import Path


PAGE = Path(__file__).resolve().parents[1] / "articles" / "cumulative-distribution-function.qmd"


def mixed_cdf(x):
    if x < 0:
        return Fraction(0)
    if x < 1:
        return Fraction(1, 4) + Fraction(3, 4) * x
    return Fraction(1)


def cubic_cdf(x):
    if x < 0:
        return Fraction(0)
    if x < 1:
        return x ** 3
    return Fraction(1)


def die_cdf(x):
    return Fraction(sum(face <= x for face in range(1, 7)), 6)


def die_quantile(u):
    return next(face for face in range(1, 7) if die_cdf(face) >= u)


if __name__ == "__main__":
    page = PAGE.read_text(encoding="utf-8")
    checks = [
        mixed_cdf(Fraction(-1)) == 0,
        mixed_cdf(Fraction(0)) == Fraction(1, 4),
        mixed_cdf(Fraction(1, 2)) == Fraction(5, 8),
        mixed_cdf(Fraction(1)) == 1,
        mixed_cdf(Fraction(0)) - mixed_cdf(Fraction(-1, 10**6)) == Fraction(1, 4),
        mixed_cdf(Fraction(1, 2)) - mixed_cdf(Fraction(0)) == Fraction(3, 8),
        mixed_cdf(Fraction(1, 2)) - 0 == Fraction(5, 8),
        mixed_cdf(Fraction(1, 3)) == Fraction(1, 2),
        die_quantile(Fraction(1, 8)) == 1,
        die_quantile(Fraction(1, 2)) == 3,
        die_cdf(Fraction(4)) == Fraction(2, 3),
        die_cdf(Fraction(4)) - die_cdf(Fraction(3)) == Fraction(1, 6),
        cubic_cdf(Fraction(3, 4)) - cubic_cdf(Fraction(1, 2)) == Fraction(19, 64),
        3 * Fraction(1, 4) == Fraction(3, 4),
        Fraction(2, 3) * Fraction(1, 2) == Fraction(1, 3),
        Fraction(1, 2) ** 3 == Fraction(1, 8),
        Fraction(3, 4) ** 3 == Fraction(27, 64),
        "$F_5(2)=3/5$" in page,
        "jump at $1$ is $2/5$" in page,
        "$F_X(0)-F_X(0-)=1/4$" in page,
        "$F_X(1/2)-F_X(0)=5/8-1/4=3/8$" in page,
        "$F_X(1/2)=5/8$" in page,
        "$Q(1/2)=1/3$" in page,
        "$Q(1/8)=0$" in page,
        "=(3/4)^3-(1/2)^3=19/64$" in page,
        "$f(x)=F'(x)=3x^2$" in page,
        "=3/4$" in page,
        "F_1(m)\\cdots F_n(m)" in page,
    ]
    assert all(checks), [index for index, passed in enumerate(checks, 1) if not passed]
    print(f"cumulative-distribution-function arithmetic: {len(checks)} checks passed")
