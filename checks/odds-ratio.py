"""Exact table, baseline-risk and stratified odds-ratio checks."""

from fractions import Fraction as F
from pathlib import Path

import sympy as sp


def odds(p: F) -> F:
    return p / (1 - p)


def main() -> None:
    article = (Path(__file__).resolve().parents[1] / "articles/odds-ratio.qmd").read_text()
    a, b, c, d = 30, 70, 10, 90
    pe, pu = F(a, a + b), F(c, c + d)
    assert (pe, pu) == (F("0.30"), F("0.10"))
    assert odds(pe) == F(3, 7)
    assert odds(pu) == F(1, 9)
    assert F(a * d, b * c) == odds(pe) / odds(pu) == F(27, 7)
    assert round(float(F(3, 7)), 4) == 0.4286
    assert round(float(F(1, 9)), 4) == 0.1111
    assert round(float(F(27, 7)), 4) == 3.8571
    assert pe / pu == 3 and pe - pu == F("0.20")
    assert F(c * b, d * a) == F(7, 27)
    a2, b2, c2, d2 = 8, 92, 4, 96
    assert F(a2 * d2, b2 * c2) == F(48, 23)
    assert round(float(F(48, 23)), 4) == 2.0870
    assert F(a2, a2 + b2) / F(c2, c2 + d2) == 2
    assert F(a2, a2 + b2) - F(c2, c2 + d2) == F("0.04")
    assert odds(F(3, 4)) / odds(F(1, 2)) == 3
    assert F(3, 4) / F(1, 2) == F(3, 2) == F("1.5")
    for u, e in [(F(1, 10), F(1, 4)), (F(1, 2), F(3, 4))]:
        assert odds(e) / odds(u) == 3
        assert 3 * u / (1 - u + 3 * u) == e
    marg_u = (F(1, 10) + F(1, 2)) / 2
    marg_e = (F(1, 4) + F(3, 4)) / 2
    assert (marg_u, marg_e) == (F(3, 10), F(1, 2))
    assert odds(marg_e) / odds(marg_u) == F(7, 3)
    assert round(float(F(7, 3)), 4) == 2.3333
    beta = sp.symbols("beta", real=True)
    assert sp.simplify(sp.exp(beta) / 1 - sp.exp(beta)) == 0
    for printed in (
        "30/70=3/7\\approx0.4286", "10/90=1/9\\approx0.1111",
        "27}{7}\\approx3.8571", "0.30", "0.10", "0.20",
        "48/23\\approx2.0870", "0.08/0.04=2", "0.08-0.04=0.04",
        "7/3\\approx2.3333", "3/2=1.5", "p_E=rp_U/(1-p_U+rp_U)",
    ):
        assert printed in article, f"Missing printed value: {printed}"
    print("odds-ratio arithmetic: 22 checks passed")


if __name__ == "__main__":
    main()
