"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

o=np.array([584,398,168,35,15]); raw=np.array([584,398,168,35,9,4,0,1,0,1])
assert sum(raw)==1200 and np.dot(raw,np.arange(10))==911
lam=911/1200; e=np.r_[1200*stats.poisson.pmf(np.arange(4),lam),1200*stats.poisson.sf(3,lam)]
assert np.allclose(e,[561.67,426.40,161.85,40.96,9.12],atol=.01)
assert round(sum((o-e)**2/e),2)==7.67
fit=optimize.minimize_scalar(lambda x:-np.dot(o,np.r_[stats.poisson.logpmf(np.arange(4),x),stats.poisson.logsf(3,x)]),bounds=(.1,2),method='bounded')
l=fit.x; e2=np.r_[1200*stats.poisson.pmf(np.arange(4),l),1200*stats.poisson.sf(3,l)]
print('Grouped Poisson:',l,e2,sum((o-e2)**2/e2),stats.chi2.sf(sum((o-e2)**2/e2),3))
assert round(l,4)==.7512
assert round(stats.chi2.sf(4,1),4)==.0455 and round(stats.chi2.sf(4,2),4)==.1353
assert sum((np.array([30,40,30])-np.array([25,50,25]))**2/np.array([25,50,25]))==4
assert round(sum((o-e2)**2/e2),4)==7.7362 and round(stats.chi2.sf(sum((o-e2)**2/e2),3),5)==.05179
assert np.allclose(e2,[566.13,425.31,159.75,40.00,8.80],atol=.005)
assert round(stats.poisson.pmf(4,lam)*1200,2)==7.77 and round(stats.poisson.pmf(5,lam)*1200,2)==1.18
assert stats.poisson.pmf(6,lam)*1200<.2
assert round(stats.chi2.sf(sum((o-e)**2/e),3),3)==.053 and round(stats.chi2.ppf(.95,3),3)==7.815
print("chi-squared-test-with-estimated-parameters: numerical checks passed")
