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

import sympy as sp
import numpy as np
# Orthogonal innovations with a finite MA filter give a Toeplitz covariance.
a=np.array([1.,.4]);variance=4*(a@a);cov=4*a[0]*a[1]
assert np.allclose([variance,cov,cov/variance],[4.64,1.6,.3448275862068966])
assert np.allclose([.4*5,4,4*(1+.4**2)],[2,4,4.64])
assert np.allclose([4*(1+0**2),4*0,0*5],[4,0,0])
z,h=sp.symbols('z h',real=True);w=sp.pi/6
# Equal uncorrelated amplitude variances give covariance depending only on lag.
harmonic_cov=sp.cos(w*z)*sp.cos(w*(z+h))+sp.sin(w*z)*sp.sin(w*(z+h))
assert sp.trigsimp(harmonic_cov-sp.cos(w*h))==0
for f in [sp.cos,sp.sin]:
 assert sp.trigsimp(sp.expand_trig(f(w*z)-2*sp.cos(w)*f(w*(z-1))+f(w*(z-2))))==0
assert "property-representation" in article
assert "4.64" in article and "0.34483" in article

print("wold-decomposition: numerical, algebra and generated-content checks passed")
