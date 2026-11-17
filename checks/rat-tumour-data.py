"""Recompute numerical examples and exercise answers for rat-tumour-data."""
import math
import numpy as np
from scipy import stats, special, linalg, integrate

from scipy import optimize
fractions='0/20 0/20 0/20 0/20 0/20 0/20 0/20 0/19 0/19 0/19 0/19 0/18 0/18 0/17 1/20 1/20 1/20 1/20 1/19 1/19 1/18 1/18 2/25 2/24 2/23 2/20 2/20 2/20 2/20 2/20 2/20 1/10 5/49 2/19 5/46 3/27 2/17 7/49 7/47 3/20 3/20 2/13 9/48 10/50 4/20 4/20 4/20 4/20 4/20 4/20 4/20 10/48 4/19 4/19 4/19 5/22 11/46 12/49 5/20 5/20 6/23 5/19 6/22 6/20 6/20 6/20 16/52 15/47 15/46 9/24'
y,n=np.array([[int(t) for t in f.split('/')] for f in fractions.split()]).T
assert len(y)==70 and y.sum()==263 and n.sum()==1725
assert round((y/n).mean(),6)==.136007 and round((y/n).std(ddof=1),6)==.103492
assert round(y.sum()/n.sum(),6)==.152464
f=lambda q:-np.sum(special.betaln(y+np.exp(q[0]),n-y+np.exp(q[1]))-special.betaln(*np.exp(q)))
def grad(q):
 a,b=np.exp(q);common=special.digamma(a+b+n)-special.digamma(a+b)
 return -np.array([a*np.sum(special.digamma(a+y)-special.digamma(a)-common),b*np.sum(special.digamma(b+n-y)-special.digamma(b)-common)])
fit=optimize.minimize(f,np.log([2,12]),jac=grad,method='BFGS',options={'gtol':1e-8})
a,b=np.exp(fit.x);assert np.linalg.norm(grad(fit.x))<1e-6
assert np.allclose([a,b],[2.3048,14.0798],atol=.0001)
assert round((a+4)/(a+b+14),5)==.20750
assert (2+4)/(2+8+14)==.25 and (2+1)/(2+8+10)==.15
assert np.isclose(14/24*4/14+10/24*.2,.25)
print('historical MLE',a,b,'current conditional mean',(a+4)/(a+b+14))
assert (2+0)/(2+8+10)>0
print("rat-tumour-data: numerical checks passed")
