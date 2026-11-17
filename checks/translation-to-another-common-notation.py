"""Recompute numerical examples and verify the generated article."""
from pathlib import Path
import math
import re
import numpy as np
from scipy import stats, integrate
ROOT=Path(__file__).resolve().parents[1]
SLUG='translation-to-another-common-notation'
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
lam=3;eta=np.log(lam);A=np.exp(eta);x=2
close(A,3);close(np.exp(x*eta-A)/math.factorial(x),stats.poisson.pmf(x,lam))
close(stats.poisson.pmf(2,3),.22404,.000005)
close([np.exp(eta)/(1+np.exp(eta)),np.log1p(np.exp(eta))],[.75,np.log(4)])
close(stats.poisson.pmf(0,2),.13534,.000005)
# Symbolic derivatives distinguish natural from mean parameters.
import sympy as sp
e,l=sp.symbols('e l',real=True)
assert sp.diff(sp.exp(e),e,2)==sp.exp(e)
assert sp.diff(l,l,2)==0
v=sp.symbols('v',positive=True)
assert sp.diff(sp.log(2*sp.pi*v)/2,v,2)==-1/(2*v**2)
shown('0.22404','0.13534','\\log4','\\log3')
finish()
