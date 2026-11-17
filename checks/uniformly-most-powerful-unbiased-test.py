"""Recompute numerical examples and verify the generated article."""
from pathlib import Path
import math
import re
import numpy as np
from scipy import stats, integrate
ROOT=Path(__file__).resolve().parents[1]
SLUG='uniformly-most-powerful-unbiased-test'
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
a=.05;c=stats.norm.ppf(1-a/2);one=stats.norm.ppf(1-a)
power=lambda d:stats.norm.sf(c-d)+stats.norm.cdf(-c-d)
close([c,one,power(1),stats.norm.sf(one-1),stats.norm.sf(one+1)],[1.95996398454,1.64485362695,.170075045753,.259511022841,.004086313060],1e-11)
for d in np.linspace(-5,5,51):assert power(d)>=a-1e-14
close(stats.t.ppf([.975,.95],41),[2.01954097,1.68287800],1e-8)
close(2*stats.t.sf(stats.t.ppf(.95,41),41),.1)
# The chord inequality supporting the UMPU proof, checked on both shift directions.
zs=np.linspace(-8,8,1001)
for delta in [-2,-.5,.5,2]:
 ylo,yhi=np.exp(-delta*c),np.exp(delta*c);slope=(yhi-ylo)/(2*c);intercept=(ylo+yhi)/2
 residual=np.exp(delta*zs)-slope*zs-intercept
 assert np.all(residual[np.abs(zs)>c]>=-1e-12)
 assert np.all(residual[np.abs(zs)<c]<=1e-12)
close(integrate.quad(lambda z:z*stats.norm.pdf(z),c,np.inf)[0]+integrate.quad(lambda z:z*stats.norm.pdf(z),-np.inf,-c)[0],0)
shown('0.17008','0.25951','0.00409','2.01954','1.68288','0.10')
finish()
