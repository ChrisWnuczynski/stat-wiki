"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

o=np.array([[67,41,6],[129,183,32]]);e=o.sum(1)[:,None]*o.sum(0)[None,:]/o.sum();t=sum(((o-e)**2/e).flat)
assert o.sum()==458 and np.all(o.sum(1)==[114,344])
assert np.allclose(e,[[48.79,55.76,9.46],[147.21,168.24,28.54]],atol=.01)
assert round(t,2)==15.94 and round(stats.chi2.sf(t,2),6)==.000346
assert round(67/114,4)==.5877 and 129/344==.375
z=np.array([[20,30],[30,70]]);ee=z.sum(1)[:,None]*z.sum(0)[None,:]/z.sum();tt=np.sum((z-ee)**2/ee)
assert math.isclose(tt,1.5) and round(stats.chi2.sf(tt,1),4)==.2207
assert round(t,4)==15.9364
assert np.allclose(np.round((o-e)**2/e,2),[[6.80,3.90,1.26],[2.25,1.29,.42]])
print("contingency-tables: numerical checks passed")
