"""Recompute the mathematical claims and printed values for regression-tree."""
from pathlib import Path
import math
import numpy as np
from scipy import stats,integrate,special
ROOT=Path(__file__).resolve().parents[1]
article=(ROOT/"articles"/"regression-tree.qmd").read_text(encoding="utf-8")
count=0
def eq(actual,expected,tol=1e-10):
 global count
 assert np.allclose(actual,expected,rtol=tol,atol=tol),(actual,expected)
 count+=1
x=np.arange(1.,5.);y=np.array([1.,2.,8.,9.]);parent=((y-y.mean())**2).sum();eq(parent,50)
rss=[]
for k in range(1,4):rss.append(((y[:k]-y[:k].mean())**2).sum()+((y[k:]-y[k:].mean())**2).sum())
eq(rss,[86/3,1,86/3]);eq(np.argmin(rss),1);eq(y[:2].mean(),1.5);eq(y[2:].mean(),8.5)
eq(parent-rss[1],49);eq(2*2/4*(8.5-1.5)**2,49);eq(np.mean([2,4,9]),5)
eq(np.where(np.array([2.2,100])<2.5,1.5,8.5),[1.5,8.5])
for token in ['28.666667']:
 assert token in article,token
 count+=1
assert "## Check yourself {#check-yourself}" in article
print(f"regression-tree: {count} mathematical and printed-value checks passed")
