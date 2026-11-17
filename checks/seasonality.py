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
Y=np.array([[80,100,120,100],[90,110,130,110]])
means=Y.mean(axis=1); effects=Y-means[:,None]
assert np.array_equal(means,[100,110])
assert np.array_equal(effects,[[-20,0,20,0]]*2)
assert np.array_equal(Y.mean(axis=0),[85,105,125,105])
assert Y.mean()==105 and np.all(effects.sum(axis=1)==0)
assert np.array_equal(np.diff(Y,axis=0),[[10]*4])
third=np.array([100,120,140,120]);assert third.mean()==120
assert np.array_equal(third-Y[1],[10]*4)
assert np.array_equal(third-third.mean(),[-20,0,20,0])
assert "105" in article and "(-20,0,20,0)" in article

print("seasonality: numerical, algebra and generated-content checks passed")
