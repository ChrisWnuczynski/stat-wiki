"""Recompute numerical examples and verify the generated article."""
from pathlib import Path
import math
import re
import numpy as np
from scipy import stats, integrate
ROOT=Path(__file__).resolve().parents[1]
SLUG='surrogate-split'
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
primary=np.array([0]*6+[1]*2);surrogate=primary.copy();surrogate[0]=1
agreement=np.mean(primary==surrogate);baseline=max(np.mean(primary==0),np.mean(primary==1))
close([agreement,baseline,(agreement-baseline)/(1-baseline)],[.875,.75,.5])
close([18/20,11/20],[.9,.55]);close((.8-.5)/(1-.5),.6)
assert np.mean(primary==np.zeros(8))==baseline
shown('0.875','0.75','0.5','0.6','usesurrogate','maxsurrogate')

# Reversing a perfect mismatch produces agreement 1.
opposite=1-primary
close([np.mean(primary==opposite),np.mean(primary==(1-opposite))],[0,1])
close((.9-.55)/(1-.55),7/9)
shown('0.777778','8/8')
finish()
