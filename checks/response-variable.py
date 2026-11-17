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
x=np.array([0.,1.,2.]); y=np.array([0.,0.,1.])
xc=x-x.mean();yc=y-y.mean()
sxx=xc@xc;syy=yc@yc;sxy=xc@yc
assert np.allclose([sxx,syy,sxy],[2,2/3,1])
b=sxy/sxx;a=y.mean()-b*x.mean()
rev=sxy/syy;ar=x.mean()-rev*y.mean()
assert np.allclose([a,b,ar,rev,b*rev],[-1/6,.5,.5,1.5,.75])
fit=np.linalg.lstsq(np.column_stack([np.ones(3),x]),10+2*y,rcond=None)[0]
assert np.allclose(fit,[29/3,1])
assert np.allclose([3204.23-18.84*z for z in [15,35]],[2921.63,2544.83])
assert "2921.63" in article and "2544.83" in article and "29/3" in article

print("response-variable: numerical, algebra and generated-content checks passed")
