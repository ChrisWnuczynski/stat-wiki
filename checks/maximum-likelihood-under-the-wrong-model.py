"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SLUG='maximum-likelihood-under-the-wrong-model'
ARTICLE=(ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
WORKED=ARTICLE.split("{#worked-example}",1)[1].split("\n## ",1)[0]
EXAMPLE,TURN=WORKED.split("**Your turn.**",1)
ANSWER=TURN.split('title="Answer"}',1)[1].split("\n:::",1)[0]

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

for m,v,n,sd in [(4,12,100,.3464101615),(4,2,100,.1414213562)]:
 A=1/m;B=v/m**2
 close(B/A**2/n,v/n);close(math.sqrt(v/n),sd)
close(math.sqrt(4/100),.2);close(math.sqrt(12/4),math.sqrt(3))
close(math.sqrt(9/400),.15);close(math.sqrt(36/400),.3)
# Population expected Poisson log-likelihood is maximized at its true mean.
from scipy.optimize import minimize_scalar
for mean in [2,4,9]:
 f=lambda l:-(mean*math.log(l)-l)
 opt=minimize_scalar(f,bounds=(.01,20),method='bounded')
 close(opt.x,mean,tol=2e-5)
# Compare computed values with the worked example and hidden answer.
assert rf"\approx{math.sqrt(12/100):.6f}" in EXAMPLE
assert rf"\approx{math.sqrt(2/100):.6f}" in EXAMPLE
assert rf"\sqrt{{9/400}}={math.sqrt(9/400):.2f}" in ANSWER
assert rf"\sqrt{{36/400}}={math.sqrt(36/400):.1f}" in ANSWER
print("maximum-likelihood-under-the-wrong-model: numerical checks passed")
