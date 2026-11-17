"""Recompute the article's displayed examples and inspect the generated article."""
from pathlib import Path
import math,re,json
import numpy as np
import sympy as sp
from itertools import product
ROOT=Path(__file__).resolve().parents[1]
SLUG='normal-normal-model'
article=(ROOT / "articles" / (SLUG+".qmd")).read_text(encoding="utf-8")
body=article.split("## See also",1)[0]
checks=0
def check(condition):
    global checks
    assert condition, SLUG
    checks+=1
def close(actual,expected,rtol=1e-10,atol=1e-12):
    check(np.allclose(np.asarray(actual,dtype=float),np.asarray(expected,dtype=float),rtol=rtol,atol=atol))

from scipy.stats import norm
xs=np.array([4.,6.,8.]);P=1/9+len(xs)/4;h=5/9+xs.sum()/4;m=h/P;v=1/P
close([xs.mean(),P,m,v],[6,31/36,182/31,36/31]);close(math.sqrt(v),1.0776318121606494);close(4+v,160/31)
close(norm.ppf([.025,.975],loc=m,scale=math.sqrt(v)),[3.7588482,7.98308728],atol=1e-8)
close([(h+6/4)/(P+1/4),1/(P+1/4)],[5.9,.9])
check(np.mean([5,6,7])==xs.mean());check(v<9 and v<4/3 and 4+v>4)
mu=sp.symbols('mu',real=True)
check(sp.expand(sum((sp.Rational(int(x))-mu)**2 for x in xs)-sum((sp.Rational(int(x))-6)**2 for x in xs)-3*(6-mu)**2)==0)
# Law of total variance separates uncertainty about the mean from measurement noise.
close(v+4,160/31)

# Verify citation coverage in the composed article, including copied source blocks.
check(len(re.findall(r'class="cite-ref"',body))>=5)
proper_keys=set(re.findall(r'data-cite-key="([^" ]+)"',body))-{'r_faraway_leafblotch2026'}
check(len(proper_keys)>=2)

for token in ['182/31', '36/31', '160/31', '1.077632', '5.9']:
    check(token in body)
check("**Your turn.**" in body)
check(len(re.findall(r"^## Check yourself \{#check-yourself\}",body,re.M))==1)
print(f"{SLUG}: {checks} numerical, algebraic and rendered-content checks passed")
