"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SLUG='kernel-support-vector-machine'
ARTICLE=(ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
WORKED=ARTICLE.split("{#worked-example}",1)[1].split("\n## ",1)[0]
EXAMPLE,TURN=WORKED.split("**Your turn.**",1)
ANSWER=TURN.split('title="Answer"}',1)[1].split("\n:::",1)[0]

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
# Compare computed values with the worked example and hidden answer.
eigenvalues=','.join(str(int(v)) for v in np.rint(np.linalg.eigvalsh(k)[::-1]))
assert f"eigenvalues ${eigenvalues}$" in EXAMPLE
assert rf"\alpha_i={F(float(a[0])).limit_denominator()}" in EXAMPLE
turn_margin=F(float((y*(P@w2))[0])).limit_denominator()
turn_prediction=F(float(w2@phi([.5,-.5]))).limit_denominator()
assert f"margin is ${turn_margin}$" in ANSWER
assert f"f(0.5,-0.5)={turn_prediction}>0" in ANSWER
print("kernel-support-vector-machine: numerical checks passed")
