"""Independently recompute the article's finite examples."""
from pathlib import Path
import re
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT / "articles" / "hartigan-wong-algorithm.qmd").read_text(encoding="utf-8")
assert "Your turn" in text
assert "## Check yourself {#check-yourself}" in text
assert len(re.findall('class="cite-ref"',text))>=5
assert len(set(re.findall('data-cite-key="([^\"]+)',text)))>=2

pts=[sp.Matrix(p) for p in [(0,0),(0,1),(10,0),(10,1)]]
def wss(ids):
 c=sum((pts[i] for i in ids),sp.zeros(2,1))/len(ids)
 return sum(((pts[i]-c).dot(pts[i]-c) for i in ids),sp.Integer(0))
assert wss([0,2])+wss([1,3])==100
assert wss([0])+wss([1,2,3])==sp.Rational(202,3)==sp.Rational(606,9)
assert wss([0,1])+wss([2,3])==1
assert 2*25==50 and sp.Rational(2,3)*26==sp.Rational(52,3)
assert sp.Rational(52,3)-50==-sp.Rational(98,3)
assert sp.Rational(2,3)*16-sp.Rational(3,2)*9==-sp.Rational(17,6)
for token in ['100','202/3','67.333333','52/3']:assert token in text,token

print("hartigan-wong-algorithm: exact example recomputation and generated-article assertions passed")
