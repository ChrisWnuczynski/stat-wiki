"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

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
print("limits-of-sequences-of-events: numerical checks passed")
