"""Recompute the mathematical claims and printed values for softmax-is-multinomial-logistic-regression."""
from pathlib import Path
import math
import numpy as np
from scipy import stats,integrate,special
ROOT=Path(__file__).resolve().parents[1]
article=(ROOT/"articles"/"softmax-is-multinomial-logistic-regression.qmd").read_text(encoding="utf-8")
count=0
def eq(actual,expected,tol=1e-10):
 global count
 assert np.allclose(actual,expected,rtol=tol,atol=tol),(actual,expected)
 count+=1
z=np.log(np.array([1.,2.,3.]));p=special.softmax(z);eq(p,[1/6,1/3,1/2])
eq(-np.log(p[2]),np.log(2));eq(p-np.array([0,0,1]),[1/6,1/3,-1/2]);eq((p-np.array([0,0,1])).sum(),0)
eq(special.softmax(z+1000),p);eq(special.softmax(z-z.max()),p);eq(p[2]/p[0],3)
# Recompute the three-score calculations in the accompanying explanation.
z0=np.array([1.,0.,-1.]);q=special.softmax(z0)
eq(np.exp(z0),[np.e,1,1/np.e]);eq(np.exp(z0).sum(),4.086161269630487)
eq(q,[.6652409557748218,.24472847105479764,.09003057317038046]);eq(-np.log(q[0]),.40760596444438046)
eq(special.softmax([6,5,4]),q);eq(special.expit(2),np.exp(3)/(np.exp(3)+np.exp(1)))
for token in ['0.693147']:
 assert token in article,token
 count+=1
assert "## Check yourself {#check-yourself}" in article
print(f"softmax-is-multinomial-logistic-regression: {count} mathematical and printed-value checks passed")
