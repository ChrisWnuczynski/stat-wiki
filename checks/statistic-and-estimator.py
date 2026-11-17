"""Recompute numerical examples and verify the generated article."""
from pathlib import Path
import math
import re
import numpy as np
from scipy import stats, integrate
ROOT=Path(__file__).resolve().parents[1]
SLUG='statistic-and-estimator'
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
x=np.array([1,0,1,1]);k=x.sum();n=len(x)
close([k,x.mean(),x.var(ddof=1),(k+1)/(n+2)],[3,.75,.25,2/3])
for p in np.linspace(0,1,21):
 ks=np.arange(n+1);pr=stats.binom.pmf(ks,n,p)
 estimates=[ks/n,(ks+1)/(n+2)]
 means=[np.dot(pr,e) for e in estimates]
 risks=[np.dot(pr,(e-p)**2) for e in estimates]
 close(means,[p,(n*p+1)/(n+2)])
 close(risks,[p*(1-p)/n,p*(1-p)/9+((1-2*p)/6)**2])
close([.5*.5/4,.5*.5/9,(1/6)**2],[1/16,1/36,1/36])
y=np.array([0,0,1,0]);close([y.mean(),(y.sum()+1)/6],[1/4,1/3])
shown('1/16','1/36','3/4','2/3')
finish()
