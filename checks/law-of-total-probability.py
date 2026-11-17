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

from fractions import Fraction as F
import numpy as np
shares=[F(15,100),F(35,100),F(50,100)]
rates=[F(1,100),F(5,100),F(2,100)]
joint=[a*b for a,b in zip(shares,rates)];total=sum(joint)
assert total==F(29,1000) and joint[0]/total==F(3,58)
assert np.allclose([float(x/total) for x in joint],[.051724137931,.603448275862,.344827586207])
received=F(9,10)*F(1,4)+F(5,100)*F(3,4)
assert received==F(21,80) and (F(9,10)*F(1,4))/received==F(6,7)
assert (F(1,100)*F(1,2))/(F(1,100)*F(1,2)+F(95,100)*F(1,2))==F(1,96)
assert F(2,10)*F(1,100)+F(8,10)*F(4,100)==F(34,1000)
assert (F(95,100)*F(2,3))/(F(95,100)*F(2,3)+F(10,100)*F(1,3))==F(95,100)
assert F(9,10)*(1-F(1,10)**2)==F(891,1000)
assert "0.05172" in article and "0.029" in article and "0.2625" in article

print("law-of-total-probability: numerical, algebra and generated-content checks passed")
