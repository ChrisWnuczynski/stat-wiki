"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SLUG='multi-server-and-finite-capacity-queues'
ARTICLE=(ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
WORKED=ARTICLE.split("{#worked-example}",1)[1].split("\n## ",1)[0]
EXAMPLE,TURN=WORKED.split("**Your turn.**",1)
ANSWER=TURN.split('title="Answer"}',1)[1].split("\n:::",1)[0]

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

a=1;rho=.5;c=2;lam=mu=2
pi0=1/(1+a+a*a/math.factorial(c)/(1-rho));close(pi0,1/3)
wait=pi0*a*a/2/(1-rho);Lq=pi0*a*a/2*rho/(1-rho)**2
close(wait,1/3);close(Lq,1/3);close(Lq/lam,1/6);close(Lq/lam*60,10)
w=np.array([1,1,.5,.25]);pi=w/w.sum();close(pi,np.array([4,4,2,1])/11)
through=lam*(1-pi[-1]);close(through,20/11)
L=pi@np.arange(4);close(L,1);close(L/through,11/20)
close(pi@np.minimum(np.arange(4),2),10/11);close(mu*(pi@np.minimum(np.arange(4),2)),through)
close(np.ones(3)/3,[1/3]*3);close(lam*(1-1/3),2*lam/3)
for r in [.5,1,2]:
 K=4;weights=r**np.arange(K+1);prob=weights/weights.sum()
 if r!=1:close(prob,(1-r)*r**np.arange(K+1)/(1-r**(K+1)))
 close(prob[-1]*(K-prob@np.arange(K+1))/r,(K*r**(K-1)*weights.sum()-r**K*sum(j*r**(j-1) for j in range(1,K+1)))/weights.sum()**2)
# Compare computed values with the worked example and hidden answer.
assert rf"\pi_0={F(pi0).limit_denominator()}" in EXAMPLE
assert f"mean waiting is ${F(Lq/lam).limit_denominator()}$ hour" in EXAMPLE
assert f"throughput is ${F(through).limit_denominator()}$ per hour" in EXAMPLE
assert f"={F(float(L/through)).limit_denominator()}$ hour" in EXAMPLE
turn_block=F(float((np.ones(3)/3)[-1])).limit_denominator()
turn_accept=1-turn_block
assert rf"\pi_2={turn_block}" in ANSWER
assert rf"={turn_accept.numerator}\lambda/{turn_accept.denominator}" in ANSWER
print("multi-server-and-finite-capacity-queues: numerical checks passed")
