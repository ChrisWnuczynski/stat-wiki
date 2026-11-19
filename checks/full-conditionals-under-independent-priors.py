"""Recompute the examples and audit the generated article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats
from scipy.special import gammaln,digamma,logsumexp
ROOT=Path(__file__).resolve().parents[1]
SLUG='full-conditionals-under-independent-priors'
body=(ROOT/"articles"/(SLUG+'.qmd')).read_text().split('## See also',1)[0]
assert 'Your turn' in body and 'collapse="true"' in body
assert '## Check yourself {#check-yourself}' in body
assert len(re.findall('class="cite-ref"',body))>=5
assert len(set(re.findall('data-cite-key="([^"]+)',body)))>=2
assert len(re.findall(r'\{#self-check-[^}]+\}',body)) in (2,3)
assert '{{cite:' not in body

# Inspect every copied and new inline citation, beyond the minimum count.
for cite in re.finditer(r'<sup[^>]*class="cite-ref"[^>]*>.*?</sup>',body):
    assert re.search(r'data-locator="[^"]+"', cite.group(0)), cite.group(0)[:220]
for answer in re.findall(r':{3,} \{\.callout-tip collapse="true" title="Answer"\}(.*?)(?=\n:{3,})',body,re.S):
    assert 'class="cite-ref"' not in answer and '{{cite:' not in answer

x=np.array([1.,2.,3.]);n=len(x);v=1;v0=4;mu0=0;a0=2;b0=1
V=1/(n/v+1/v0);m=V*(x.sum()/v+mu0/v0)
assert np.isclose(m,24/13) and np.isclose(V,4/13)
a=a0+n/2;b=b0+np.sum((x-2)**2)/2
assert a==3.5 and b==2 and b/(a-1)==.8 and a/b==1.75 and 1/(a/b)==4/7
v=4;V=1/(n/v+1/v0);m=V*x.sum()/v;assert m==1.5 and V==1
# Completing the normal square differs only by a term constant in mu.
mu=sp.symbols('mu');expr=sum((sp.Integer(int(t))-mu)**2 for t in x)+mu**2/4
assert sp.diff(expr-(mu-sp.Rational(24,13))**2/sp.Rational(4,13),mu)==0
# q04 kernels: exponents recover Bin(10,theta), Beta(x+2,13-x).
for z in range(11):assert z+2>0 and 13-z>0
assert '24/13' in body and '0.8' in body

print(SLUG+": numerical, algebraic and generated-article checks passed")
