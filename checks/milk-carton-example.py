"""Recompute the article's displayed examples and inspect the generated article."""
from pathlib import Path
import math,re,json
import numpy as np
import sympy as sp
from itertools import product
ROOT=Path(__file__).resolve().parents[1]
SLUG='milk-carton-example'
article=(ROOT / "articles" / (SLUG+".qmd")).read_text(encoding="utf-8")
body=article.split("## See also",1)[0]
checks=0
def check(condition):
    global checks
    assert condition, SLUG
    checks+=1
def close(actual,expected,rtol=1e-10,atol=1e-12):
    check(np.allclose(np.asarray(actual,dtype=float),np.asarray(expected,dtype=float),rtol=rtol,atol=atol))

from scipy.stats import t as t_law
x=np.array([1.035,1.019,1.068,1.084,1.077,.998,1.041,1.037,1.051,1.102]);n=len(x);mean=x.mean();s=x.std(ddof=1);se=s/math.sqrt(n)
check(sum(x<1)==1);close(x.sum(),10.512);close(mean,1.0512);close(s,.03169227035098626);close(se,.010021975853094053)
t=(mean-1.1)/se;pv=2*t_law.sf(abs(t),n-1);ci=mean+np.array([-1,1])*t_law.ppf(.975,n-1)*se
close(t,-4.869299299392553);close(pv,.000884373588752854);close(ci,[1.02852872,1.07387128],atol=1e-8)
close([np.median(x),min(x),max(x),np.ptp(x)],[1.046,.998,1.102,.104]);z=np.sort(x);close([np.median(z[:5]),np.median(z[5:])],[1.035,1.077])
close((mean-1.05)/se,.11973686801785874);close(t_law.ppf(.975,9),2.2621571628540993)
check(abs((mean-1.05)/se)<t_law.ppf(.975,9))

# Verify citation coverage in the composed article, including copied source blocks.
check(len(re.findall(r'class="cite-ref"',body))>=5)
proper_keys=set(re.findall(r'data-cite-key="([^" ]+)"',body))-{'r_faraway_leafblotch2026'}
check(len(proper_keys)>=2)

for token in ['1.0512', '0.03169', '4.869', '0.000884', '1.0285', '1.073871']:
    check(token in body)
check("**Your turn.**" in body)
check(len(re.findall(r"^## Check yourself \{#check-yourself\}",body,re.M))==1)
print(f"{SLUG}: {checks} numerical, algebraic and rendered-content checks passed")
