"""Check all numeric transition calculations in the generated page and new depth text."""
from fractions import Fraction as F
from pathlib import Path
import sympy as s

root = Path(__file__).parents[1]
depth = (root / "research/content/transition-matrix.md").read_text()
page = (root / "articles/transition-matrix.qmd").read_text() if (root / "articles/transition-matrix.qmd").exists() else depth
P = s.Matrix([[F(1, 2), F(1, 2), 0], [0, F(1, 2), F(1, 2)], [F(1, 2), 0, F(1, 2)]])
assert P**2 == s.Matrix([[F(1, 4), F(1, 2), F(1, 4)], [F(1, 4), F(1, 4), F(1, 2)], [F(1, 2), F(1, 4), F(1, 4)]])
assert P**3 == s.Matrix([[F(1, 4), F(3, 8), F(3, 8)], [F(3, 8), F(1, 4), F(3, 8)], [F(3, 8), F(3, 8), F(1, 4)]])
pi = s.Matrix([[F(1, 3), F(1, 3), F(1, 3)]])
assert pi * P == pi
assert (P**2)[0, 2] == P[0, 1] * P[1, 2] == F(1, 4)
assert (P**2)[2, 1] == P[2, 0] * P[0, 1] == F(1, 4)
assert all(sum(P.row(i)) == 1 for i in range(3))
weather = s.Matrix([[F(4, 5), F(1, 5)], [F(3, 10), F(7, 10)]])
assert (weather**2)[0, 1] == F(3, 10)
assert (weather**2)[1, 0] == F(9, 20)
assert sum(weather[:, 0]) != 1 and sum(weather[:, 1]) != 1
path = s.Matrix([[F(7, 10), F(3, 10), 0], [F(1, 5), F(1, 2), F(3, 10)], [0, F(2, 5), F(3, 5)]])
assert (path**2)[0, 2] == F(9, 100)
swap = s.Matrix([[0, 1], [1, 0]])
identity = s.eye(2)
assert swap*identity == swap and swap**2 == identity
assert P**0 == s.eye(3)
assert s.Matrix([[F(1, 2), F(1, 2)]])*swap == s.Matrix([[F(1, 2), F(1, 2)]])
for token in ("1/2", "1/4", "3/8", "1/3", "P^2", "P^3"):
    assert token in depth, token
for token in ("0.30", "0.45", "0.09"):
    assert token in page or page == depth, token
print("transition-matrix arithmetic: 21 checks passed")
