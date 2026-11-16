"""Check feature-kernel Gram calculations and final-page structure."""

from math import isclose, log, sqrt
from pathlib import Path
import numpy as np
import sympy as sp

root = Path(__file__).resolve().parents[1]
body = (root / 'articles/kernel.qmd').read_text().split('## See also', 1)[0]

# Inherited quadratic feature map and non-kernel counterexample.
u = sp.Matrix([1, 1]); v = sp.Matrix([2, 0])
phi = lambda x: sp.Matrix([x[0]**2, sp.sqrt(2)*x[0]*x[1], x[1]**2])
assert (u.dot(v))**2 == 4 == phi(u).dot(phi(v))
assert -u.dot(u) == -2 < 0
# Gaussian numeric worked example.
G = np.array([[1.0, np.exp(-log(2))], [np.exp(-log(2)), 1.0]])
assert np.allclose(G, [[1,.5],[.5,1]])
assert np.allclose(np.linalg.eigvalsh(G), [.5,1.5])
assert isclose(np.linalg.det(G), .75)
# Polynomial hidden answer; feature map proves all finite Gram matrices PSD.
x = sp.symbols('x', real=True); z = sp.symbols('z', real=True)
assert sp.expand((1+x*z)**2) == sp.expand(sp.Matrix([1,sp.sqrt(2)*x,x*x]).dot(sp.Matrix([1,sp.sqrt(2)*z,z*z])))
H = sp.Matrix([[1,1],[1,4]])
assert H.det() == 3
assert sorted(round(float(e),6) for e in H.eigenvals()) == [.697224,4.302776]
L = sp.Matrix([[1,-1],[-1,1]])
assert sorted(L.eigenvals()) == [0,2]
for printed in ('1/2', '3/2', '3/4', '4.302776', '0.697224', 'determinant $3'):
    assert printed in body, printed
assert body.count('![') == 0
assert body.count('title="Proof"') == 1
assert '## Motivating example' in body and '## Worked example' in body
assert '**Your turn.**' in body and 'title="Answer"' in body
assert 'data-cite-key="scholkopf_smola2003_intro"' in body
print('kernel arithmetic and practice passed')
