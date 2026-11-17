"""Recompute the mathematical claims and printed values for one-hidden-layer-approximates-continuous-functions."""
from pathlib import Path
import math
import numpy as np
from scipy import stats,integrate,special
ROOT=Path(__file__).resolve().parents[1]
article=(ROOT/"articles"/"one-hidden-layer-approximates-continuous-functions.qmd").read_text(encoding="utf-8")
count=0
def eq(actual,expected,tol=1e-10):
 global count
 assert np.allclose(actual,expected,rtol=tol,atol=tol),(actual,expected)
 count+=1
sig=lambda z: special.expit(z)
f=lambda x,k: sig(k*(x-.25))-sig(k*(x-.75))
eq(f(.5,10),.8482836399575129)
eq(f(0,10),.07530540134167948)
eq(f(1,10),f(0,10))
eq(f(.5,20),.9866142981514305)
eq(6*sig(0),3)
x=np.linspace(0,1,101)
eq(f(x,10),f(1-x,10))
eq(np.max(sig(np.linspace(-10,10,101))*(1-sig(np.linspace(-10,10,101)))),.25)
eq(10*(.5-.25),2.5)
eq(10*(.5-.75),-2.5)
eq(10*.25+10*.25,5)
for token in ['0.848284', '0.075305', '0.986614']:
 assert token in article,token
 count+=1
assert "## Check yourself {#check-yourself}" in article
print(f"one-hidden-layer-approximates-continuous-functions: {count} mathematical and printed-value checks passed")
