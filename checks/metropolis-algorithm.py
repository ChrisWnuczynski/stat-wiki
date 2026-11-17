"""Recompute the worked calculations and inspect the generated article."""
from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
source = (root / "research" / "content" / (Path(__file__).stem + ".md")).read_text()
article = (root / "articles" / (Path(__file__).stem + ".qmd")).read_text()
body = article.split("## See also", 1)[0]
assert len(re.findall(r"\{\{cite:", source)) >= 5
assert len(set(re.findall(r"\{\{cite:([^}]+)", source))) >= 2
assert "Your turn" in body and 'collapse="true"' in body

import numpy as np
from fractions import Fraction as F
w=np.array([1.,2.,3.]);pi=w/w.sum();P=np.zeros((3,3))
for i in range(3):
    for j in range(3):
        if i!=j:P[i,j]=.5*min(1,w[j]/w[i])
    P[i,i]=1-P[i].sum()
assert np.allclose(P,[[0,.5,.5],[.25,.25,.5],[1/6,1/3,.5]])
assert np.allclose(pi@P,pi)
assert np.allclose(pi[:,None]*P,(pi[:,None]*P).T)
jump=pi*(1-P.diagonal());jump/=jump.sum()
assert np.allclose(jump,[.25,.375,.375])
assert F(1,3)*F(1,4)==F(1,12)
assert '3/8' in body and '1/12' in body

print("metropolis-algorithm checks passed")
