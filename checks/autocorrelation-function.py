"""Exact checks for the six-observation autocorrelation illustration."""

from fractions import Fraction
from pathlib import Path

import sympy as sp
from sympy.stats import E, Normal


def main() -> None:
    article = (Path(__file__).resolve().parents[1] / "articles/autocorrelation-function.qmd").read_text()
    y = list(map(Fraction, (4, 7, 5, 8, 6, 9)))
    mean = sum(y) / len(y)
    centered = [value - mean for value in y]
    denominator = sum(value * value for value in centered)
    numerator = lambda k: sum(centered[t] * centered[t - k] for t in range(k, len(y)))
    assert mean == Fraction(13, 2) == Fraction("6.5")
    assert denominator == Fraction(35, 2) == Fraction("17.5")
    assert numerator(1) == Fraction(-25, 4) == Fraction("-6.25")
    assert numerator(2) == 9
    assert numerator(3) == Fraction(-31, 4)
    assert numerator(1) / denominator == Fraction(-5, 14)
    assert numerator(2) / denominator == Fraction(18, 35)
    assert numerator(3) / denominator == Fraction(-31, 70)
    assert round(float(Fraction(-5, 14)), 4) == -0.3571
    assert round(float(Fraction(18, 35)), 4) == 0.5143
    assert round(float(Fraction(-31, 70)), 4) == -0.4429
    z = Normal("z", 0, 1)
    assert E(z**2) == 1 and E(z**4) == 3
    for printed in (
        "4,7,5,8,6,9",
        "13/2=6.5",
        "35/2=17.5",
        "-25/4=-6.25",
        "-5/14",
        "-0.3571",
        "18/35",
        "0.5143",
        "-31/4",
        "-31/70",
        "-0.4429",
    ):
        assert printed in article, f"Missing printed value: {printed}"
    print("autocorrelation-function arithmetic: 12 checks passed")


if __name__ == "__main__":
    main()
