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
Q=sp.Matrix([[-2,2,0],[4,-7,3],[0,6,-6]])
pi=sp.Matrix([[sp.Rational(4,7),sp.Rational(2,7),sp.Rational(1,7)]])
assert pi*Q==sp.zeros(1,3) and sum(pi)==1
assert pi*(10*Q)==sp.zeros(1,3)
assert 1/(-10*Q[0,0])==sp.Rational(1,10)/(-Q[0,0])
assert pi[1]+2*pi[2]==sp.Rational(4,7)
assert pi[0]*2==pi[1]*4 and pi[1]*3==pi[2]*6
rho=sp.Rational(1,2);n=sp.symbols('n',integer=True,nonnegative=True)
assert sp.summation((1-rho)*rho**n,(n,0,sp.oo))==1
assert sp.summation(n*(1-rho)*rho**n,(n,0,sp.oo))==1
weights=np.array([1,3,2]);discrete=weights/weights.sum()
P=np.array([[0,1,0],[1/3,0,2/3],[0,1,0]])
assert np.allclose(discrete@P,discrete)
assert "4/7" in article and "2/7" in article and "1/7" in article

print("birth-death-balance: numerical, algebra and generated-content checks passed")
