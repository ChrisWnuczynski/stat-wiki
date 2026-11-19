"""Verify score calculations, proof structure and original links."""

import json
import math
from pathlib import Path
import sympy as sp

root = Path(__file__).resolve().parents[1]
page = (root / "articles/score-function.qmd").read_text()
body = page.split("## See also", 1)[0]
pending = {'self_checks': json.loads((root / 'research/self-checks.json').read_text())['score-function']}

beta = sp.symbols("beta", real=True)
p = 1 / (1 + sp.exp(-beta))
ll = 2 * sp.log(p) + sp.log(1 - p)
score = sp.diff(ll, beta)
hessian = sp.diff(score, beta)
assert sp.simplify(score - (2 - 3 * p)) == 0
assert sp.simplify(hessian + 3 * p * (1 - p)) == 0
assert score.subs(beta, 0) == sp.Rational(1, 2)
assert hessian.subs(beta, 0) == -sp.Rational(3, 4)
assert -score.subs(beta, 0) / hessian.subs(beta, 0) == sp.Rational(2, 3)
assert sp.simplify(score.subs(beta, sp.log(2))) == 0
assert round(float(sp.log(2)), 4) == .6931
assert round(float(score.subs(beta, sp.Rational(2, 3))), 4) == .0177
ll4 = sp.log(p) + 3 * sp.log(1 - p)
assert sp.diff(ll4, beta).subs(beta, 0) == -1
assert sp.diff(ll4, beta, 2).subs(beta, 0) == -1
assert sp.simplify(sp.diff(ll4, beta).subs(beta, sp.log(sp.Rational(1, 3)))) == 0
assert round(math.log(1 / 3), 4) == -1.0986
for printed in ("0.5", "-0.75", "0.6667", "0.6931", "0.0177", "-1.0986"):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert "{#motivating-example}" in body and "{#worked-example}" in body
assert "**Your turn.**" in body and 'title="Answer"' in body
assert pending["self_checks"] == ["q-33", "q-56"]
for q in pending["self_checks"]:
    assert (root / "questions" / f"{q}.qmd").exists()
for q in ("q-33", "q-45", "q-54", "q-56", "c-18"):
    assert f"../questions/{q}.qmd" in page
for key in ("nelder_wedderburn1972", "albert_anderson1984", "dodge2008"):
    assert f'data-cite-key="{key}"' in body
assert json.loads((root / "research/baseline.json").read_text())["score-function"]["figures"] == 0
print("score identities, examples and original links passed")
