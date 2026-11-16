"""Check the four-state weather construction and state-space article structure."""

from fractions import Fraction as F
from pathlib import Path

from sympy import Matrix

root = Path(__file__).resolve().parents[1]
page = (root / "articles/state-space.qmd").read_text()
body = page.split("## See also", 1)[0]

# Ordering: (0,0), (0,1), (1,0), (1,1).
p = Matrix([[F(4, 5), F(1, 5), 0, 0],
            [0, 0, F(7, 10), F(3, 10)],
            [F(4, 5), F(1, 5), 0, 0],
            [0, 0, F(1, 5), F(4, 5)]])
assert p.shape == (4, 4)
assert all(v >= 0 for v in p)
assert all(sum(p.row(i)) == 1 for i in range(4))
assert p[1, 3] * p[3, 3] == F(6, 25)  # .3 * .8 = .24
assert p[3, 3] ** 2 == F(16, 25)  # .8 squared = .64
after_two = p.row(2) * p
assert after_two[1] + after_two[3] == F(11, 50)  # rain at t+2 = .22
assert F(4, 5) * F(1, 5) + F(1, 5) * F(3, 10) == F(11, 50)
assert p[1, 3] != p[3, 3]  # same visible rain, different next-step law

for printed in ("0.2", "0.3", "0.8", "0.7", "0.24", "0.64", "0.22",
                "0.8(0.2)+0.2(0.3)", "(0,0),(0,1),(1,0),(1,1)"):
    assert printed in body, f"missing printed number: {printed}"
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
assert "{#assumptions-and-limits}" in body
for qid in ("c-12", "ex-sp-same-marginals", "ex-sp-increments-and-levels"):
    assert f"../questions/{qid}.qmd" in body
    assert "Worked answer" in (root / f"questions/{qid}.qmd").read_text()
print("state-space numbers and structure passed")
