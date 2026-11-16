"""Printed-value checks for partial autocorrelation."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROSE = (ROOT / "research" / "content" / "partial-autocorrelation.md").read_text(encoding="utf-8")


def phi22(rho1: float, rho2: float) -> float:
    return (rho2 - rho1 ** 2) / (1 - rho1 ** 2)


def main() -> None:
    assert [0.5 ** k for k in (1, 2, 3)] == [0.5, 0.25, 0.125]
    assert phi22(0.5, 0.25) == 0
    rho = Fraction(3, 5) / (1 + Fraction(9, 25))
    assert rho == Fraction(15, 34)
    assert abs(float(rho) - 0.4411764705882353) < 1e-12
    assert f"{float(rho):.4f}" == "0.4412"
    num = -(rho ** 2)
    den = 1 - rho ** 2
    assert num / den == Fraction(-225, 931)
    assert f"{float(num / den):.4f}" == "-0.2417"
    assert phi22(0.8, 0.8 ** 2) == 0
    assert abs(phi22(Fraction(4, 5), Fraction(16, 25))) < 1e-15
    assert abs(phi22(0.5, 0.1) - (-0.2)) < 1e-12
    for token in ("0.125", "0.4412", "-0.2417", "0.64", "-0.2", "15}{34", "225}{931"):
        assert token in PROSE, token
    article = ROOT / "articles" / "partial-autocorrelation.qmd"
    if article.is_file():
        body = article.read_text(encoding="utf-8")
        assert "0.4412" in body and "-0.2417" in body
    print("partial-autocorrelation checks passed")


if __name__ == "__main__":
    main()
