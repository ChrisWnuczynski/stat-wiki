"""Recompute numerical examples and exercise answers for univariate-t-test-as-a-template-for-t2."""
import math
import numpy as np
from scipy import stats, special, linalg, integrate

x=np.array([8,9,10,11,12]);n=len(x);s2=x.var(ddof=1);t=(x.mean()-8)/math.sqrt(s2/n)
assert x.mean()==10 and s2==2.5 and np.isclose(t,2*math.sqrt(2)) and np.isclose(t*t,8)
c=stats.t.ppf(.975,4);assert round(c,6)==2.776445 and round(c*c,6)==7.708647
assert np.isclose(c*c,stats.f.ppf(.95,1,4)) and np.isclose(2*stats.t.sf(abs(t),4),stats.f.sf(t*t,1,4))
assert round(2*stats.t.sf(abs(t),4),6)==.047421
assert (3-1)/(2/3)==3 and 9*(3-1)**2/4==9
assert (-2)**2==4 and 12-1==11
print("univariate-t-test-as-a-template-for-t2: numerical checks passed")
