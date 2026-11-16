"""Check Markov conditioning example and retained source quantities."""

import json
from pathlib import Path
import sympy as sp

root = Path(__file__).resolve().parents[1]
page = (root / "articles/markov-property.qmd").read_text()
body = page.split("## See also", 1)[0]
pending = json.loads((root / "research/pending/markov-property.json").read_text())

P2 = sp.Matrix([[sp.Rational(8, 10), sp.Rational(2, 10)], [sp.Rational(4, 10), sp.Rational(6, 10)]])
initial = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)]])
assert (initial * P2)[0] == sp.Rational(6, 10)
assert (P2 ** 2)[1, 0] == sp.Rational(56, 100)
assert (P2 ** 2)[0, 1] == sp.Rational(28, 100)
assert P2[0, 0] == sp.Rational(8, 10) and P2[1, 1] == sp.Rational(6, 10)
assert sp.Rational(2, 10) != sp.Rational(8, 10)  # same current state, differing previous states
P6 = sp.Matrix([
    [0, sp.Rational(1, 3), 0, sp.Rational(1, 3), sp.Rational(1, 3), 0],
    [sp.Rational(1, 2), 0, sp.Rational(1, 2), 0, 0, 0],
    [sp.Rational(1, 2), 0, 0, sp.Rational(1, 2), 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, sp.Rational(1, 2), 0, sp.Rational(1, 2)],
    [0, 0, sp.Rational(1, 2), 0, sp.Rational(1, 2), 0],
])
assert list((P6 ** 2).row(0)) == [sp.Rational(1, 6), 0, sp.Rational(1, 6), sp.Rational(1, 6), 0, sp.Rational(1, 2)]
assert round(float((P6 ** 10)[0, 0]), 4) == .1049
assert sp.Matrix([[12, 4, 20, 25, 22, 36]]) * P6 == sp.Matrix([[12, 4, 20, 25, 22, 36]])
for printed in ("0.5", "0.6", "0.8", "0.56", "0.28", "0.2", "0.1049"):
    assert printed in body, printed
assert page.count("![") >= 1
assert body.count('title="Proof"') == 1
assert "## Motivating example" in body and "## Worked example" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
assert pending["self_checks"] == ["c-12", "ex-prob-markov-two-steps"]
for q in pending["self_checks"]:
    assert "## Worked answer" in (root / "questions" / f"{q}.qmd").read_text()
assert "../questions/c-12.qmd" in page
for key in ("levin_peres2017", "dodge2008"):
    assert f'data-cite-key="{key}"' in body
for unread in ("markov1906", "feller1968", "norris1997", "grimmett_stirzaker2020", "ross2019", "chapman1928", "kolmogorov1931"):
    assert f'data-cite-key="{unread}"' not in body
assert json.loads((root / "research/baseline.json").read_text())["markov-property"]["figures"] == 1
print("Markov property probabilities and preservation passed")
