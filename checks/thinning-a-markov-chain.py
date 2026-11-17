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
rho=.8;N=1000;k=5
C=rho**np.abs(np.subtract.outer(np.arange(17),np.arange(17)))
weights=np.ones(17)/17
finite=(1+2*sum((1-h/17)*rho**h for h in range(1,17)))/17
assert abs(weights@C@weights-finite)<1e-14
tau=(1+rho)/(1-rho);rho_k=rho**k;tau_k=(1+rho_k)/(1-rho_k)
assert np.allclose([tau,rho_k,tau_k],[9,.32768,1.9747739171822944])
assert np.allclose([N/tau,(N/k)/tau_k],[111.111111111,101.2774161966])
assert np.allclose([tau/N,tau_k/(N/k)],[.009,.009873869585911])
P=np.array([[.9,.1],[.4,.6]]);pi=np.array([.8,.2])
assert np.allclose(pi@np.linalg.matrix_power(P,5),pi)
assert (1/(N/k))/(1/N)==5
assert "101.28" in article and "0.32768" in article

print("thinning-a-markov-chain: numerical, algebra and generated-content checks passed")
