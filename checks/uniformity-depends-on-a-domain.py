"""Recompute numerical examples and verify the generated article."""
from pathlib import Path
import math
import re
import numpy as np
from scipy import stats, integrate
ROOT=Path(__file__).resolve().parents[1]
SLUG='uniformity-depends-on-a-domain'
body=(ROOT/"articles"/f'{SLUG}.qmd').read_text().split('## See also',1)[0]
def close(a,b,atol=1e-10):
    aa,bb,tt=np.broadcast_arrays(np.asarray(a),np.asarray(b),np.asarray(atol))
    for x,y,tol in zip(aa.flat,bb.flat,tt.flat):
        np.testing.assert_allclose(x,y,rtol=0,atol=float(tol))
def shown(*values):
    for value in values:
        assert value in body, (SLUG,value)
def finish():
    assert '**Your turn.**' in body
    assert '## Check yourself' in body
    assert body.count('data-cite-key=')>=5
    assert len(set(re.findall(r'data-cite-key="([^" ]+)"',body)))>=2
    assert not any(ord(c)<32 and c not in '\n\r\t' for c in body)
    print(SLUG+': numerical examples and article checks passed')
import sympy as sp
a,b=sp.symbols('a b',positive=True);t=a+b
J=sp.Matrix([a/t,t**sp.Rational(-1,2)]).jacobian([a,b]).det()
assert sp.simplify(J+sp.Rational(1,2)*t**sp.Rational(-5,2))==0
close(integrate.quad(lambda v:v**-2,1,2)[0],.5)
close(np.sqrt(2)-1,.41421,.000005)
close(integrate.quad(lambda t:.5*t**-1.5,.25,1)[0],1)
close(integrate.quad(lambda v:.5*v**-2,2,4)[0],1/8)
close([4**-2,2**-2],[1/16,1/4])
# Gamma shape-two concentration follows from two iid exponentials by a Jacobian t.
close(integrate.quad(lambda t:t*np.exp(-t),0,np.inf)[0],1)
shown('0.41421','1/16','1/8','1/4')
finish()
