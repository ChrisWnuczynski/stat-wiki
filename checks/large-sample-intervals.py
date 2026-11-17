"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

n,mean,s=51,1136,178
se=s/math.sqrt(n);close(se,24.9249854957)
h=1.96*se;close(h,48.8529715716)
close([mean-h,mean+h],[1087.1470284284,1184.8529715716])
q=stats.t.ppf(.975,50);close(q,2.0085591121)
close([mean-q*se,mean+q*se],[1085.9366932636,1186.0633067364])
close((1.96*178/25)**2,194.74760704);assert math.ceil((1.96*178/25)**2)==195
close([20-1.96*5/10,20+1.96*5/10],[19.02,20.98])
close(1.96*5/math.sqrt(400),.49)
print("large-sample-intervals: numerical checks passed")
