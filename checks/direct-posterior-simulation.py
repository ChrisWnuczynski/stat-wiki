"""Recompute numerical examples and inspect the generated article."""
from pathlib import Path
import re
import numpy as np
from scipy.stats import norm, f, t, gamma, beta, betabinom, invgamma
from scipy.special import expit, betaln, gammaln
ROOT = Path(__file__).resolve().parents[1]
SLUG = Path(__file__).stem

a,b=4.,8.;C=np.diag([.1,.025]);q=t.sf((1.5-2)/np.sqrt((b/a)*C[1,1]),2*a)
assert np.isclose(q,.972116735549502) and np.isclose(np.sqrt(q*(1-q)/10000),.001646383552337718)
assert np.allclose(np.linalg.cholesky(C)@np.linalg.cholesky(C).T,C)
# Independent sampling verifies both the IG mean and marginal t probability.
rng=np.random.default_rng(488502);M=160000
G=rng.gamma(a,1,size=M);v=b/G;Z=rng.normal(size=(M,2));B=np.array([1,2])+np.sqrt(v)[:,None]*(Z@np.linalg.cholesky(C).T)
assert abs(v.mean()-b/(a-1))<.025
assert abs(np.mean(B[:,1]>1.5)-q)<.003
assert abs(np.corrcoef(B[:,0],B[:,1])[0,1])<.015
assert abs(np.corrcoef((B[:,0]-1)**2,v)[0,1])>.3
# Marginal variance shape differs from the full conditional by p/2.
n,p,SSE=10,2,16;assert (n-p)/2==4 and n/2==5
# Normal-inverse-gamma update and flat-mean prior marginalisation.
k0,m0,a0,b0,n,xb,SS=2.,1.,3.,4.,5,2.,6.
kn=k0+n;mn=(k0*m0+n*xb)/kn;an=a0+n/2;bn=b0+.5*(SS+k0*n/kn*(xb-m0)**2)
assert np.allclose([kn,mn,an,bn],[7,12/7,5.5,54/7])
assert np.allclose(2+np.array([-1,1])*2.306*np.sqrt(.05),[1.48436273,2.51563727])
assert np.allclose(1+np.array([-1,1])*2.306*np.sqrt(2.2),[-2.42035074,4.42035074])
assert np.isclose(np.array([1,4])@C@np.array([1,4]),.5)
EXPECT=["0.9721167","0.001646","marginal"]

source = (ROOT / "research" / "content" / (SLUG + ".md")).read_text()
article = (ROOT / "articles" / (SLUG + ".qmd")).read_text().split("## See also", 1)[0]
assert "Motivating example" in article and "Your turn" in article
assert "## Check yourself {#check-yourself}" in article
citations = list(re.finditer(r'<sup[^>]*class="cite-ref"[^>]*>.*?</sup>', article))
assert len(citations) >= 5
assert len(set(re.findall(r'data-cite-key="([^"]+)"', article))) >= 2
for mark in citations:
    assert re.search(r'data-locator="(?:&quot;|ch\.|Chs\.|§|Thm\.|Lem\.|Lems\.|p\.|pp\.|Glossary|Ex\.|Summary|Def\.|Sec\.|Props\.|Introduction|Description|Format|Source|References|Examples|Notes|Basic Theory)', mark.group(0), re.I), mark.group(0)[:220]
practice = article.split("## Check yourself", 1)[1].split("\n## ", 1)[0]
ids = re.findall(r"(?m)^### .*\{#self-check-([^}]+)\}", practice)
assert 2 <= len(ids) <= 3 and len(set(ids)) == len(ids)
assert practice.count('collapse="true" title="Answer"') == len(ids)
assert all((ROOT / "questions" / (q + ".qmd")).exists() for q in ids)
for answer in re.findall(r'::: \{\.callout-tip collapse="true" title="Answer"\}\n(.*?)\n:::', source, re.S):
    assert "{{cite:" not in answer
assert not re.search(r"\b(?:inherited|retained|existing|original|earlier version|the manual|not a claim|not proved here|question bank item|linked chapter)\b", source, re.I)
for snippet in EXPECT:
    assert snippet in article, (SLUG, snippet)
print(SLUG + ": arithmetic, algebra and generated content pass")
