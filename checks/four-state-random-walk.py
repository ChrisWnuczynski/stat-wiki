"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

Q=np.array([[.5,.25,0,0],[.5,.5,.25,0],[0,.25,.5,.5],[0,0,.25,.5]])
pi=np.array([1,2,2,1])/6
assert np.allclose(Q.sum(0),1) and np.allclose(Q@pi,pi)
assert np.allclose(Q*pi[None,:],(Q*pi[None,:]).T)
assert np.allclose(np.sort(np.linalg.eigvals(Q)),[0,.25,.75,1])
assert np.allclose(Q@Q@np.array([1,0,0,0]),[3/8,1/2,1/8,0]) and (Q@Q)[0,1]==.25
h=np.linalg.solve(np.eye(3)-Q[:3,:3].T,np.ones(3));assert np.allclose(h,[18,16,10])
assert np.allclose(np.linalg.matrix_power(Q,100)[:,0],pi,atol=1e-12)
A=Q.copy();A[:,3]=[0,0,0,1]
assert np.all(np.linalg.matrix_power(A,3)[3,:3]>=1/32)
assert 3/(1/32)==96 and max(h)<96
print("four-state-random-walk: numerical checks passed")
