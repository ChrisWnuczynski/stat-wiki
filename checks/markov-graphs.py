"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SLUG='markov-graphs'
ARTICLE=(ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
WORKED=ARTICLE.split("{#worked-example}",1)[1].split("\n## ",1)[0]
EXAMPLE,TURN=WORKED.split("**Your turn.**",1)
ANSWER=TURN.split('title="Answer"}',1)[1].split("\n:::",1)[0]

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

import itertools
states=list(itertools.product([0,1],repeat=3))
w=np.array([2**(a==b)*2**(b==c) for a,b,c in states]);assert w.sum()==18
p=w/w.sum();mask=np.array([b==0 for a,b,c in states]);p0=p[mask]/p[mask].sum();s0=[s for s in states if s[1]==0]
P=lambda pred:sum(q for q,s in zip(p0,s0) if pred(s))
close(P(lambda s:s[0]==0),2/3);close(P(lambda s:s[2]==0),2/3)
close(P(lambda s:s[0]==0 and s[2]==0),4/9)
close(P(lambda s:s[0]==1 and s[2]==0),2/9)
close(sum(q for q,s in zip(p,states) if s[0]==s[2]),5/9)
edges={frozenset(e) for e in [(1,2),(1,3),(2,3),(2,4),(3,4),(4,5),(4,6),(5,6)]}
V=set(range(1,7))
complete=lambda c:all(frozenset(e) in edges for e in itertools.combinations(c,2))
cliques=[set(c) for k in range(1,7) for c in itertools.combinations(V,k) if complete(c)]
maximal=[c for c in cliques if not any(c<d for d in cliques)]
assert {frozenset(c) for c in maximal}=={frozenset([1,2,3]),frozenset([2,3,4]),frozenset([4,5,6])}
assert all(frozenset(e) in edges for e in [(1,3),(3,4),(4,5)])
# Compare computed values with the worked example and hidden answer.
assert f"Z=2(3)(3)={w.sum()}" in EXAMPLE
joint=F(float(P(lambda s:s[0]==0 and s[2]==0))).limit_denominator()
assert rf"\mathbb{{P}}(X_1=0,X_3=0\mid X_2=0)={joint}" in EXAMPLE
marginal=F(float(sum(q for q,s in zip(p,states) if s[0]==s[2]))).limit_denominator()
assert rf"\mathbb{{P}}(X_1=X_3)={marginal}" in EXAMPLE
turn_joint=F(float(P(lambda s:s[0]==1 and s[2]==0))).limit_denominator()
assert f"Conditional independence gives ${turn_joint}$" in ANSWER
print("markov-graphs: numerical checks passed")
