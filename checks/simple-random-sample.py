"""Recompute the mathematical claims and printed values for simple-random-sample."""
from pathlib import Path
import math
import numpy as np
from scipy import stats,integrate,special
ROOT=Path(__file__).resolve().parents[1]
article=(ROOT/"articles"/"simple-random-sample.qmd").read_text(encoding="utf-8")
count=0
def eq(actual,expected,tol=1e-10):
 global count
 assert np.allclose(actual,expected,rtol=tol,atol=tol),(actual,expected)
 count+=1
import itertools
pop=np.array([1.,3.,5.,7.]);samples=list(itertools.combinations(range(4),2));means=np.array([pop[list(s)].mean() for s in samples])
eq(len(samples),6);eq(means,[2,3,4,4,5,6]);eq(means.mean(),4);eq(means.var(),5/3)
eq(pop.var(ddof=1),20/3);eq((1-2/4)*pop.var(ddof=1)/2,5/3)
for i in range(4):eq(sum(i in s for s in samples)/6,.5)
eq(2*(2-1)/(4*(4-1)),1/6);eq(math.comb(5,3),10);eq(math.comb(20,10),184756)
eq(5*50+5*100,750);eq(100*250/750,100/3);eq(33+67,100);eq(5+5*2,15);eq(2*50,100);eq(4*25,100)
for token in ['$5/3$']:
 assert token in article,token
 count+=1
assert "## Check yourself {#check-yourself}" in article
print(f"simple-random-sample: {count} mathematical and printed-value checks passed")
