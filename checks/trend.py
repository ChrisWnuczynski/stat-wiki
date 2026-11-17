"""Recompute article examples and inspect generated content."""
from pathlib import Path
import re
ROOT = Path(__file__).resolve().parents[1]
SLUG = Path(__file__).stem
source = (ROOT / "research" / "content" / (SLUG + ".md")).read_text()
article = (ROOT / "articles" / (SLUG + ".qmd")).read_text().split("## See also", 1)[0]
assert "Motivating example" in article and "Your turn" in article
assert "## Check yourself {#check-yourself}" in article
assert len(re.findall(r'class="cite-ref"', article)) >= 5
assert len(set(re.findall(r'data-cite-key="([^"]+)"', article))) >= 2
practice = article.split("## Check yourself", 1)[1].split("\n## ", 1)[0]
questions = set(re.findall(r'\.\./questions/([\w-]+)\.qmd', practice))
assert 2 <= len(questions) <= 3, questions
assert all((ROOT / "questions" / (q + ".qmd")).exists() for q in questions)
for answer in re.findall(r'::: \{\.callout-tip collapse="true" title="Answer"\}\n(.*?)\n:::', source, re.S):
    assert "{{cite:" not in answer

import numpy as np
import sympy as sp
t=np.arange(1,6); y=np.array([3,5,7,9,11])
a,b=np.linalg.lstsq(np.column_stack([np.ones(5),t]),y,rcond=None)[0]
assert np.allclose([a,b],[1,2]) and np.all(np.diff(y)==2)
# Differencing independent errors is a linear map with shared opposite signs.
D=np.zeros((4,5))
for i in range(4):D[i,i]=-1;D[i,i+1]=1
C=4*D@D.T
assert np.all(np.diag(C)==8) and C[0,1]==-4 and C[0,1]/C[0,0]==-.5
z=sp.symbols('z');assert sp.expand((1+2*z)-(1+2*(z-4)))==8
assert np.allclose([20+.6*(30-20),20+.6**2*(30-20),9,9*(1+.6**2)],[26,23.6,9,12.24])
assert "12.24" in article and "variance $8$" in article

print("trend: numerical, algebra and generated-content checks passed")
