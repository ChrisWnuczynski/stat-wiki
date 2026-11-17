"""Recompute the examples and inspect the generated one-hot-encoding article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats

ROOT=Path(__file__).resolve().parents[1]
SLUG='one-hot-encoding'
source=(ROOT / "research" / "content" / (SLUG+".md")).read_text()
body=(ROOT / "articles" / (SLUG+".qmd")).read_text().split("## See also",1)[0]
assert "Your turn" in body and 'collapse="true"' in body
assert "## Check yourself {#check-yourself}" in body
assert len(re.findall('class="cite-ref"',body))>=5

p=np.array([.2,.5,.3]); y=np.array([0,1,0]); g=p-y
assert np.isclose(-np.log(p[1]),.6931471805599453)
assert np.allclose(g,[.2,-.5,.3]) and np.isclose(g.sum(),0)
z=np.array([0,.5,-.2]);s=np.exp(z)/sum(np.exp(z))
assert np.allclose(s,[.28839620365112,.475484955348767,.236118841000113])
assert np.allclose(s,np.exp(z+5)/sum(np.exp(z+5)))
assert np.isclose(np.log(s[2]/s[1]),-.7)
X=np.c_[np.ones(3),np.eye(3)]
assert np.linalg.matrix_rank(X)==3 and X.shape==(3,4)
assert np.isclose(np.linalg.norm(np.eye(3)[0]-np.eye(3)[1]),np.sqrt(2))
assert np.isclose(-np.log(.25),1.3862943611198906)
assert '0.693147' in body and '0.475485' in body

print(SLUG+": numeric and generated-article checks passed")
