"""Recompute the article examples independently and inspect generated prose."""
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
for answer in re.findall(r'::: \{\.callout-tip collapse="true" title="Answer"\}\n(.*?)\n:::', source, re.S):
    assert "{{cite:" not in answer

import numpy as np
from math import gcd
P=np.array([[.5,.5],[.25,.75]])
pi=np.array([1/3,2/3])
assert np.allclose(pi@P,pi)
assert np.allclose(P@P,[[.375,.625],[.3125,.6875]])
waiting=1/(1-P[1,1])
return_mean=1+P[0,1]*waiting
assert waiting==4 and return_mean==3 and abs(return_mean-1/pi[0])<1e-14
Q=np.array([[0,1],[1,0]])
assert np.array_equal(Q@Q,np.eye(2)) and gcd(2,4)==2
R=np.array([[.9,.1],[.4,.6]])
assert abs((R@R)[0,1]-.15)<1e-14
assert np.allclose(np.array([.8,.2])@R,[.8,.2])
for value in ("0.375", "0.3125", "0.6875", "0.15"):
    assert value in article, value

print("recurrence-and-period: numerical, algebra and generated-content checks passed")
