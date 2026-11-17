"""Recompute the mathematical claims and printed values for scaling."""
from pathlib import Path
import math
import numpy as np
from scipy import stats,integrate,special
ROOT=Path(__file__).resolve().parents[1]
article=(ROOT/"articles"/"scaling.qmd").read_text(encoding="utf-8")
count=0
def eq(actual,expected,tol=1e-10):
 global count
 assert np.allclose(actual,expected,rtol=tol,atol=tol),(actual,expected)
 count+=1
S=np.diag([4.,1.]);D=np.diag([2.,1.]);R=np.linalg.inv(D)@S@np.linalg.inv(D)
eq(R,np.eye(2));eq(4/5,.8);eq(np.linalg.eigvalsh(R),[1,1]);eq(1/np.trace(R),.5)
m=np.array([4.,10.]);sc=np.array([2.,5.]);eq((np.array([6.,5.])-m)/sc,[1,-1]);eq((np.array([8.,15.])-m)/sc,[2,1])
eq(.01*100**2,100);eq(1000**2,10**6);eq(10**2,100)
eq((6-4)/2,1);eq(np.linalg.eigvalsh([[1,.8],[.8,1]]),[.2,1.8])
for token in ['80', '50']:
 assert token in article,token
 count+=1
assert "## Check yourself {#check-yourself}" in article
print(f"scaling: {count} mathematical and printed-value checks passed")
