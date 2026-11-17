"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SLUG='maximum-likelihood-for-a-covariance-matrix'
ARTICLE=(ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
WORKED=ARTICLE.split("{#worked-example}",1)[1].split("\n## ",1)[0]
EXAMPLE,TURN=WORKED.split("**Your turn.**",1)
ANSWER=TURN.split('title="Answer"}',1)[1].split("\n:::",1)[0]

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
# Compare computed values with the worked example and hidden answer.
diagonal=lambda matrix:','.join(str(F(float(v)).limit_denominator()) for v in np.diag(matrix))
assert rf"A=\operatorname{{diag}}({diagonal(A)})" in EXAMPLE
turn_mean=','.join(f'{v:g}' for v in x3.mean(0))
assert f"mean is $({turn_mean})$" in ANSWER
assert rf"scatter is $\operatorname{{diag}}({diagonal(A3)})$" in ANSWER
assert rf"covariance MLE is $\operatorname{{diag}}({diagonal(A3/4)})$" in ANSWER
assert rf"inverse is $\operatorname{{diag}}({diagonal(np.linalg.inv(A3/4))})$" in ANSWER
print("maximum-likelihood-for-a-covariance-matrix: numerical checks passed")
