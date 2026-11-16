"""Exact forecasting and covariance checks for AR and MA models."""

from fractions import Fraction as F
from pathlib import Path

import sympy as sp


def main() -> None:
    article = (Path(__file__).resolve().parents[1] / "articles/autoregression-and-moving-averages.qmd").read_text()
    phi, theta, sig2 = F(3, 5), F(1, 2), F(4)
    mu, today = F(10), F(12)
    assert mu + phi * (today - mu) == F(56, 5) == F("11.2")
    assert mu + phi**2 * (today - mu) == F(268, 25) == F("10.72")
    assert sig2 / (1 - phi**2) == F(25, 4) == F("6.25")
    assert sig2 * (1 + theta**2) == 5
    assert theta * sig2 == 2
    assert theta / (1 + theta**2) == F(2, 5) == F("0.4")
    assert mu + theta * 2 == 11
    assert mu + (-theta) * 2 == 9
    assert (-theta) * sig2 == -2
    assert (-theta) / (1 + theta**2) == F(-2, 5) == F("-0.4")
    z = sp.symbols("z")
    assert sp.summation(sp.Rational(3, 5) ** (2 * z), (z, 0, sp.oo)) == F(25, 16)
    for printed in (
        "3/5=0.6", "56/5=11.2", "268/25=10.72", "25/4=6.25",
        "2/5=0.4", "10+(1/2)2=11", "10+(-1/2)2=9",
        "(-1/2)4=-2", "-2/5=-0.4", "365", "\\beta=1",
    ):
        assert printed in article, f"Missing printed value: {printed}"
    assert "figures/ar-paths.png" in article
    print("AR and MA arithmetic: 12 checks passed")


if __name__ == "__main__":
    main()
