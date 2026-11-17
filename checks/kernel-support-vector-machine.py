"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

x=np.array([[-1,-1],[-1,1],[1,-1],[1,1]],float); y=np.array([-1,1,1,-1])
k=(1+x@x.T)**2
close(k,8*np.eye(4)+np.ones((4,4)));close(np.linalg.eigvalsh(k),[8,8,8,12])
close(y@k@y,32)
a=np.full(4,1/8);close(y@a,0)
close(a.sum()-.5*(a*y)@k@(a*y),.25)
phi=lambda z:np.array([1,math.sqrt(2)*z[0],math.sqrt(2)*z[0]*z[1],math.sqrt(2)*z[1],z[0]**2,z[1]**2])
P=np.array([phi(z) for z in x]); close(P@P.T,k)
w=(a*y)@P; close(w,[0,0,-math.sqrt(2)/2,0,0,0])
close(np.linalg.norm(w),1/math.sqrt(2));close(y*(P@w),np.ones(4))
close([w@phi([.5,-.5]),w@phi([2,2])],[.25,-4])
close(1/np.linalg.norm(w),math.sqrt(2));close(2/np.linalg.norm(w),2*math.sqrt(2))
C=1/16; w2=(np.full(4,C)*y)@P
close(y*(P@w2),np.full(4,.5));close(w2@phi([.5,-.5]),.125)
print("kernel-support-vector-machine: numerical checks passed")
