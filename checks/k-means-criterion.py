"""Independently recompute the article's finite examples."""
from pathlib import Path
import re
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT / "articles" / "k-means-criterion.qmd").read_text(encoding="utf-8")
assert "Your turn" in text
assert "## Check yourself {#check-yourself}" in text
assert len(re.findall('class="cite-ref"',text))>=5
assert len(set(re.findall('data-cite-key="([^\"]+)',text)))>=2

x=list(map(sp.Integer,[0,2,8,10]));m=sum(x)/4
T=sum((a-m)**2 for a in x);assert m==5 and T==68
def within(groups):return sum(sum((x[i]-sum(x[j] for j in g)/len(g))**2 for i in g) for g in groups)
assert within([[0,1],[2,3]])==4 and within([[0,2],[1,3]])==64
assert 2*(1-5)**2+2*(9-5)**2==64
assert 9*4==36 and 9*68==612
for token in ['68','64','36','612']:assert token in text,token

print("k-means-criterion: exact example recomputation and generated-article assertions passed")
