"""Recompute the examples and audit the generated article."""
from pathlib import Path
import re
import numpy as np
import sympy as sp
from scipy import stats
from scipy.special import gammaln,digamma,logsumexp
ROOT=Path(__file__).resolve().parents[1]
SLUG='dirichlet-moments'
body=(ROOT/"articles"/(SLUG+'.qmd')).read_text().split('## See also',1)[0]
assert 'Your turn' in body and 'collapse="true"' in body
assert '## Check yourself {#check-yourself}' in body
assert len(re.findall('class="cite-ref"',body))>=5
assert len(set(re.findall('data-cite-key="([^"]+)',body)))>=2
assert len(re.findall(r'\{#self-check-[^}]+\}',body)) in (2,3)
assert '{{cite:' not in body

# Inspect every copied and new inline citation, beyond the minimum count.
for cite in re.finditer(r'<sup[^>]*class="cite-ref"[^>]*>.*?</sup>',body):
    assert re.search(r'data-locator="(?:&quot;|[Cc]h\.|Chs\.|§|Thm\.|Lem\.|Lems\.|p\.|pp\.|Glossary|Ex\.|Summary|Def\.|Sec\.|Props\.|biography,|Introduction|Description|Basic Theory|Convergence|Vector Spaces|Assumptions|Sampling|[“"])', cite.group(0)), cite.group(0)[:220]
for answer in re.findall(r':{3,} \{\.callout-tip collapse="true" title="Answer"\}(.*?)(?=\n:{3,})',body,re.S):
    assert 'class="cite-ref"' not in answer and '{{cite:' not in answer

a=np.array([2.,3.,5.]);A=a.sum();m=a/A;cov=(np.diag(m)-np.outer(m,m))/(A+1)
assert np.allclose(m,[.2,.3,.5]) and np.allclose(np.diag(cov),np.array([16,21,25])/1100)
c=np.array([1,-1,0]);assert np.isclose(c@cov@c,49/1100)
c=np.array([1,1,0]);assert np.isclose(c@cov@c,1/44)
r=np.array([2,1,0]);moment=np.exp(gammaln(A)-gammaln(A+r.sum())+(gammaln(a+r)-gammaln(a)).sum())
assert np.isclose(moment,3/220) and np.isclose(digamma(2)-digamma(10),-1.828968253968254)
a2=2*a;cov2=(np.diag(m)-np.outer(m,m))/(a2.sum()+1);assert np.allclose(cov2,cov*11/21)
a=np.ones(3);m=a/3;v=(np.diag(m)-np.outer(m,m))/4;assert np.isclose(v[0,0],1/18) and np.isclose(v[0,1],-1/36)
assert np.isclose(stats.beta.var(1,5),5/252) and np.isclose(-1*2/(6**2*7),-1/126)
a=np.array([9,7,17,13,5,15]);assert a.sum()==66 and a[[2,5]].sum()/66==16/33 and a[5]/a[3:].sum()==5/11
# Independent Monte Carlo and beta quantiles check the linked restaurant summaries.
a=np.array([108.79,47.6,11.36,59.25]);p=a/a.sum();assert np.allclose(p[[0,3]],[.4792511013,.2610132159])
assert np.allclose(stats.beta.ppf([.025,.975],a[0],a.sum()-a[0]),[.41464017,.54420841])
assert np.allclose([p[0],p[3],1-p[3],p[0]-p[3]],[.479,.261,.739,.218],atol=.0005)
for aa,bb,interval in [(a[0],227-a[0],[.415,.544]),(a[3],227-a[3],[.206,.320]),(227-a[3],a[3],[.680,.794])]:
    assert np.allclose(stats.beta.ppf([.025,.975],aa,bb),interval,atol=.0005)
assert np.allclose(np.array([63,19,3,38])+100*np.array([.4479,.2760,.0736,.2025])+1,a)
draws=np.random.default_rng(20261117).dirichlet(a,100000)
assert np.allclose(np.quantile(draws[:,0]-draws[:,3],[.025,.975]),[.109,.325],atol=.003)
assert '49' in body and '3/220' in body

print(SLUG+": numerical, algebraic and generated-article checks passed")
