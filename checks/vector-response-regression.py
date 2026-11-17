"""Recompute numerical examples and verify the generated article."""
from pathlib import Path
import math
import re
import numpy as np
from scipy import stats, integrate
ROOT=Path(__file__).resolve().parents[1]
SLUG='vector-response-regression'
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
p1,p2,odds=.3,.4,2
q=(1.7-np.sqrt(1.93))/2;cells=np.array([q,p1-q,p2-q,1-p1-p2+q])
assert np.all(cells>0);close(cells.sum(),1);close([cells[0]+cells[1],cells[0]+cells[2]],[p1,p2])
close(cells[0]*cells[3]/(cells[1]*cells[2]),odds)
close(cells,[.15538,.14462,.24462,.45538],.000005)
close(p1*p2,.12);close([max(0,.7+.6-1),min(.7,.6),.7*.6],[.3,.6,.42])
# A wrong invertible working covariance preserves mean-zero equations at the true mean.
outcomes=np.array([[1,1],[1,0],[0,1],[0,0]]);mean=np.array([p1,p2]);W=np.array([[2,.3],[.3,1.]])
close(cells@((outcomes-mean)@np.linalg.inv(W)),[0,0])
shown('0.15538','0.14462','0.24462','0.45538','0.42')
finish()
