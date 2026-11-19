"""Recompute numerical examples and inspect the generated article."""
from pathlib import Path
import re
import numpy as np
from scipy.stats import norm, f, t, gamma, beta, betabinom, invgamma
from scipy.special import expit, betaln, gammaln
ROOT = Path(__file__).resolve().parents[1]
SLUG = Path(__file__).stem

x=np.arange(5.);y=np.array([1.,2,1,4,2]);X=np.c_[np.ones(5),x]
C=np.linalg.inv(X.T@X);bh=np.linalg.lstsq(X,y,rcond=None)[0];r=y-X@bh;sse=r@r
assert np.allclose(bh,[1.2,.4]) and np.allclose(C,[[.6,-.2],[-.2,.1]])
assert np.isclose(sse,4.4) and np.allclose(X.T@r,0)
a=np.array([1.,2]);assert np.isclose(a@C@a,.2)
assert np.allclose(np.sqrt(np.diag(C)),[.7745966692414834,.31622776601683794])
assert np.isclose(t.sf((0-bh[1])/np.sqrt(sse/3*C[1,1]),3),.8134893188136102)
# Complete the square at an arbitrary coefficient vector.
b=np.array([-2.,1.3]);assert np.isclose(np.sum((y-X@b)**2),sse+(b-bh)@X.T@X@(b-bh))
V0=np.diag([2.,3]);v=4.;mn=np.linalg.solve(X.T@X/v+np.linalg.inv(V0),X.T@y/v)
assert np.allclose((X.T@X/v+np.linalg.inv(V0))@mn,X.T@y/v)
assert np.allclose(2+np.array([-1,1])*2.306*np.sqrt(.05),[1.48436273,2.51563727])
assert np.isclose(8/(4-1),8/3)
# A nonzero proper normal prior: direct quadratic expansion about its posterior mean.
m0=np.array([-1.,2.]);V0=np.array([[2.,.3],[.3,3.]])
precision=X.T@X/v+np.linalg.inv(V0)
mn=np.linalg.solve(precision,X.T@y/v+np.linalg.solve(V0,m0))
def quadratic(b):
    return np.sum((y-X@b)**2)/v+(b-m0)@np.linalg.solve(V0,b-m0)
for b in [np.zeros(2),np.ones(2),np.array([-.2,3.])]:
    assert np.isclose(quadratic(b)-quadratic(mn),(b-mn)@precision@(b-mn))
# Numerical integration independently verifies the scalar normal/IG mixture.
from scipy.integrate import quad
scale=np.sqrt((sse/3)*C[1,1])
for u in [-1.,.4,2.]:
    mixture=quad(lambda vv:norm.pdf(u,bh[1],np.sqrt(vv*C[1,1]))*invgamma.pdf(vv,1.5,scale=sse/2),0,np.inf,epsabs=1e-11)[0]
    assert np.isclose(mixture,t.pdf((u-bh[1])/scale,3)/scale,rtol=1e-8,atol=1e-10)
# Full bank regression summary: scale, variance and mean/new-response intervals.
nu=8;s2=2.;Cbank=np.diag([.1,.025])
assert np.allclose([np.array([1,z])@Cbank@np.array([1,z]) for z in [0,4]],[.1,.5])
assert np.allclose(1+np.array([-1,1])*2.306*np.sqrt(2.2),[-2.42035074,4.42035074])
assert np.allclose(1+np.array([-1,1])*2.306*np.sqrt(.2),[-.03127455,2.03127455])
assert np.isclose((nu/(nu-2))*(s2/40),(8/3)/40)
EXPECT=["0.813489","0.774597","0.8"]

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
