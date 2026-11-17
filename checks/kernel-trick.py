"""Independent numerical and algebraic checks for kernel-trick."""
import math
from pathlib import Path
import numpy as np


import sympy as sp
x,z=sp.symbols('x z');assert sp.expand((1+x*z)**2-(1+2*x*z+x*x*z*z))==0
X=np.array([[-1,-1],[-1,1],[1,-1],[1,1.]])
y=np.array([-1,1,1,-1]);K=(1+X@X.T)**2
assert np.array_equal(K,8*np.eye(4)+np.ones((4,4)))
assert np.allclose(np.linalg.eigvalsh(K),[8,8,8,12])
a=np.ones(4)/8;assert np.allclose(y*(K@(a*y)),1)
assert abs(.5*np.dot(a*y,K@(a*y))-.25)<1e-14
assert abs(np.dot(a,y))<1e-14
assert abs((1+np.dot([1,2],[3,1]))**2-36)<1e-14
for z0 in [[.5,-.5],[2,2]]: assert abs(np.dot(a*y,(1+X@z0)**2)+z0[0]*z0[1])<1e-14
assert .9**2==.81 and 1.5**2==2.25

G=np.exp(-.5*(np.arange(3)[:,None]-np.arange(3)[None,:])**2)
assert all(np.linalg.det(G[:j,:j])>0 for j in range(1,4))

root=Path(__file__).resolve().parents[1]
body=(root / "articles" / "kernel-trick.qmd").read_text()
source=(root / "research/content" / "kernel-trick.md").read_text()
assert "**Your turn.**" in body
assert len(__import__("re").findall(r"\{\{cite:",source)) >= 5
for token in ['0.25', '-4', '8,8,8,12']:
    assert token in body, (token, "kernel-trick")
print("kernel-trick: numerical and algebraic checks passed")
