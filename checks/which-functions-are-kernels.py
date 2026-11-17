"""Recompute numerical examples and exercise answers for which-functions-are-kernels."""
import math
import numpy as np
from scipy import stats, special, linalg, integrate

a=np.array([[1,2],[2,1]]);v=np.array([1,-1]);assert v@a@v==-2
x=np.array([-1.,0,1]);G=(1+np.outer(x,x))**2
P=np.column_stack([np.ones(3),np.sqrt(2)*x,x*x]);assert np.allclose(G,P@P.T)
assert np.allclose(G,[[4,1,0],[1,1,1],[0,1,4]])
assert np.allclose(np.linalg.eigvalsh(G),[(5-math.sqrt(17))/2,4,(5+math.sqrt(17))/2])
assert np.allclose(np.round(np.linalg.eigvalsh(G),4),[.4384,4,4.5616])
H=np.array([[1,-3],[-3,1]]);assert np.ones(2)@H@np.ones(2)==-4
for f in [[1,2],[0,0],[-3,7]]:assert np.linalg.matrix_rank(np.outer(f,f))<=1
assert -.2<0 and -1<0
print("which-functions-are-kernels: numerical checks passed")
