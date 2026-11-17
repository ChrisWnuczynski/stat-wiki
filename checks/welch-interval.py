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

from math import sqrt
from scipy.stats import t,norm
import numpy as np
import sympy as sp
def interval(nx,ny,sx,sy,d):
 a=sx*sx/nx;b=sy*sy/ny;se=sqrt(a+b)
 df=(a+b)**2/(a*a/(nx-1)+b*b/(ny-1))
 c=t.ppf(.975,df);return se,df,c,d-c*se,d+c*se
assert np.allclose(interval(10,20,2,4,3),[1.0954451150103321,27.98181818181818,2.048467107, .7560167142,5.2439832858])
assert np.allclose(interval(15,10,15,12,-9.5),[5.4221766847,22.0999342538,2.0733294787,-20.741958759,1.741958759])
a,n=sp.symbols('a n',positive=True)
assert sp.simplify(4*a*a/(2*a*a/(n-1))-2*(n-1))==0
assert abs((2*norm.cdf(2)-1)-.9544997361036416)<1e-14
assert abs(norm.ppf(.995)-2.5758293035489004)<1e-14
assert "27.9818" in article and "0.7560" in article and "22.0999" in article

print("welch-interval: numerical, algebra and generated-content checks passed")
