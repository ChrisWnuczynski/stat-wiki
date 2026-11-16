"""Verify Markov examples, source preservation and theorem structure."""

import json
from pathlib import Path
import sympy as sp

root = Path(__file__).resolve().parents[1]
page = (root / "articles/finite-state-markov-chain.qmd").read_text()
body = page.split("## See also", 1)[0]
pending = {'self_checks': json.loads((root / 'research/self-checks.json').read_text())['finite-state-markov-chain']}

P = sp.Matrix([
    [0, sp.Rational(1, 3), 0, sp.Rational(1, 3), sp.Rational(1, 3), 0],
    [sp.Rational(1, 2), 0, sp.Rational(1, 2), 0, 0, 0],
    [sp.Rational(1, 2), 0, 0, sp.Rational(1, 2), 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, sp.Rational(1, 2), 0, sp.Rational(1, 2)],
    [0, 0, sp.Rational(1, 2), 0, sp.Rational(1, 2), 0],
])
assert list((P ** 2).row(0)) == [sp.Rational(1, 6), 0, sp.Rational(1, 6), sp.Rational(1, 6), 0, sp.Rational(1, 2)]
pi = sp.Matrix([[12, 4, 20, 25, 22, 36]]) / 119
assert pi * P == pi and sum(pi) == 1
assert round(float((P ** 10)[0, 0]), 4) == .1049
assert all(round(float((P ** 100)[i, j]), 4) == round(float(pi[j]), 4) for i in range(6) for j in range(6))
weather = sp.Matrix([[sp.Rational(8, 10), sp.Rational(2, 10)], [sp.Rational(4, 10), sp.Rational(6, 10)]])
assert weather ** 2 == sp.Matrix([[sp.Rational(72, 100), sp.Rational(28, 100)], [sp.Rational(56, 100), sp.Rational(44, 100)]])
assert sp.Matrix([[sp.Rational(2, 3), sp.Rational(1, 3)]]) * weather == sp.Matrix([[sp.Rational(2, 3), sp.Rational(1, 3)]])
machine = sp.Matrix([[sp.Rational(9, 10), sp.Rational(1, 10)], [sp.Rational(3, 10), sp.Rational(7, 10)]])
assert machine ** 2 == sp.Matrix([[sp.Rational(84, 100), sp.Rational(16, 100)], [sp.Rational(48, 100), sp.Rational(52, 100)]])
assert sp.Matrix([[sp.Rational(3, 4), sp.Rational(1, 4)]]) * machine == sp.Matrix([[sp.Rational(3, 4), sp.Rational(1, 4)]])
for printed in ("0.84", "0.75", "0.25", "0.48", "0.52", "0.1049"):
    assert printed in body, printed
assert "0.56" in (root / "notes/prob-06-markov-chains.qmd").read_text()
assert page.count("![") >= 2
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
assert pending["self_checks"] == ["ex-prob-markov-limit", "ex-prob-markov-periodic"]
for q in pending["self_checks"]:
    assert (root / "questions" / f"{q}.qmd").exists()
for key in ("levin_peres2017", "dodge2008"):
    assert f'data-cite-key="{key}"' in body
for unread in ("markov1906", "feller1968", "norris1997", "grimmett_stirzaker2020", "ross2019"):
    assert f'data-cite-key="{unread}"' not in body
assert json.loads((root / "research/baseline.json").read_text())["finite-state-markov-chain"]["figures"] == 2
print("finite-state chain calculations and preservation passed")
