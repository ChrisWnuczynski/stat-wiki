"""Recompute numerical examples and verify the generated article."""
from pathlib import Path
import math
import re
import numpy as np
from scipy import stats, integrate
ROOT=Path(__file__).resolve().parents[1]
SLUG='bayes-factors-and-posterior-odds'
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
m0=.5**4;m1=integrate.quad(lambda p:p**3*(1-p),0,1)[0]
close([m0,m1,m1/m0],[1/16,1/20,4/5])
prior=.25;odds=prior/(1-prior)*(m1/m0);post=odds/(1+odds)
close([odds,post],[4/15,4/19]);close(post,.21053,.000005)
close((.5*m1)/(.5*m1+.5*m0),4/9)
close((math.comb(4,3)*m1)/(math.comb(4,3)*m0),4/5)
# Arbitrary improper-prior constants cancel in a parameter posterior but not in m1/m0.
for constant in [.1,10]:close((constant*m1)/(m0),constant*(4/5))
shown('1/20','4/5','4/15','0.21053','4/9')
finish()
