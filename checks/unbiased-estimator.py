"""Check unbiasedness examples and the retained normal-variance MSE comparison."""

from fractions import Fraction


if __name__ == "__main__":
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
    ]
    assert all(checks)
    print(f"unbiased-estimator arithmetic: {len(checks)} checks passed")
