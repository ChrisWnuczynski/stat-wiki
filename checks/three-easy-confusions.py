"""Recompute numerical examples and verify the generated article."""
from pathlib import Path
import math
import re
import numpy as np
from scipy import stats, integrate
ROOT=Path(__file__).resolve().parents[1]
SLUG='three-easy-confusions'
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
n,p,sse=12,3,18
shape,rate=(n-p)/2,sse/2
close([shape,rate,stats.invgamma.mean(shape,scale=rate)],[4.5,9,18/7])
close([n/2,24/2],[6,12]);close([2*.25,np.sqrt(.5)],[.5,1/np.sqrt(2)])
close(stats.t.var(9,scale=np.sqrt(.5)),.5*9/7)
close([(10-2)/2,16/2,stats.invgamma.mean(4,scale=8)],[4,8,8/3])
# Integrate the coefficient kernel at two v values; its v^(p/2) factor is explicit.
for v in [1.,2.]:
 integral=integrate.quad(lambda z:np.exp(-z*z/(2*v)),-np.inf,np.inf)[0]**3
 close(integral,(2*np.pi*v)**(3/2))
shown('4.5','18/7','2.5714','8/3')
finish()
