"""Recompute examples independently and inspect the generated article."""
import numpy as np
import math

risk=np.array([.3+.2,.3]);leaves=np.array([2,5])
assert np.allclose(risk+.15*leaves,[.8,1.05])
assert np.allclose(risk+.05*leaves,[.6,.55])
cross=(risk[0]-risk[1])/(leaves[1]-leaves[0])
assert abs(cross-1/15)<1e-14
assert abs((risk+cross*leaves)[0]-(risk+cross*leaves)[1])<1e-14
assert abs((.24-.12)/(4-1)-.04)<1e-14
# Finite-tree comparisons verify monotonic optimum leaf counts and the breakpoint.
penalties=np.linspace(0,.2,201)
chosen=[leaves[np.argmin(risk+a*leaves)] for a in penalties]
assert np.all(np.diff(chosen)<=0)
assert .07143+.03117==.1026
assert abs(.1111-1/9)<.0001

# Dynamic-programming pruning agrees with every explicitly enumerated subtree.
def risks(tree):
    risk,children=tree
    if not children:return [(risk,1)]
    left,right=children
    return [(risk,1)]+[(rl+rr,nl+nr) for rl,nl in risks(left) for rr,nr in risks(right)]
def dp(tree,alpha):
    risk,children=tree
    if not children:return risk+alpha
    return min(risk+alpha,sum(dp(c,alpha) for c in children))
tree=(.5,[(.3,[(.05,[]),(.10,[])]),(.2,[(.04,[]),(.06,[])])])
for a in np.linspace(0,.3,61):
    assert abs(dp(tree,a)-min(r+a*n for r,n in risks(tree)))<1e-13

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

for token in ['0.066667', '1.05']:
    assert token in body, (slug,token)
print(slug+" checks passed")
