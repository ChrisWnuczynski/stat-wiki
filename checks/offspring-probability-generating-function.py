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
from scipy.optimize import brentq
from math import exp
s=sp.symbols('s');f=sp.Rational(1,4)+s/4+s*s/2
mean=sp.diff(f,s).subs(s,1);var=sp.diff(f,s,2).subs(s,1)+mean-mean**2
assert mean==sp.Rational(5,4) and var==sp.Rational(11,16)
assert sp.factor(4*(f-s))==(s-1)*(2*s-1)
q=sp.Rational(0);values=[]
for _ in range(4):q=f.subs(s,q);values.append(float(q))
import numpy as np
assert np.allclose(values,[.25,.34375,.39501953125,.42677509784698486])
pq=brentq(lambda z: exp(1.5*(z-1))-z,0,.9)
assert abs(pq-.41718835613418864)<1e-12 and abs(exp(-1.5)-.22313016014842982)<1e-14
assert sp.factor(4*(sp.Rational(1,4)+3*s*s/4-s))==(s-1)*(3*s-1)
critical=sp.Rational(2,5)+s/5+2*s*s/5
assert sp.diff(critical,s).subs(s,1)==1 and sp.factor(5*(critical-s))==2*(s-1)**2
r=sp.symbols('r',positive=True);g=(1-r)/(1-r*s)
assert sp.simplify(g.subs(s,(1-r)/r)-(1-r)/r)==0
assert "0.417188" in article and "0.42678" in article

print("offspring-probability-generating-function: numerical, algebra and generated-content checks passed")
