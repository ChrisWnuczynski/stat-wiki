"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SLUG='limits-of-sequences-of-events'
ARTICLE=(ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
WORKED=ARTICLE.split("{#worked-example}",1)[1].split("\n## ",1)[0]
EXAMPLE,TURN=WORKED.split("**Your turn.**",1)
ANSWER=TURN.split('title="Answer"}',1)[1].split("\n:::",1)[0]

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

odd,even={"a","b"},{"b","c"}
liminf=odd&even; limsup=odd|even
assert liminf=={"b"} and limsup=={"a","b","c"}
p={"a":F(1,2),"b":F(1,3),"c":F(1,6)}
P=lambda s:sum(p[z] for z in s)
assert P(odd)==F(5,6) and P(even)==F(1,2) and P(liminf)==F(1,3) and P(limsup)==1
assert F(1,3)<=F(1,2)<=F(5,6)<=1
assert {1,2}&{2,3}=={2} and {1,2}|{2,3}=={1,2,3}
# De Morgan and indicator limits for every periodic sequence of two events.
import itertools
universe=set(range(4))
sets=[set(c) for k in range(5) for c in itertools.combinations(universe,k)]
for A in sets:
 for B in sets:
  assert universe-(A|B)==(universe-A)&(universe-B)
  assert A&B<=A|B
  for z in universe:
   assert int(z in A&B)==min(int(z in A),int(z in B))
   assert int(z in A|B)==max(int(z in A),int(z in B))
# Compare computed values with the worked example and hidden answer.
assert rf"${P(liminf)}\le{min(P(odd),P(even))}\le{max(P(odd),P(even))}\le{P(limsup)}$" in EXAMPLE
turn_inf={1,2}&{2,3}
turn_sup={1,2}|{2,3}
tex_set=lambda values:r'\{'+','.join(map(str,sorted(values)))+r'\}'
assert f"liminf is ${tex_set(turn_inf)}$" in ANSWER
assert f"limsup is ${tex_set(turn_sup)}$" in ANSWER
print("limits-of-sequences-of-events: numerical checks passed")
