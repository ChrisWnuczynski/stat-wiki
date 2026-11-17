"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

x=np.array([[0,0],[2,0],[0,2],[2,2]],float);m=x.mean(0);A=(x-m).T@(x-m)
close(m,[1,1]);close(A,np.diag([4,4]));close(A/4,np.eye(2));close(A/3,np.eye(2)*4/3)
x2=np.array([[0,0],[1,1],[2,2]],float);A2=(x2-x2.mean(0)).T@(x2-x2.mean(0))
close(A2,[[2,2],[2,2]]);close(np.linalg.eigvalsh(A2),[0,4])
x3=np.array([[0,0],[4,0],[0,2],[4,2]],float);A3=(x3-x3.mean(0)).T@(x3-x3.mean(0))
close(x3.mean(0),[2,1]);close(A3,np.diag([16,4]));close(np.linalg.inv(A3/4),np.diag([.25,1]))
for val in [.01,.3,1,2,100]:assert math.log(val)-val+1<=1e-14
# Nonzero curvature in symmetric directions makes the precision objective strictly concave.
for H in [np.eye(2),np.array([[0,1],[1,0]])]:assert np.trace(H@H)>0
# Null-direction construction increases log determinant without changing trace scatter.
v=np.array([1,-1])/math.sqrt(2)
for t in [1,10,100]:
 T=np.eye(2)+t*np.outer(v,v);close(np.trace(A2@T),np.trace(A2));close(np.linalg.det(T),1+t)
print("maximum-likelihood-for-a-covariance-matrix: numerical checks passed")
