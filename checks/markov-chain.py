"""Exact transition and path checks for the Markov-chain article."""

from fractions import Fraction as F
from pathlib import Path

import sympy as sp


def main() -> None:
    article = (Path(__file__).resolve().parents[1] / "articles/markov-chain.qmd").read_text()
    P = sp.Matrix(
        [
            [F(1, 5), F(4, 5), 0],
            [0, F(3, 10), F(7, 10)],
            [F(3, 5), 0, F(2, 5)],
        ]
    )
    assert all(sum(P.row(i)) == 1 for i in range(3))
    assert list(sp.Matrix([[1, 0, 0]]) * P**2) == list((P**2).row(0))
    assert list((P**2).row(0)) == [F(1, 25), F(2, 5), F(14, 25)]
    assert P[0, 1] * P[1, 2] == F(14, 25) == F("0.56")
    assert P[0, 1] * P[1, 2] * P[2, 0] == F(42, 125) == F("0.336")
    assert P[2, 0] == F(3, 5) == F("0.6")
    assert F(1, 25) + F(2, 5) + F(14, 25) == 1
    Q = sp.Matrix(
        [
            [F(1, 2), F(1, 4), 0, 0],
            [F(1, 2), F(1, 2), F(1, 4), 0],
            [0, F(1, 4), F(1, 2), F(1, 2)],
            [0, 0, F(1, 4), F(1, 2)],
        ]
    )
    assert all(sum(Q.col(j)) == 1 for j in range(4))
    pi = sp.Matrix([F(1, 6), F(2, 6), F(2, 6), F(1, 6)])
    assert Q * pi == pi and sum(pi) == 1
    assert Q[1, 0] * pi[0] == Q[0, 1] * pi[1]
    assert Q[2, 1] * pi[1] == Q[1, 2] * pi[2]
    assert Q[3, 2] * pi[2] == Q[2, 3] * pi[3]
    for printed in (
        "1/5&4/5&0", "0&3/10&7/10", "3/5&0&2/5",
        "14/25=0.56", "1/25,\\ 2/5,\\ 14/25", "0.04,\\ 0.40,\\ 0.56",
        "42/125=0.336", "3/5=0.6", "1/6,2/6,2/6,1/6",
    ):
        assert printed in article, f"Missing printed value: {printed}"
    print("markov-chain arithmetic: 12 checks passed")


if __name__ == "__main__":
    main()
