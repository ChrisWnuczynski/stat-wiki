"""Recompute numerical examples and verify the generated article."""
from pathlib import Path
import math
import re
import numpy as np
from scipy import stats, integrate
ROOT=Path(__file__).resolve().parents[1]
SLUG='axioms-of-probability'
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
weights=np.array([.1,.2,.3,.4]);A=np.array([True,True,False,False]);B=np.array([False,True,True,False])
close(weights.sum(),1)
close([weights[A].sum(),weights[B].sum(),weights[A&B].sum(),weights[A|B].sum(),weights[~A].sum(),weights[A^B].sum()],[.3,.5,.2,.6,.7,.4])
for N in [1,3,10,30]:
 close(sum(2.**-k for k in range(1,N+1)),1-2.**-N)
close(2.**-3,1/8)
# Fair die and uniform-interval examples copied by the renderer.
close(np.ones(6).sum()/6,1);close(integrate.quad(lambda x:1,0,1)[0],1)
close(.5+.5*integrate.quad(lambda x:1,0,1)[0],1)
shown('0.6','0.7','0.4','1/8','are rules')
finish()
