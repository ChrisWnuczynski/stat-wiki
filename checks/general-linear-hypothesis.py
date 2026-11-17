"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

x=np.arange(1,5);y=np.array([2,3,5,6]);X=np.c_[np.ones(4),x];b=np.linalg.lstsq(X,y,rcond=None)[0]
assert np.allclose(b,[.5,1.4])
rss1=sum((y-X@b)**2);rss0=sum((y-y.mean())**2)
assert math.isclose(rss1,.2) and rss0==10 and math.isclose((rss0-rss1)/(rss1/2),98)
assert round(stats.f.ppf(.95,1,2),1)==18.5
assert ((70-52)/2)/(52/26)==4.5
print('joint p',stats.f.sf(4.5,2,26),'exercise p',stats.f.sf(4,1,17))
assert (42-34)/(34/17)==4
P=X@np.linalg.inv(X.T@X)@X.T;P0=np.ones((4,4))/4
assert np.allclose((P-P0)@(np.eye(4)-P),0)
assert round(stats.f.sf(4.5,2,26),5)==.02098 and round(stats.f.sf(4,1,17),4)==.0617
print("general-linear-hypothesis: numerical checks passed")
