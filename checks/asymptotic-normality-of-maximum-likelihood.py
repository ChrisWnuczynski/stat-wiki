"""Recompute numerical examples and verify the generated article."""
from pathlib import Path
import math
import re
import numpy as np
from scipy import stats, integrate
ROOT=Path(__file__).resolve().parents[1]
SLUG='asymptotic-normality-of-maximum-likelihood'
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
p=sp.symbols('p',positive=True);k,n=sp.symbols('k n',positive=True)
ell=k*sp.log(p)+(n-k)*sp.log(1-p)
assert sp.simplify(sp.diff(ell,p)-(k-n*p)/(p*(1-p)))==0
phat=70/200;se=np.sqrt(phat*(1-phat)/200);ci=phat+np.array([-1,1])*stats.norm.ppf(.975)*se
close(se,.03373,.000005);close(ci,[.28390,.41610],.000005);close(200/(phat*(1-phat)),879.12088,.000005)
# Run the copied Newton loop and compare its iterates with the actual Poisson root.
x=np.array([0,2,1,4,1,0,3]);n=len(x);s=x.sum();lam=1.
for _ in range(5):lam+=(s/lam-n)/(s/lam**2)
close([n,s,x.mean(),lam],[7,11,11/7,11/7],1e-10)
close(.5+np.array([-1,1])*stats.norm.ppf(.975)*.05,[.40200,.59800],.000005)
# At theta=0, the thresholded estimator is zero with increasing probability.
for sample_n in [100,10000]:
 prob=2*stats.norm.cdf(sample_n**.25)-1
 assert prob>.99
assert "S"+chr(39)*3+"(" not in body
shown('0.03373','879.12088','0.28390','0.41610','11/7','0.40200')
finish()
