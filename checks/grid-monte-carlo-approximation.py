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
x=np.array([0.,1.,2.]);weights=np.array([1.,2.,1.]);p=weights/weights.sum()
assert np.array_equal(p,[.25,.5,.25]) and np.array_equal(p.cumsum(),[.25,.75,1])
mean=p@x;variance=p@((x-mean)**2)
assert mean==1 and variance==.5 and abs(np.sqrt(variance/10000)-.007071067811865475)<1e-16
assert np.allclose(np.array([1,3])/4,[.25,.75])
z1,z2=sp.symbols('z1 z2',real=True)
J=sp.Matrix([sp.exp(z1),sp.exp(z2)]).jacobian([z1,z2]).det()
assert sp.simplify(J-sp.exp(z1)*sp.exp(z2))==0
# Inverse CDF cells have exactly the requested interval lengths.
edges=np.r_[0,p.cumsum()];assert np.array_equal(np.diff(edges),p)
assert "0.007071" in article and "piecewise-constant" in article

print("grid-monte-carlo-approximation: numerical, algebra and generated-content checks passed")
