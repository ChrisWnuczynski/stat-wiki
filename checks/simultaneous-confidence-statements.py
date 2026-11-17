"""Recompute numerical examples and exercise answers for simultaneous-confidence-statements."""
import math
import numpy as np
from scipy import stats, special, linalg, integrate

S=np.array([[4.,1],[1,9]]);C=.2*S;c=18*2/17*stats.f.ppf(.95,2,17)
assert round(c,6)==7.605594
assert np.allclose(np.round(np.sqrt(c*np.diag(C)),6),[2.466673,3.700009])
a=np.ones(2);assert a@C@a==3 and round(math.sqrt(c*a@C@a),6)==4.776692
assert math.sqrt(9*4)==6 and round(math.sqrt(45),6)==6.708204
for a in [np.array([1.,0]),np.array([1.,1]),np.array([2.,-1])]:
 h=math.sqrt(c)*C@a/math.sqrt(a@C@a)
 assert np.isclose(h@np.linalg.solve(C,h),c) and np.isclose(a@h,math.sqrt(c*a@C@a))
assert math.isclose(3*(.05/3),.05)
print("simultaneous-confidence-statements: numerical checks passed")
