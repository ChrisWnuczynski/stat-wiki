"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

p=np.array([stats.poisson.pmf(n,2) for n in range(3)]);d=2*(np.r_[0,p[:-1]]-p)
assert np.allclose(p,[.13534,.27067,.27067],atol=5e-6)
assert np.allclose(d,[-.27067,-.27067,0],atol=5e-6)
p0=math.exp(-1.5);p1=1.5*p0
assert round(p1,5)==.33470 and math.isclose(3*(p0-p1),-p1)
for rate,time in [(2,1),(3,.5),(1,.2)]:
 for n in range(1,8):
  eps=1e-5;fd=(stats.poisson.pmf(n,rate*(time+eps))-stats.poisson.pmf(n,rate*(time-eps)))/(2*eps)
  rhs=rate*(stats.poisson.pmf(n-1,rate*time)-stats.poisson.pmf(n,rate*time))
  assert math.isclose(fd,rhs,abs_tol=1e-8)
from scipy.special import factorial
for m in [.2,2,1.5]:
 n=np.arange(100);pr=stats.poisson.pmf(n,m)
 assert math.isclose(np.dot(n,pr),m) and math.isclose(np.dot(n*(n-1),pr),m*m)
 assert math.isclose(np.dot((n-m)**2,pr),m)
print("forward-equations-of-the-poisson-process: numerical checks passed")
