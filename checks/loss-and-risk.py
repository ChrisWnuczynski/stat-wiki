"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SLUG='loss-and-risk'
ARTICLE=(ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
WORKED=ARTICLE.split("{#worked-example}",1)[1].split("\n## ",1)[0]
EXAMPLE,TURN=WORKED.split("**Your turn.**",1)
ANSWER=TURN.split('title="Answer"}',1)[1].split("\n:::",1)[0]

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

p=np.array([.2,.5,.3]);v=np.array([0,1,4]);mean=p@v
close(mean,1.7)
close(p@(v-mean)**2,2.41);close(p@(v-1)**2,2.9)
close(p@abs(v-1),1.1);close(p@abs(v-mean),1.38)
risk=lambda a,t:a*a+(a-1)**2*t*t
close([risk(1,0),risk(.5,0),risk(1,2),risk(.5,2)],[1,.25,1,1.25])
close(risk(.5,math.sqrt(3)),1);close(.2+.4**2,.36)
assert .36<.5 and 2**2==4
# Empirical absolute, square and maximum losses have distinct minimizers.
y=np.array([0,1,9]);grid=np.linspace(0,9,9001)
close(grid[np.argmin(((grid[:,None]-y)**2).sum(1))],10/3,tol=.001)
close(grid[np.argmin(abs(grid[:,None]-y).sum(1))],1)
close(grid[np.argmin(abs(grid[:,None]-y).max(1))],4.5)
# Compare computed values with the worked example and hidden answer.
assert f"posterior mean is ${mean:.1f}$" in EXAMPLE
assert f"Expected squared loss at ${mean:.1f}$ is ${p@(v-mean)**2:.2f}$" in EXAMPLE
assert f"Expected absolute loss at $1$ is ${p@abs(v-1):.1f}$" in EXAMPLE
assert f"At zero, the risks are ${F(risk(1,0))}$ and ${F(risk(F(1,2),0))}$" in ANSWER
assert f"At two, they are ${F(risk(1,2))}$ and ${F(risk(F(1,2),2))}$" in ANSWER
print("loss-and-risk: numerical checks passed")
