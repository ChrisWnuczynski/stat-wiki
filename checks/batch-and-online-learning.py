"""Recompute numerical examples and verify the generated article."""
from pathlib import Path
import math
import re
import numpy as np
from scipy import stats, integrate
ROOT=Path(__file__).resolve().parents[1]
SLUG='batch-and-online-learning'
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
y=np.array([0.,2,4]);w=1.;grad=w-y
close(grad,[1,-1,-3]);close([grad.mean(),grad.sum()],[-1,-3])
L=lambda w:np.mean((w-y)**2)/2
full=w-.1*grad.mean();single=w-.1*grad[0]
close([full,single,L(w),L(full),L(single)],[1.1,.9,11/6,1.738333333333333,1.938333333333333])
close(grad.var(),8/3)
from itertools import product,combinations
close(np.var([np.mean(v) for v in product(grad,repeat=2)]),4/3)
close(np.var([np.mean(v) for v in combinations(grad,2)]),2/3)
close([1-.1*grad.sum(),1-(1/30)*grad.sum()],[1.3,1.1])
shown('1.73833','1.93833','8/3','4/3','2/3','1/30')
finish()
