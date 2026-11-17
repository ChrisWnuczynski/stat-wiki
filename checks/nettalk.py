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

def parameters(d,h,c):return d*h+h*c+h+c
assert 7*29==203
assert 203*80+80*26==18320
assert parameters(203,80,26)==18426
assert 18320+(203+80+26)==18629
assert parameters(203,50,26)==11526
assert parameters(15,2,3)==41 and parameters(10,5,3)==73
assert (3-1)*(10+1)==22
assert 5000*26==130000 and abs(130000/18426-7.05524801910344)<1e-14
import sympy as sp
w,lam,eps=sp.symbols('w lam eps')
assert sp.diff(lam*w*w/2,w)==lam*w
assert sp.expand(w-eps*lam*w)==sp.expand((1-eps*lam)*w)
for val in ['18426','18629','11526','130000','7.055']:assert val in article

print("nettalk: numerical, algebra and generated-content checks passed")
