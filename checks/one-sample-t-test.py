"""Recompute the numerical examples, exercises and answers for one-sample-t-test."""
from pathlib import Path
import math
import itertools
import numpy as np
from scipy import stats
ROOT = Path(__file__).resolve().parents[1]
article = (ROOT / "articles" / "one-sample-t-test.qmd").read_text(encoding="utf-8")
checks = 0
def near(a, b, tol=1e-9):
    global checks
    assert math.isclose(float(a), float(b), rel_tol=tol, abs_tol=tol), (a,b)
    checks += 1
def printed(value, decimals=3):
    global checks
    token = f"{value:.{decimals}f}"
    assert token in article, ("Printed value missing",token)
    checks += 1

se=1.2/math.sqrt(16);t=(12.6-12)/se;c=stats.t.ppf(.95,15)
for v in [se,t,.6]:printed(v)
for v in [stats.t.sf(t,15),2*stats.t.sf(t,15),c,12.6-c*se,stats.t.sf(1,15)]:printed(v,6)
printed((12.6-12.3)/se)
# Caffeine example and sample-size power illustration.
z=(19.57-19)/(1.4/math.sqrt(40));printed(z,3);printed(stats.t.ppf(.99,39),2)
near(stats.t.sf(z,39),.006966167702731513,tol=1e-11)
for n in [5,50]:printed(stats.nct.sf(stats.t.ppf(.95,n-1),n-1,math.sqrt(n)/2),3)
# Recompute the paired laboratory example, including the comparison that discards pairing.
lab1=np.array([22,18,28,26,13,8,21,26,27,29,25,24,22,28,15],dtype=float)
lab2=np.array([25,21,31,27,11,10,25,26,29,28,26,23,22,25,17],dtype=float)
d=lab1-lab2;paired=stats.ttest_rel(lab1,lab2);unpaired=stats.ttest_ind(lab1,lab2,equal_var=False)
printed(d.mean(),2);printed(d.std(ddof=1),2);printed(paired.statistic,4);printed(paired.pvalue,4)
printed(paired.statistic,2);printed(paired.pvalue,2);printed(unpaired.statistic,2);printed(unpaired.pvalue,2)
# The tyre comparison has five matched cars.
tyre_a=np.array([10.6,9.8,12.3,9.7,8.8]);tyre_b=np.array([10.2,9.4,11.8,9.1,8.3]);d=tyre_a-tyre_b
assert np.allclose(d,[.4,.4,.5,.6,.5]);checks+=1
printed(d.mean(),2);printed(d.std(ddof=1),4);printed(d.std(ddof=1)/math.sqrt(5),4)
printed(stats.ttest_rel(tyre_a,tyre_b).statistic,1);printed(stats.ttest_rel(tyre_a,tyre_b).pvalue,4)
# Caffeine bounds and two-sided interval.
se=1.4/math.sqrt(40);printed(19.57-2.43*se,2)
for endpoint in 19.57+np.array([-1,1])*stats.t.ppf(.995,39)*se:printed(endpoint,2)

print("one-sample-t-test:", checks, "numerical and rendered-value checks passed")
