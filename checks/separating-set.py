"""Recompute examples independently and inspect the generated article."""
import numpy as np
import math

from itertools import combinations
edges={(1,2),(1,3),(2,3),(2,4),(3,4),(4,5),(4,6),(5,6)}
V=set(range(1,7));adj={i:{j for j in V if tuple(sorted((i,j))) in edges} for i in V}
def reach(a,removed):
 seen={a};todo=[a]
 while todo:
  i=todo.pop()
  for j in adj[i]-removed-seen:seen.add(j);todo.append(j)
 return seen
assert not ({5,6}&reach(1,{4}))
assert 4 in reach(1,{2}) and 4 in reach(1,{3})
assert 4 not in reach(1,{2,3})
assert (adj[1]|adj[2])-{1,2}=={3,4}
assert adj[5]|{5}=={4,5,6}
cliques=[set(c) for n in range(1,7) for c in combinations(V,n) if all(tuple(sorted(e)) in edges for e in combinations(c,2))]
maximal=[c for c in cliques if not any(c<d for d in cliques)]
assert {frozenset(c) for c in maximal}=={frozenset({1,2,3}),frozenset({2,3,4}),frozenset({4,5,6})}
K=np.array([[2.,-1,0],[-1,3,-1],[0,-1,2]]);S=np.linalg.inv(K)
assert abs(np.linalg.det(K)-8)<1e-12
assert np.allclose(8*S,[[5,2,1],[2,4,2],[1,2,5]])
assert abs(S[0,2]/math.sqrt(S[0,0]*S[2,2])-.2)<1e-14
assert abs(S[0,2]-S[0,1]*S[1,2]/S[1,1])<1e-14
assert abs(-K[0,1]/math.sqrt(K[0,0]*K[1,1])-1/math.sqrt(6))<1e-14

# Generated article checks.
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
slug=Path(__file__).stem
source=(root/"research"/"content"/(slug+".md")).read_text()
body=(root/"articles"/(slug+".qmd")).read_text().split("## See also",1)[0]
assert len(re.findall(r"\{\{cite:",source))>=5
assert len(set(re.findall(r"\{\{cite:([^}]+)",source)))>=2
assert "Your turn" in body and "## Check yourself" in body
check=body.split("## Check yourself",1)[1]
assert check.count('collapse="true" title="Answer"') in {2,3}
assert len(set(re.findall(r"../questions/([\w-]+)\.qmd",check))) in {2,3}

for token in ['0.408248', '1/8']:
    assert token in body, (slug,token)
print(slug+" checks passed")
