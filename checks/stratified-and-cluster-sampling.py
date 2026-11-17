"""Recompute the mathematical claims and printed values for stratified-and-cluster-sampling."""
from pathlib import Path
import math
import numpy as np
from scipy import stats,integrate,special
ROOT=Path(__file__).resolve().parents[1]
article=(ROOT/"articles"/"stratified-and-cluster-sampling.qmd").read_text(encoding="utf-8")
count=0
def eq(actual,expected,tol=1e-10):
 global count
 assert np.allclose(actual,expected,rtol=tol,atol=tol),(actual,expected)
 count+=1
import itertools
W=np.array([.4,.6]);means=np.array([12.,18.]);eq(W@means,15.6);eq(means.mean(),15)
eq([10*.4,10*.6],[4,6]);eq(5/40,.125);eq(5/60,1/12)
clustermeans=np.array([0.,0.,10.,10.]);cm=np.array([clustermeans[list(s)].mean() for s in itertools.combinations(range(4),2)])
eq(cm,[0,5,5,5,5,10]);eq(cm.var(),25/3)
pop=np.repeat(clustermeans,4);v=(1-8/16)*pop.var(ddof=1)/8;eq(v,5/3);eq(cm.var()/v,5)
eq(5*50+5*100,750);eq(100*250/750,100/3);eq(33+67,100);eq(5+5*2,15);eq(2*50,100);eq(4*25,100)
for token in ['15.6', '8.333333', '1.666667']:
 assert token in article,token
 count+=1
assert "## Check yourself {#check-yourself}" in article
print(f"stratified-and-cluster-sampling: {count} mathematical and printed-value checks passed")
