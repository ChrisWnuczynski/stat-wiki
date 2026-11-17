"""Recompute the mathematical claims and printed values for pearson-chi-squared-approximation."""
from pathlib import Path
import math
import numpy as np
from scipy import stats,integrate,special
ROOT=Path(__file__).resolve().parents[1]
article=(ROOT/"articles"/"pearson-chi-squared-approximation.qmd").read_text(encoding="utf-8")
count=0
def eq(actual,expected,tol=1e-10):
 global count
 assert np.allclose(actual,expected,rtol=tol,atol=tol),(actual,expected)
 count+=1
x=np.array([18,26,22,34]);expected=np.repeat(25.,4)
eq(x.sum(),100)
eq((x-expected)**2/expected,[1.96,.04,.36,3.24])
eq(np.sum((x-expected)**2/expected),5.6)
eq(stats.chi2.sf(5.6,3),.13277835802223117)
eq(stats.chi2.ppf(.95,3),7.814727903251179)
eq(np.sum((np.array([20,20,30,30])-25)**2/25),4)
eq((0-8)**2/8,8)
q=np.repeat(.5,4);P=np.eye(4)-np.outer(q,q)
eq(P@P,P);eq(np.trace(P),3)
eq(((np.array([23,50,20])-np.array([23.25,46.5,23.25]))**2/np.array([23.25,46.5,23.25])).sum(),.7204301075268817)
eq(stats.chi2.sf(.7204301075268817,2),math.exp(-.7204301075268817/2))
eq(round(stats.chi2.sf(.7204301075268817,2),2),.70)
eq(stats.chi2.ppf(.95,2),5.991464547107979)
eq(np.sum((np.array([14,6,13,12,11,12,5,11,7,9])-10)**2/10),8.6)
eq(stats.chi2.ppf(.95,9),16.918977604620448)
for token in ['5.60', '0.132778', '7.814728']:
 assert token in article,token
 count+=1
assert "## Check yourself {#check-yourself}" in article
print(f"pearson-chi-squared-approximation: {count} mathematical and printed-value checks passed")
