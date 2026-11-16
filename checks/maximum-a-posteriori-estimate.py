"""Exact beta–binomial, density-transform and penalty checks for the MAP page."""

from fractions import Fraction as F
from pathlib import Path

import sympy as sp


def main() -> None:
    article = (Path(__file__).resolve().parents[1] / "articles/maximum-a-posteriori-estimate.qmd").read_text()
    theta, eta, lam, sigma2, tau2 = sp.symbols("theta eta lam sigma2 tau2", positive=True)
    a, b, n, y = 3, 2, 8, 6
    A, B = a + y, b + n - y
    assert (A, B) == (9, 4)
    assert F(A - 1, A + B - 2) == F(8, 11)
    assert F(A, A + B) == F(9, 13)
    assert F(y, n) == F(3, 4) == F("0.75")
    assert round(float(F(8, 11)), 4) == 0.7273
    assert round(float(F(9, 13)), 4) == 0.6923
    A2, B2 = a + 4, b + n - 4
    assert (A2, B2) == (7, 6)
    assert F(A2 - 1, A2 + B2 - 2) == F(6, 11)
    assert F(A2, A2 + B2) == F(7, 13)
    assert F(4, 8) == F(1, 2) == F("0.5")
    assert round(float(F(6, 11)), 4) == 0.5455
    assert round(float(F(7, 13)), 4) == 0.5385
    density = 6 * theta * (1 - theta)
    odds_density = sp.simplify(density.subs(theta, eta / (1 + eta)) / (1 + eta) ** 2)
    assert odds_density == 6 * eta / (1 + eta) ** 4
    assert sp.solve(sp.diff(density, theta), theta) == [sp.Rational(1, 2)]
    assert sp.solve(sp.diff(odds_density, eta), eta) == [sp.Rational(1, 3)]
    assert sp.simplify(sp.diff(sp.log(odds_density), eta) - (1 / eta - 4 / (1 + eta))) == 0
    assert sp.simplify((sigma2 / tau2) / sigma2 - 1 / tau2) == 0
    assert sp.simplify(2 * sigma2 * lam / (2 * sigma2) - lam) == 0
    for printed in (
        "\\operatorname{Beta}(9,4)", "8/11\\approx0.7273", "9/13\\approx0.6923",
        "6/8=3/4=0.75", "\\operatorname{Beta}(7,6)",
        "6/11\\approx0.5455", "7/13\\approx0.5385", "4/8=1/2=0.5",
        "6\\theta(1-\\theta)", "6\\eta/(1+\\eta)^4", "\\eta=1/3",
        "\\theta=1/2", "2\\sigma^2\\lambda", "\\sigma^2/\\tau^2",
    ):
        assert printed in article, f"Missing printed value: {printed}"
    print("MAP estimate arithmetic: 24 checks passed")


if __name__ == "__main__":
    main()
