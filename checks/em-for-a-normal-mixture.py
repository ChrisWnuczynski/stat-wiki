"""Recompute the examples and audit the generated article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats
from scipy.special import gammaln,digamma,logsumexp
ROOT=Path(__file__).resolve().parents[1]
SLUG='em-for-a-normal-mixture'
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

x=np.array([0.,4.]);mu=np.array([1.,2.]);lp=stats.norm.logpdf(x[:,None],mu)+np.log(.5)
r=np.exp(lp-logsumexp(lp,axis=1)[:,None]);N=r.sum(0);mean=(r*x[:,None]).sum(0)/N
var=(r*(x[:,None]-mean)**2).sum(0)/N
assert np.allclose(r[:,0],[.817574476,.075858180],atol=1e-8)
assert np.allclose(N,[.89343266,1.10656734]) and np.allclose(N/2,[.44671633,.55328367])
assert np.allclose(mean,[.33962573,3.34057145]) and np.allclose(var,[1.24315729,2.20286818])
old=logsumexp(lp,axis=1).sum();new=logsumexp(stats.norm.logpdf(x[:,None],mean,np.sqrt(var))+np.log(N/2),axis=1).sum()
assert np.isclose(old,-5.4438684152539345) and np.isclose(new,-3.8044293297438103) and new>old
x=np.array([0.,2.]);r=np.array([[.75,.25],[.25,.75]]);N=r.sum(0);m=(r*x[:,None]).sum(0)/N
assert np.allclose(m,[.5,1.5]) and np.allclose((r*(x[:,None]-m)**2).sum(0)/N,[.75,.75])
assert stats.norm.pdf(1,0)==stats.norm.pdf(1,2)
assert '3.340571' in body and '2.202868' in body

print(SLUG+": numerical, algebraic and generated-article checks passed")
