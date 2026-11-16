"""Check unbiasedness examples and their displayed numerical values."""

from fractions import Fraction
from pathlib import Path


PAGE = Path(__file__).resolve().parents[1] / "articles" / "unbiased-estimator.qmd"


if __name__ == "__main__":
    page = PAGE.read_text(encoding="utf-8")
    binary_pairs = ((0, 0), (0, 1), (1, 0), (1, 1))
    corrected = []
    uncorrected = []
    for pair in binary_pairs:
        mean = Fraction(sum(pair), 2)
        total = sum((Fraction(x) - mean) ** 2 for x in pair)
        corrected.append(total)
        uncorrected.append(total / 2)

    x = (0, 1, 2)
    expected_y = (1, 3, 5)
    xbar = Fraction(sum(x), len(x))
    ybar = Fraction(sum(expected_y), len(expected_y))
    sxx = sum((xi - xbar) ** 2 for xi in x)
    slope = sum((xi - xbar) * yi for xi, yi in zip(x, expected_y)) / sxx
    intercept = ybar - slope * xbar
    checks = [
        corrected == [0, Fraction(1, 2), Fraction(1, 2), 0],
        uncorrected == [0, Fraction(1, 4), Fraction(1, 4), 0],
        sum(corrected) / 4 == Fraction(1, 4),
        sum(uncorrected) / 4 == Fraction(1, 8),
        Fraction(1, 2) * (1 - Fraction(1, 2)) == Fraction(1, 4),
        Fraction(3, 4) * 9 == Fraction(27, 4),
        sxx == 2,
        slope == 2,
        intercept == 1,
        Fraction(2, 9) > Fraction(19, 100),
        Fraction(19, 100) == Fraction(2 * 10 - 1, 10 * 10),
        Fraction(1, 4) ** 2 + Fraction(9, 16) == Fraction(5, 8),
        "takes values $0,1/2,1/2,0$" in page,
        "values $0,1/4,1/4,0$ and expectation $1/8$" in page,
        "Its expectation is $1/4$" in page,
        "The first expectation is $9$" in page,
        "$((n-1)/n)\\sigma^2=(3/4)9=27/4=6.75$" in page,
        round(Fraction(2, 9), 3) == Fraction(222, 1000) and "$0.222\\,\\sigma^4$" in page,
        round(Fraction(19, 100), 3) == Fraction(190, 1000) and "$0.190\\,\\sigma^4$" in page,
    ]
    assert all(checks), [index for index, passed in enumerate(checks, 1) if not passed]
    print(f"unbiased-estimator arithmetic: {len(checks)} checks passed")
