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

from scipy.stats import norm
import numpy as np
import sympy as sp
n=np.array([25,100,400]);probs=2*norm.sf(.2*np.sqrt(n))
assert np.allclose(probs,[.31731050786291415,.04550026389635839,.00006334248366624])
assert np.all(np.diff(probs)<0) and np.allclose(1/n,[.04,.01,.0025])
n0,sigma=sp.symbols('n0 sigma',positive=True)
mse=sigma**2/n0+1/n0**2
assert sp.limit(mse,n0,sp.oo)==0
assert 1/400 == (1/100)/4
assert np.sqrt((1/100)/(1/400)) == 2
theta,total,nobs=sp.symbols("theta total nobs", positive=True)
ell=total*sp.log(theta)-nobs*theta
assert sp.solve(sp.diff(ell,theta),theta)==[total/nobs]
assert sp.simplify(sp.diff(ell,theta,2)+total/theta**2)==0
assert sp.limit(theta/nobs,nobs,sp.oo)==0
assert abs(2*norm.cdf(2)-1-.9544997361036416)<1e-14
assert abs(norm.ppf(.995)-2.5758293035489004)<1e-14
assert "0.31731" in article and "0.00006334" in article

print("consistent-estimator: numerical, algebra and generated-content checks passed")
