"""Recompute numerical examples and verify the generated article."""
from pathlib import Path
import math
import re
import numpy as np
from scipy import stats, integrate
ROOT=Path(__file__).resolve().parents[1]
SLUG='training-data-and-classifier'
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
x=np.array([-2,-1,.1,1,2]);labels=np.array([1,1,1,2,2]);weights=np.array([.1,.1,.2,.3,.3])
def threshold(x,t=0):return np.where(x<t,1,2)
close(weights.sum(),1);close([np.dot(weights,threshold(x)!=labels),np.dot(weights,np.ones(5)!=labels)],[.2,.6])
train=np.array([0,1,3,4]);close([np.mean(threshold(x[train])!=labels[train]),np.mean(np.ones(4)!=labels[train])],[0,.5])
close([np.dot(weights,threshold(x,.5)!=labels),np.mean(threshold(x[train],.5)!=labels[train])],[0,0])
assert threshold(np.array([.1]))[0]==2
shown('0.2','0.6','0.5','0.1')
finish()
