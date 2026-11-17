"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SLUG='nuisance-parameters'
ARTICLE=(ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
WORKED=ARTICLE.split("{#worked-example}",1)[1].split("\n## ",1)[0]
EXAMPLE,TURN=WORKED.split("**Your turn.**",1)
ANSWER=TURN.split('title="Answer"}',1)[1].split("\n:::",1)[0]

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

x=np.array([2,4,6]);mean=x.mean();R=((x-mean)**2).sum()
close(mean,4);close(R,8);close(R/3,8/3);close(((x-5)**2).sum()/3,11/3)
close((8/11)**1.5,.6202202658)
h=stats.t.ppf(.975,2)*2/math.sqrt(3);close(h,4.9682754235)
close([mean-h,mean+h],[-.9682754235,8.9682754235])
q=stats.t.ppf(.975,15);close(q,2.1314495456);close([10-q,10+q],[7.8685504544,12.1314495456])
I=np.array([[4,2],[2,4]],float);close(np.linalg.inv(I)[0,0],1/3);close(1/I[0,0],.25)
# Positive definite Schur complement identity in the multi-nuisance case.
I=np.array([[5,1,2],[1,4,0],[2,0,3]],float)
close(np.linalg.inv(I)[0,0],1/(I[0,0]-I[0,1:]@np.linalg.inv(I[1:,1:])@I[1:,0]))
# Compare computed values with the worked example and hidden answer.
assert rf"\approx{(8/11)**1.5:.6f}" in EXAMPLE
assert f"{mean-h:.6f},{mean+h:.6f}" in EXAMPLE
assert rf"10\pm{q:.6f}=({10-q:.6f},{10+q:.6f})" in ANSWER
print("nuisance-parameters: numerical checks passed")
