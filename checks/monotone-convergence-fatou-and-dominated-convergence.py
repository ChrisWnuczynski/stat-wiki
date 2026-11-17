"""Recompute the worked calculations and inspect the generated article."""
from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
source = (root / "research" / "content" / (Path(__file__).stem + ".md")).read_text()
article = (root / "articles" / (Path(__file__).stem + ".qmd")).read_text()
body = article.split("## See also", 1)[0]
assert len(re.findall(r"\{\{cite:", source)) >= 5
assert len(set(re.findall(r"\{\{cite:([^}]+)", source))) >= 2
assert "Your turn" in body and 'collapse="true"' in body

from scipy.integrate import quad
from math import sqrt
for n in [1,2,10,100]:
    numerical=n/n**2+quad(lambda u:1/sqrt(u),1/n**2,1)[0]
    assert abs(numerical-(2-1/n))<1e-10
    assert n*(1/n)==1
    assert abs(sqrt(n)/n-1/sqrt(n))<1e-14
    assert n/n==1
assert '1.9' in body and '2-\\frac1n' in body

print("monotone-convergence-fatou-and-dominated-convergence checks passed")
