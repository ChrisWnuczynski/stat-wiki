"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SLUG='machine-repair-model'
ARTICLE=(ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
WORKED=ARTICLE.split("{#worked-example}",1)[1].split("\n## ",1)[0]
EXAMPLE,TURN=WORKED.split("**Your turn.**",1)
ANSWER=TURN.split('title="Answer"}',1)[1].split("\n:::",1)[0]

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

lam,mu=1,2
Q=np.array([[-2*lam,2*lam,0],[mu,-mu-lam,lam],[0,mu,-mu]],float)
w=np.array([1,2*lam/mu,2*(lam/mu)**2]);pi=w/w.sum()
close(pi,[.4,.4,.2]);close(pi@Q,[0,0,0]);close(Q.sum(1),[0,0,0])
failed=pi@np.arange(3);operating=2-failed
close([failed,operating,operating/2],[.8,1.2,.6]);close(mu*(1-pi[0]),lam*operating)
w2=np.array([1,1,.25]);close(w2/w2.sum(),[4/9,4/9,1/9])
q2=Q.copy();q2[2]=[0,4,-4];close((w2/w2.sum())@q2,[0,0,0])
w3=np.array([1,2,2]);p3=w3/w3.sum();close(p3,[.2,.4,.4]);close(2-p3@np.arange(3),.8)
close(pi@(3*Q),[0,0,0])

A=np.array([[1,-1],[-2/3,1]],float);rhs=np.array([.5,1/3]);hit=np.linalg.solve(A,rhs)
close(hit,[2.5,2]);close((3*1+2)/(2*1**2),2.5)

# Compare computed values with the worked example and hidden answer.
probabilities=','.join(str(F(float(v)).limit_denominator()) for v in pi)
assert rf"\pi=({probabilities})" in EXAMPLE
assert f"${F(float(failed)).limit_denominator()}$ failed machines" in EXAMPLE
assert f"${F(float(operating)).limit_denominator()}$ operating machines" in EXAMPLE
turn_probabilities=','.join(str(F(float(v)).limit_denominator()) for v in p3)
assert f"probabilities are ${turn_probabilities}$" in ANSWER
assert f"operating machines is ${F(float(2-p3@np.arange(3))).limit_denominator()}$" in ANSWER
print("machine-repair-model: numerical checks passed")
