"""Recompute the numerical examples, exercises and answers for paired-samples."""
from pathlib import Path
import math
import itertools
import numpy as np
from scipy import stats
ROOT = Path(__file__).resolve().parents[1]
article = (ROOT / "articles" / "paired-samples.qmd").read_text(encoding="utf-8")
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

d=np.array([4.,1.,3.,2.,5.]);m=d.mean();s=d.std(ddof=1);se=s/math.sqrt(len(d));t=m/se;c=stats.t.ppf(.975,4)
printed(m);printed(s*s);printed(se,6);printed(t,6);printed(2*stats.t.sf(t,4),6)
for v in [m-c*se,m+c*se]:printed(v,6)
near((-d).mean(),-m);near((-d).std(ddof=1),s)
near(4+9-2*3,7)
# Two-laboratory matched measurements also printed in the article.
x=np.array([22,18,28,26,13,8,21,26,27,29,25,24,22,28,15]);y=np.array([25,21,31,27,11,10,25,26,29,28,26,23,22,25,17]);z=x-y
printed(z.mean(),2);printed(z.std(ddof=1),2);printed(stats.ttest_rel(x,y).statistic,4);printed(stats.ttest_rel(x,y).pvalue,4)

# Recompute all ten matched student changes from the displayed measurements.
a=np.array([71.6,69.7,50.,56.9,60.9,77.5,53.9,49.6,32.3,61.3])
b=np.array([83.4,77.7,57.9,67.,69.2,87.4,63.7,59.,39.7,71.1])
change=b-a
printed(change.mean(),2);printed(change.std(ddof=1),2)
printed(stats.ttest_1samp(change,0).statistic,1)
near(stats.ttest_1samp(change,0,alternative="greater").pvalue/1e-9,2.0152450652825263)
near(abs(stats.ttest_ind(a,b,equal_var=True).statistic),1.5367709559737794)
# Recompute the paired laboratory example, including the comparison that discards pairing.
lab1=np.array([22,18,28,26,13,8,21,26,27,29,25,24,22,28,15],dtype=float)
lab2=np.array([25,21,31,27,11,10,25,26,29,28,26,23,22,25,17],dtype=float)
d=lab1-lab2;paired=stats.ttest_rel(lab1,lab2);unpaired=stats.ttest_ind(lab1,lab2,equal_var=False)
printed(d.mean(),2);printed(d.std(ddof=1),2);printed(paired.statistic,4);printed(paired.pvalue,4)
printed(paired.statistic,2);printed(paired.pvalue,2);printed(unpaired.statistic,2);printed(unpaired.pvalue,2)
unpaired_students=stats.ttest_ind(b,a,equal_var=False)
printed(unpaired_students.statistic,2)

print("paired-samples:", checks, "numerical and rendered-value checks passed")
