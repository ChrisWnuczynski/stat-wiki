"""Check the printed proposal probabilities, acceptance rates, and flows."""
from fractions import Fraction as F
from pathlib import Path

text = (Path(__file__).parents[1] / "research/content/random-walk-and-independent-proposals.md").read_text()
page = (Path(__file__).parents[1] / "articles/random-walk-and-independent-proposals.qmd").read_text()
pi = (F(1, 2), F(1, 3), F(1, 6))
g = (F(1, 6), F(1, 2), F(1, 3))
q = ((F(1, 2), F(1, 2), F(0)), (F(1, 2), F(0), F(1, 2)), (F(0), F(1, 2), F(1, 2)))
assert sum(pi) == sum(g) == 1
assert all(sum(row) == 1 for row in q)
rw01 = min(F(1), pi[1] * q[1][0] / (pi[0] * q[0][1]))
rw12 = min(F(1), pi[2] * q[2][1] / (pi[1] * q[1][2]))
ind01 = min(F(1), pi[1] * g[0] / (pi[0] * g[1]))
ind10 = min(F(1), pi[0] * g[1] / (pi[1] * g[0]))
ind12 = min(F(1), pi[2] * g[1] / (pi[1] * g[2]))
assert (rw01, rw12, ind01, ind10, ind12) == (F(2, 3), F(1, 2), F(2, 9), 1, F(3, 4))
assert pi[0] * q[0][1] * rw01 == pi[1] * q[1][0] == F(1, 6)
assert pi[0] * g[1] * ind01 == pi[1] * g[0] * ind10 == F(1, 18)
assert pi[1] / pi[0] == F(2, 3) != ind01
for token in ("(1/2,1/3,1/6)", "(1/6,1/2,1/3)", "2/3", "2/9", "1/6", "1/18", "1/2", "3/4"):
    assert token in text, token
    assert token in page, token
print("proposal arithmetic: 18 checks passed")
