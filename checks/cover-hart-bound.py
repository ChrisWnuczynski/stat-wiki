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
r=np.array([.1,.3]);rb=r.mean();risk=np.mean(2*r*(1-r));bound=2*rb*(1-rb)
assert np.allclose([rb,risk,bound,np.var(r)],[.2,.3,.32,.01])
assert abs(risk-(bound-2*np.var(r)))<1e-14
assert np.allclose([min(.9,.1),2*.9*.1,(2*.9*.1)/.1],[.1,.18,1.8])
eta=sp.symbols('eta',real=True)
assert sp.simplify(2*eta*(1-eta)-2*(1-eta)*eta)==0
for values in [np.linspace(0,.5,101),np.array([0,.5]),np.array([.2])]:
 b=values.mean();e=np.mean(2*values*(1-values))
 assert b <= e+1e-14 <= 2*b*(1-b)+1e-13
assert np.allclose([1+np.sqrt(2/k) for k in [1,7,50]],[2.41421356237,1.53452248382,1.2])
assert "0.30" in article and "0.32" in article

print("cover-hart-bound: numerical, algebra and generated-content checks passed")
