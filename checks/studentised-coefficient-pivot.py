"""Recompute numerical examples and verify the generated article."""
from pathlib import Path
import math
import re
import numpy as np
from scipy import stats, integrate
ROOT=Path(__file__).resolve().parents[1]
SLUG='studentised-coefficient-pivot'
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
n,p,sse,c,bhat=8,3,20,.25,1.5
s2=sse/(n-p);se=np.sqrt(s2*c)
close([s2,se,(bhat-.5)/se],[4,1,1])
close([2*stats.t.sf(1,5),2*stats.t.sf(1.5,5)],[.363217467649,.193903680242],1e-12)
q=stats.t.ppf(.975,5);close(q,2.570581835636,1e-12)
close([bhat-q*se,bhat+q*se],[-1.070581835636,4.070581835636],1e-12)
# Verify the orthogonal projection identities for a concrete full-rank design.
X=np.column_stack([np.ones(8),np.arange(8),np.arange(8)**2])
C=np.linalg.inv(X.T@X);H=X@C@X.T
close(H@H,H);close(X.T@(np.eye(8)-H),np.zeros((3,8)))
close(np.linalg.eigvalsh(np.eye(8)-H),[0,0,0,1,1,1,1,1])
shown('0.3632','0.1939','2.5706','## Statement')
assert 'title="Proof"' in body

den=2*np.sqrt(.5); tstat=1.2/den
close([den,tstat,2*stats.t.sf(tstat,5)],[np.sqrt(2),0.8485281374238569,0.4348746270959881])
shown('0.848528','0.434875','1.414214')
finish()
