"""Recompute numerical examples and verify the generated article."""
from pathlib import Path
import math
import re
import numpy as np
from scipy import stats, integrate
ROOT=Path(__file__).resolve().parents[1]
SLUG='the-limit-of-hotelling-s-statistic'
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
for n,tail in [(20,.084590643846611),(200,.052822909676996)]:
 transformed=(n-2)/(2*(n-1))*6
 close(stats.f.sf(transformed,2,n-2),tail,1e-13)
close(stats.chi2.sf(6,2),np.exp(-3));close(stats.chi2.ppf(.95,2),5.991464547108,1e-12)
for n in [20,200]:
 tail=stats.f.sf((n-2)/(2*(n-1))*5.991,2,n-2)
 close(tail,.085 if n==20 else .053,.0006)
S=np.array([[2,.6],[.6,1.]])
d=np.array([.3,-.2]);A=np.array([[1,2],[-.5,1]])
close(20*d@np.linalg.inv(S)@d,20*(A@d)@np.linalg.inv(A@S@A.T)@(A@d))
close((1-2/20)/(2*(1-1/20))*6,18*6/38)
shown('0.04979','0.08459','0.05282','5.991')

fcut=float(stats.f.ppf(.95,2,18))
assert f"{fcut:.6f}"=="3.554557"
assert f"{fcut*2*19/18:.6f}"=="7.504065"
shown('3.554557','7.504065','5.991465')
finish()
