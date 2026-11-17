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

from itertools import product
from fractions import Fraction as F
vals=[-1,0,1];probs=[F(1,4),F(1,2),F(1,4)]
for n in [2,4]:
    eb=eb2=es=es2=ev=F(0)
    for inds in product(range(3),repeat=n):
        x=[F(vals[j]) for j in inds];w=__import__('functools').reduce(lambda a,j:a*probs[j],inds,F(1))
        mean=sum(x)/n;ss=sum((z-mean)**2 for z in x);s=ss/(n-1)
        eb+=w*mean;eb2+=w*mean**2;es+=w*s;es2+=w*s*s;ev+=w*ss/n
    assert eb==0 and eb2==F(1,2*n) and es==F(1,2)
    assert ev==F(n-1,2*n)
    expected=(F(1,2)-F(n-3,n-1)*F(1,4))/n
    assert es2-es**2==expected
    if n==2:assert expected==F(3,8)
assert '3/8' in body and '1/8' in body

print("moments-of-the-sample-mean-and-variance checks passed")
