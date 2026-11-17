"""Independent numerical and algebraic checks for iteratively-reweighted-least-squares."""
import math
from pathlib import Path
import numpy as np


from scipy.special import expit
X=np.c_[np.ones(4),np.arange(4)];y=np.array([0,1,0,1]);b=np.zeros(2);ls=[]
for i in range(8):
 p=expit(X@b);w=p*(1-p);z=X@b+(y-p)/w
 bn=np.linalg.solve(X.T@(w[:,None]*X),X.T@(w*z))
 newton=b+np.linalg.solve(X.T@(w[:,None]*X),X.T@(y-p))
 assert np.allclose(bn,newton)
 if i==0:assert np.allclose(bn,[-1.2,.8])
 ls.append(float(np.sum(y*(X@bn)-np.logaddexp(0,X@bn))));b=bn
assert np.all(np.diff(ls)>-1e-12)
assert np.allclose(b,[-1.36227639,.90818426],atol=5e-9)
assert abs(ls[0]+2.3525954394759676)<1e-13
assert abs(ls[-1]+2.3474865351213454)<1e-13
assert np.allclose(np.sqrt(np.diag(np.linalg.inv(X.T@((expit(X@b)*(1-expit(X@b)))[:,None]*X)))),[1.97488295,1.08519211],atol=1e-8)

assert abs(4*math.log(.5)+2.772588722239781)<1e-13

root=Path(__file__).resolve().parents[1]
body=(root / "articles" / "iteratively-reweighted-least-squares.qmd").read_text()
source=(root / "research/content" / "iteratively-reweighted-least-squares.md").read_text()
assert "**Your turn.**" in body
assert len(__import__("re").findall(r"\{\{cite:",source)) >= 5
for token in ['-1.362276', '0.908184', '1.974883', '1.085192']:
    assert token in body, (token, "iteratively-reweighted-least-squares")
print("iteratively-reweighted-least-squares: numerical and algebraic checks passed")
