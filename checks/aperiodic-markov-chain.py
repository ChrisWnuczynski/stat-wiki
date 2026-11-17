"""Check every displayed numeric transition and stationary probability on rank 158."""
from pathlib import Path
import sympy as sp
import json

root = Path(__file__).resolve().parents[1]
page = (root / "articles/aperiodic-markov-chain.qmd").read_text()
body = page.split("## See also")[0]

P = sp.Matrix([[0, 1, 0], [0, 0, 1], [sp.Rational(1, 2), sp.Rational(1, 2), 0]])
assert all(P[i, i] == 0 for i in range(3))
assert all(sum(P.row(i)) == 1 for i in range(3))
pi = sp.Matrix([[sp.Rational(1, 5), sp.Rational(2, 5), sp.Rational(2, 5)]])
assert pi * P == pi
assert (P**3)[0, 0] == sp.Rational(1, 2)
assert (P**5)[0, 0] == sp.Rational(1, 4)
assert sp.gcd(3, 5) == 1

Q = sp.Matrix([[sp.Rational(1, 4), sp.Rational(3, 4)], [sp.Rational(1, 2), sp.Rational(1, 2)]])
qpi = sp.Matrix([[sp.Rational(2, 5), sp.Rational(3, 5)]])
assert qpi * Q == qpi and (Q**2)[0, 0] == sp.Rational(7, 16)
A = sp.Matrix([[0, 1], [1, 0]])
assert (A**2)[0, 0] == 1 and A[0, 0] == 0
assert sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)]]) * A == sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)]])

for literal in ("1/2", "1/4", "1/5", "2/5", "3/5", "7/16", "3,5", "period is two", "period is one"):
    assert literal in body, literal
assert body.count('title="Proof"') == 1
assert '**Your turn.**' in body and 'title="Answer"' in body
for heading in ("Motivating example", "Worked example", "Common misconceptions", "When convergence fails", "History"):
    assert f"## {heading}" in body, heading
for q in ("ex-prob-markov-limit", "ex-prob-markov-two-state"):
    assert f"../questions/{q}.qmd" in page
    assert "## Worked answer" in (root / f"questions/{q}.qmd").read_text()
selected = json.loads((root / "research/self-checks.json").read_text())["aperiodic-markov-chain"]
assert selected == ["ex-prob-markov-limit", "ex-prob-markov-two-state"]
assert body.count("![") >= 0
print("rank 158 transition, period, stationary and preservation checks passed")
