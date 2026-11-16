"""Exact Jacobian, support and transformed-density checks."""

from fractions import Fraction as F
from pathlib import Path

import sympy as sp


def main() -> None:
    article = (Path(__file__).resolve().parents[1] / "articles/jacobian.qmd").read_text()
    A = sp.Matrix([[1, 1], [1, -1]])
    assert A.det() == -2
    assert A.inv() == sp.Matrix([[F(1, 2), F(1, 2)], [F(1, 2), F(-1, 2)]])
    assert A.inv().det() == -sp.Rational(1, 2)
    assert abs(A.det()) * abs(A.inv().det()) == 1
    assert F(1, 2) * 2 == 1
    s = sp.symbols("s", positive=True)
    assert sp.integrate(s, (s, 0, 1)) == F(1, 2)
    assert sp.integrate(2 - s, (s, 1, 2)) == F(1, 2)
    assert sp.integrate(s, (s, 0, 1)) + sp.integrate(2 - s, (s, 1, 2)) == 1
    B = sp.diag(2, 3)
    assert B.det() == 6 and B.inv().det() == F(1, 6)
    assert F(1, 6) * 6 == 1
    assert F(1, 6) * 1 == F(1, 6)
    y = sp.symbols("y", positive=True)
    correct = 1 / (2 * sp.sqrt(y))
    one_branch = 1 / (4 * sp.sqrt(y))
    assert sp.integrate(correct, (y, 0, 1)) == 1
    assert sp.integrate(one_branch, (y, 0, 1)) == F(1, 2)
    assert sp.Matrix([[1, 0], [1, 0]]).det() == 0
    for printed in (
        "-2", "-1/2", "1/2", "area $2$", "f_S(s)=s",
        "f_S(s)=2-s", "\\Pr(S<1)=1/2", "U=2X", "V=3Y",
        "1/6", "area $6$", "1/(2\\sqrt y)", "1/(4\\sqrt y)",
        "1815", "1841",
    ):
        assert printed in article, f"Missing printed value: {printed}"
    print("jacobian arithmetic: 19 checks passed")


if __name__ == "__main__":
    main()
