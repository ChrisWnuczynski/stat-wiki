"""Check every printed numeric claim in the burn-in depth page."""
from fractions import Fraction as F
from pathlib import Path

text = (Path(__file__).parents[1] / "research/content/burn-in.md").read_text()
page = (Path(__file__).parents[1] / "articles/burn-in.qmd").read_text()
P = ((F(9, 10), F(1, 10)), (F(1, 5), F(4, 5)))
assert all(sum(row) == 1 for row in P)
pi = (F(2, 3), F(1, 3))
assert tuple(sum(pi[i] * P[i][j] for i in range(2)) for j in range(2)) == pi
assert P[1][1] - P[0][1] == F(7, 10)
for t, start, prob, tv in [
    (5, 0, "0.27731", "0.0560233"),
    (10, 0, "0.3239174917", "0.0094158416"),
    (5, 1, "0.44538", "0.1120467"),
]:
    p = F(start, 1)
    for _ in range(t):
        p = F(1, 10) + F(7, 10) * p
    expected = (1 - F(7, 10) ** t) / 3 if start == 0 else F(1, 3) + F(2, 3) * F(7, 10) ** t
    assert p == expected
    assert abs(float(p) - float(prob)) < 1e-10
    assert abs(abs(float(p - pi[1])) - float(tv)) < 4e-8
    assert prob in text and tv in text
    assert prob in page and tv in page
assert F(1, 10) + F(7, 10) * F(1, 3) == F(1, 3)
assert F(7, 10) ** 10 / 3 < F(1, 100)
for token in ("0.9", "0.1", "0.2", "0.8", "2/3", "1/3", "0.7", "t=5", "t=10"):
    assert token in text, token
    assert token in page, token
print("burn-in arithmetic: 15 checks passed")
