"""Check precision inverses, partial correlations and Gaussian-only limit."""

from math import isclose
from pathlib import Path
import sympy as sp

page = (Path(__file__).resolve().parents[1] / "articles/precision-matrix.qmd").read_text()
body = page.split("## See also", 1)[0]

sigma = sp.Matrix([[4, 2], [2, 3]])
assert sigma.det() == 8
k = sigma.inv()
assert k == sp.Matrix([[3, -2], [-2, 4]]) / 8
assert 1 / k[0, 0] == sp.Rational(8, 3)
assert -k[0, 1] / k[0, 0] == sp.Rational(2, 3)
assert isclose(float(-k[0, 1] / sp.sqrt(k[0, 0] * k[1, 1])), .5774, abs_tol=.00005)
sigma2 = sp.Matrix([[2, 1], [1, 2]])
assert sigma2.det() == 3
k2 = sigma2.inv()
assert k2 == sp.Matrix([[2, -1], [-1, 2]]) / 3
assert 1 / k2[0, 0] == sp.Rational(3, 2)
assert -k2[0, 1] / sp.sqrt(k2[0, 0] * k2[1, 1]) == sp.Rational(1, 2)
chain = sp.Matrix([[1, -sp.Rational(1, 2), 0], [-sp.Rational(1, 2), 1, -sp.Rational(1, 2)], [0, -sp.Rational(1, 2), 1]])
assert all(x > 0 for x in chain.eigenvals())
assert chain.inv()[0, 2] != 0 and chain[0, 2] == 0
assert -chain[0, 1] / sp.sqrt(chain[0, 0] * chain[1, 1]) == sp.Rational(1, 2)
z = sp.symbols('z', real=True)
assert sp.integrate(z**3 * sp.exp(-z**2 / 2) / sp.sqrt(2 * sp.pi), (z, -sp.oo, sp.oo)) == 0
assert sp.integrate(z**4 * sp.exp(-z**2 / 2) / sp.sqrt(2 * sp.pi), (z, -sp.oo, sp.oo)) - 1 == 2
assert sp.diag(1, 2).inv() == sp.diag(1, sp.Rational(1, 2))
for printed in ("4(3)-2^2=8", "8/3", "2/3", "0.5774", "3/2=1.5", "1/2=0.5", "0.6667", "1/2", "K_{13}=0"):
    assert printed in body, printed
for heading in ("## Motivating example", "## Intuition", "## Definition", "## Interpretation", "## Properties", "## Statistical use", "## Worked example", "## Common misconceptions", "## Assumptions and limits", "## Connections", "## History"):
    assert heading in body, heading
assert body.count('title="Proof"') == 1
assert "**Your turn.**" in body and 'title="Answer"' in body
for key in ("friedman_glasso2008", "dodge2008", "evans_graphical_models2025"):
    assert f'data-cite-key="{key}"' in body
assert "§5.1" in body
print("Precision inverses, conditional associations and preserved chain passed")
