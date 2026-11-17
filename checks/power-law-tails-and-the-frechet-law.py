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

from math import log,sqrt,exp
from scipy.special import expm1
n=10000;alpha=2
a=n**(1/alpha)
exact=(-expm1(-log(2)/n))**(-1/alpha)
approx=a/sqrt(log(2))
assert abs(exact-120.1143222712254)<1e-7
assert abs(approx-120.11224087864498)<1e-10
assert abs((exact-approx)-.00208139258)<1e-8
assert abs((1-.25/100)**100-.7785570395897228)<1e-14
assert abs(exp(-.25)-.7788007830714049)<1e-14
assert sqrt(4)==2
for number in ['120.112241','120.114322','0.778557','0.778801']:
    assert number in body


# Rate-two exponential maximum in the linked comparison.
for n in [10,100,1000]:
    z=.7;rate=2;a=1/rate;b=log(n)/rate
    exact=(1-exp(-rate*(b+a*z)))**n
    assert abs(exact-exp(-exp(-z)))<1/n

assert abs(log(10000)-log(log(2))-9.58)<.005
assert abs(sqrt(2)-1.41)<.005
print("power-law-tails-and-the-frechet-law checks passed")
