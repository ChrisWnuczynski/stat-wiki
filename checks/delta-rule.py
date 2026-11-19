"""Recompute numerical examples and inspect the generated article."""
from pathlib import Path
import re
import numpy as np
from scipy.stats import norm, f, t, gamma, beta, betabinom, invgamma
from scipy.special import expit, betaln, gammaln
ROOT = Path(__file__).resolve().parents[1]
SLUG = Path(__file__).stem

w=np.array([.1,.4,-.3,-.2,.3,.2,.2,.5,-.4])
def evaluate(v,x,y):
    inp=np.r_[1,x];h=expit(v[:6].reshape(2,3)@inp);o=expit(v[6:]@np.r_[1,h])
    d=2*(o-y)*o*(1-o);dh=h*(1-h)*v[7:]*d
    return (y-o)**2,np.r_[(dh[:,None]*inp).ravel(),d*np.r_[1,h]],h,o
E,g,h,o=evaluate(w,[1,0],1)
fd=np.array([(evaluate(w+np.eye(9)[j]*1e-6,[1,0],1)[0]-evaluate(w-np.eye(9)[j]*1e-6,[1,0],1)[0])/2e-6 for j in range(9)])
assert np.max(np.abs(g-fd))<2e-11
assert np.allclose([E,o],[.1808417078785642,.5747451259790616])
assert np.allclose(evaluate(w-.5*g,[1,0],1)[::3],[.14627714050239402,.6175380535237603])
do=2*(.6-1)*.6*(1-.6);dh=.5*.5*1*do
assert np.allclose([do,dh,do*.5,dh*2,-.1*do*.5],[-.192,-.048,-.096,-.096,.0096])
assert np.isclose(4*expit(2)**3,2.7333017973781835)
for z in [-8.,-1.,0.,2.]:
    h=1e-5;fun=lambda z:(1-expit(z))**2
    fd=(fun(z+h)-fun(z-h))/(2*h)
    assert abs(fd-2*(expit(z)-1)*expit(z)*(1-expit(z)))<1e-10
EXPECT=["0.0096","0.00067025","2.7333"]

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
