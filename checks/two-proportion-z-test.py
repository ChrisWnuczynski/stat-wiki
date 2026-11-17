"""Recompute numerical examples and verify the generated article."""
from pathlib import Path
import math
import re
import numpy as np
from scipy import stats, integrate
ROOT=Path(__file__).resolve().parents[1]
SLUG='two-proportion-z-test'
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
def two(x1,n1,x2,n2):
 p=(x1+x2)/(n1+n2);se=np.sqrt(p*(1-p)*(1/n1+1/n2));z=(x1/n1-x2/n2)/se
 table=np.array([[x1,n1-x1],[x2,n2-x2]],float);expected=np.outer(table.sum(1),table.sum(0))/table.sum()
 pearson=np.sum((table-expected)**2/expected);close(pearson,z*z)
 close(stats.chi2.sf(pearson,1),2*stats.norm.sf(abs(z)))
 return p,se,z,2*stats.norm.sf(abs(z)),expected
p,se,z,pv,expected=two(60,100,75,150)
close([p,se,z,pv],[.54,.06434,1.5542,.1201],[1e-12,.000005,.00005,.00005])
close(expected,[[54,46],[81,69]])
un=np.sqrt(.6*.4/100+.5*.5/150);close(un,.06377,.000005)
close(.1+np.array([-1,1])*stats.norm.ppf(.975)*un,[-.025,.225],.00005)
_,_,zc,pc,ec=two(40,70,50,100)
close(ec,[[37.06,32.94],[52.94,47.06]],.005)
close(zc,.918,.0005);close(zc**2,.843,.0005);close(pc,.36,.005)
close(two(50,100,75,150)[2:4],[0,1])
shown('0.06434','1.5542','0.1201','0.06377','0.843')

p2,se2,z2,pv2,ex2=two(10,20,40,180)
close([p2,10/20,40/180,(10/20+40/180)/2,se2,z2,z2**2,pv2],[.25,.5,40/180,.3611111111111111,0.10206207261596575,2.721655269759087,7.407407407407407,0.00649558625717902],[1e-12,.0,.0,.0,5e-7,5e-7,5e-7,5e-7])
close(ex2,[[5,15],[45,135]])
unu=np.sqrt(.5*.5/20+(40/180)*(1-40/180)/180)
close(unu,.11601818598279322,5e-7)
diff=10/20-40/180
close(diff+np.array([-1,1])*1.96*unu,[0.050382133,0.505173422],.000001)
shown('0.250000','0.361111','2.721655','7.407407','0.006496','0.116018')
finish()
