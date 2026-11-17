"""Recompute numerical examples and verify the generated article."""
from pathlib import Path
import math
import re
import numpy as np
from scipy import stats, integrate
ROOT=Path(__file__).resolve().parents[1]
SLUG='wilks-theorem'
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
D=2*(60*np.log(1.2)+40*np.log(.8));close(D,4.02710,.000005)
close(stats.chi2.sf(D,1),.04477,.000005);close(stats.chi2.sf(4,1),.04550,.000005)
close(stats.chi2.cdf(.08,3),.006,.0005);close(stats.chi2.ppf(.05,3),.352,.0005)
close(stats.chi2.ppf(.9,1),2.70554,.000005)
close(.5*stats.chi2.sf(stats.chi2.ppf(.9,1),1),.05)
# Exact normal likelihood ratio from the fitted and null residual sums of squares.
x=np.array([0.,1,1,2,3]);n=len(x);mu0=0.;sse=np.sum((x-x.mean())**2);sse0=np.sum((x-mu0)**2)
tstat=np.sqrt(n)*(x.mean()-mu0)/np.sqrt(sse/(n-1))
close(n*np.log(sse0/sse),n*np.log1p(tstat*tstat/(n-1)))
O=np.array([12.,18,20,30]);E=np.array([10.,20,25,25])
close(np.sum((2*O-2*E)**2/(2*E)),2*np.sum((O-E)**2/E))
shown('4.02710','0.04477','0.04550','2.70554','0.352','0.08')
finish()
