"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SLUG='maximum-likelihood-for-a-normal-mean-vector'
ARTICLE=(ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
WORKED=ARTICLE.split("{#worked-example}",1)[1].split("\n## ",1)[0]
EXAMPLE,TURN=WORKED.split("**Your turn.**",1)
ANSWER=TURN.split('title="Answer"}',1)[1].split("\n:::",1)[0]

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

x=np.array([[1,2],[3,2],[2,5]],float);m=x.mean(0);S=np.array([[4,1],[1,9]],float);T=np.linalg.inv(S)
close(m,[2,3]);a=np.array([1,-1]);close(a@m,-1);close(a@S@a/3,11/3)
close(math.sqrt(11/3),1.9148542155);close(math.sqrt(13/3),2.0816659995)
extra=3*m@T@m;close(extra,36/7);close(math.exp(-extra/2),.07642628699)
for u in [np.zeros(2),np.array([1,5]),m]:
 lhs=sum((z-u)@T@(z-u) for z in x)
 rhs=sum((z-m)@T@(z-m) for z in x)+3*(m-u)@T@(m-u)
 close(lhs,rhs)
close(np.array([[0,1],[4,5]]).mean(0),[2,3]);close(np.array([1,1])@np.eye(2)@np.array([1,1])/2,1)
close(np.diag([4,16])/8,np.diag([.5,2]));close((0+10/4)/(1+1/4),2)

close(stats.chi2.ppf(.95,2),5.9914645471);assert 36/7<stats.chi2.ppf(.95,2)

# Compare computed values with the worked example and hidden answer.
assert rf"\widehat\mu=({','.join(f'{v:g}' for v in m)})" in EXAMPLE
assert rf"\approx{math.sqrt(a@S@a/3):.6f}" in EXAMPLE
assert rf"\approx{math.exp(-extra/2):.6f}" in EXAMPLE
turn_mean=np.array([[0,1],[4,5]]).mean(0)
turn_variance=np.ones(2)@np.eye(2)@np.ones(2)/2
assert f"MLE is $({','.join(f'{v:g}' for v in turn_mean)})$" in ANSWER
assert f"variance $(1+1)/2={turn_variance:g}$" in ANSWER
print("maximum-likelihood-for-a-normal-mean-vector: numerical checks passed")
