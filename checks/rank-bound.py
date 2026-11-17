"""Recompute the mathematical claims and printed values for rank-bound."""
from pathlib import Path
import math
import numpy as np
from scipy import stats,integrate,special
ROOT=Path(__file__).resolve().parents[1]
article=(ROOT/"articles"/"rank-bound.qmd").read_text(encoding="utf-8")
count=0
def eq(actual,expected,tol=1e-10):
 global count
 assert np.allclose(actual,expected,rtol=tol,atol=tol),(actual,expected)
 count+=1
X=np.array([[1.,0.,1.,2.,0.],[0.,1.,1.,0.,2.],[1.,1.,2.,2.,2.]])
H=np.eye(3)-np.ones((3,3))/3;C=H@X;S=C.T@C/2
rank=np.linalg.matrix_rank(C);eq(rank,2);eq(np.linalg.matrix_rank(S),2)
eq(np.linalg.eigvalsh(S),[0,0,0,7/6,5/2]);eq(np.trace(S),11/3)
eq(np.linalg.eigvalsh(S+.1*np.eye(5)),[.1,.1,.1,19/15,13/5])
eq(H@H,H);eq(H@np.ones(3),np.zeros(3));eq(20-min(12-1,20),9)
eq(100-2,98);eq(40-4,36);eq(5-rank,3)
for token in ['$7/6$', '$5/2$']:
 assert token in article,token
 count+=1
assert "## Check yourself {#check-yourself}" in article
print(f"rank-bound: {count} mathematical and printed-value checks passed")
