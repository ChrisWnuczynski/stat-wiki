"""Independently recompute the article's finite examples."""
from pathlib import Path
import re
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT / "articles" / "homogeneity-and-independence.qmd").read_text(encoding="utf-8")
assert "Your turn" in text
assert "## Check yourself {#check-yourself}" in text
assert len(re.findall('class="cite-ref"',text))>=5
assert len(set(re.findall('data-cite-key="([^\"]+)',text)))>=2

from scipy.stats import chi2_contingency,chi2
O=sp.Matrix([[12,8,10],[8,12,10]]);E=sp.ones(2,3)*10
Q=sum((O[i,j]-E[i,j])**2/E[i,j] for i in range(2) for j in range(3));assert Q==sp.Rational(8,5)
assert f'{chi2.sf(float(Q),2):.6f}'=='0.449329'
assert f'{chi2.sf(float(2*Q),2):.6f}'=='0.201897'
assert (2-1)*(3-1)==2
q,p,df,e=chi2_contingency([[8,2],[3,7]],correction=False)
assert abs(q-500/99)<1e-12 and df==1
for token in ['1.6','0.449329','0.201897']:assert token in text,token

print("homogeneity-and-independence: exact example recomputation and generated-article assertions passed")
