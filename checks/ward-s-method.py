"""Recompute the numerical claims and inspect the generated article."""
from pathlib import Path
import math
from fractions import Fraction
from itertools import combinations
import numpy as np
from scipy import stats
import sympy as sp
ROOT = Path(__file__).resolve().parents[1]
def W(xs):
 xs=np.array(xs,dtype=float);return float(np.sum((xs-xs.mean(axis=0))**2))
A=[0,2];B=[3]
assert np.isclose(W(A),2) and np.isclose(W(A+B),14/3)
assert np.isclose(W(A+B)-W(A)-W(B),8/3)
assert np.isclose(2*1/3*(1-5)**2,32/3)
assert np.isclose((3-5)**2/2,2)
assert (3*6)/(3+6)*(2-5)**2==18
assert 10/2==5
assert np.isclose((3-10)**2/2,24.5)
assert np.isclose(2/3*(1-10)**2,54)

from sklearn.datasets import load_iris
from sklearn.metrics import adjusted_rand_score
from scipy.cluster.hierarchy import linkage, fcluster
x,y=load_iris(return_X_y=True)
z=(x-x.mean(axis=0))/x.std(axis=0,ddof=1)
aris={m:adjusted_rand_score(y,fcluster(linkage(z,method=m),3,criterion="maxclust")) for m in ["single","complete","average","ward"]}
assert [round(aris[m],3) for m in ["single","complete","average","ward"]]==[.558,.573,.562,.615]
assert aris["ward"]>max(v for k,v in aris.items() if k!="ward")

text = (ROOT / "articles" / "ward-s-method.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in text
assert "Your turn" in text
assert text.count('class="cite-ref"') >= 5
print("ward-s-method: all recomputed claims and generated-text checks passed")
