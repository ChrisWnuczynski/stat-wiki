"""Recompute the article's displayed examples and inspect the generated article."""
from pathlib import Path
import math,re,json
import numpy as np
import sympy as sp
from itertools import product
ROOT=Path(__file__).resolve().parents[1]
SLUG='jackknife-bias-and-standard-error'
article=(ROOT / "articles" / (SLUG+".qmd")).read_text(encoding="utf-8")
body=article.split("## See also",1)[0]
checks=0
def check(condition):
    global checks
    assert condition, SLUG
    checks+=1
def close(actual,expected,rtol=1e-10,atol=1e-12):
    check(np.allclose(np.asarray(actual,dtype=float),np.asarray(expected,dtype=float),rtol=rtol,atol=atol))

x=np.array([1.,2.,6.]);n=len(x);T=x.mean()**2
rep=np.array([np.delete(x,i).mean()**2 for i in range(n)]);average=rep.mean();bias=(n-1)*(average-T);corrected=T-bias
close(T,9);close(rep,[16,12.25,2.25]);close(average,61/6);close(bias,7/3);close(corrected,20/3)
pseudo=n*T-(n-1)*rep;close(pseudo,[-5,2.5,22.5]);close(pseudo.mean(),corrected)
v=(n-1)/n*sum((rep-average)**2);close(v,2425/36);close(math.sqrt(v),math.sqrt(2425)/6)
close(sum((pseudo-pseudo.mean())**2)/(n*(n-1)),v)
means=np.array([np.delete(x,i).mean() for i in range(n)]);close(means,[4,3.5,1.5]);close(means.mean(),3);close((n-1)/n*sum((means-means.mean())**2),7/3)
# Recompute the five-observation mean example as well.
z=np.array([2.,4.,6.,8.,10.]);r=np.array([np.delete(z,i).mean() for i in range(5)])
close(z.mean(),6);close(r,[7,6.5,6,5.5,5]);close(r.mean(),6);close(sum((r-6)**2),2.5);close(4/5*sum((r-6)**2),2);close(z.var(ddof=1),10);close(math.sqrt(2),1.414,atol=.0005)
m,a,b=sp.symbols('m a b',positive=True)
# E[T_n]=theta+a/n+b/n²: the first-order term cancels exactly.
check(sp.simplify(m*(a/m)-(m-1)*(a/(m-1)))==0)
check(sp.simplify(m*b/m**2-(m-1)*b/(m-1)**2)==-b/(m*(m-1)))

# Verify citation coverage in the composed article, including copied source blocks.
check(len(re.findall(r'class="cite-ref"',body))>=5)
proper_keys=set(re.findall(r'data-cite-key="([^" ]+)"',body))-{'r_faraway_leafblotch2026'}
check(len(proper_keys)>=2)

for token in ['61/6', '20/3', '2425', '1.52753']:
    check(token in body)
check("**Your turn.**" in body)
check(len(re.findall(r"^## Check yourself \{#check-yourself\}",body,re.M))==1)
print(f"{SLUG}: {checks} numerical, algebraic and rendered-content checks passed")
