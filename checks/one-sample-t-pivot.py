"""Recompute the numerical examples, exercises and answers for one-sample-t-pivot."""
from pathlib import Path
import math
import itertools
import numpy as np
from scipy import stats
ROOT = Path(__file__).resolve().parents[1]
article = (ROOT / "articles" / "one-sample-t-pivot.qmd").read_text(encoding="utf-8")
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

n=9;mean=2.4;sd=1.8;se=sd/math.sqrt(n);t=mean/se;c=stats.t.ppf(.975,n-1)
near(t,4);printed(t);printed(2*stats.t.sf(t,8),6);printed(c,6)
for v in [c*se,mean-c*se,mean+c*se]:printed(v,6)
printed(1.8/math.sqrt(36));printed(2.4/(1.8/math.sqrt(36)))
# Recompute the carried calibration examples as well.
near(178/math.sqrt(51),24.92498549569857);printed(1136-stats.t.ppf(.975,50)*178/math.sqrt(51),1);printed(1136+stats.t.ppf(.975,50)*178/math.sqrt(51),1)
x=np.array([77.01,71.37,77.15,79.89,76.46,78.10,77.18,74.08,75.88,72.63]);near(x.mean(),75.975);printed(x.mean(),3)
printed(x.mean()-stats.t.ppf(.975,9)*x.std(ddof=1)/math.sqrt(10),2);printed(x.mean()+stats.t.ppf(.975,9)*x.std(ddof=1)/math.sqrt(10),2)
near(np.std([2.52,2.48],ddof=1)/math.sqrt(2),.02)
# Corrected sample scatter, small-sample quantiles and the batch-volume rescaling.
printed(x.std(ddof=1),3);printed(x.std(ddof=1),2)
near(1-1.96/stats.t.ppf(.975,9),.1335703481291961,tol=1e-3)
batches=np.array([25.36-22.84,22.84-20.36]);near(batches.mean(),2.5);near(batches.std(ddof=1),.02*math.sqrt(2))
for endpoint in batches.mean()+np.array([-1.,1.])*12.71*.02:printed(endpoint,2);printed(endpoint/50,3)
print("one-sample-t-pivot:", checks, "numerical and rendered-value checks passed")
