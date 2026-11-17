"""Recompute numerical examples and verify the generated article."""
from pathlib import Path
import math
import re
import numpy as np
from scipy import stats, integrate
ROOT=Path(__file__).resolve().parents[1]
SLUG='extended-information-criterion'
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
n,p=120,8
score=lambda ll,edges,gamma:-2*ll+edges*np.log(n)+4*edges*gamma*np.log(p)
close(score(-290,10,0)-score(-300,7,0),-5.63752,.000005)
close(score(-290,10,.5)-score(-300,7,.5),6.83913,.00001)
gamma=(20/3-np.log(n))/(4*np.log(p));close(gamma,.22592,.000005)
close(score(-290,10,gamma),score(-300,7,gamma))
close((np.log(100)+4*.5*np.log(10))/2,4.60517,.000005)
S=.6**np.abs(np.arange(p)[:,None]-np.arange(p)[None,:]);precision=np.linalg.inv(S)
assert np.linalg.eigvalsh(S).min()>0
nonzero=np.abs(precision)>1e-10;close(np.count_nonzero(np.triu(nonzero,1)),7)
assert not np.any(np.abs(precision)[np.abs(np.arange(p)[:,None]-np.arange(p)[None,:])>1]>1e-10)
close(math.comb(p,2),28);grid=np.linspace(.02,.65,18);close([len(grid),grid[0],grid[-1]],[18,.02,.65])
shown('-5.63752','6.83913','0.22592','4.60517','28','18')
finish()
