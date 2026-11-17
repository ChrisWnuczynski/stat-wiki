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
g2=evaluate(w,[0,1],0)[1];batch=g+g2
assert np.allclose(batch,[.00954901,-.02442579,.03397480,-.00671685,.02073570,-.02745255,.06664968,-.00581219,.02813227],atol=1e-8)
assert np.allclose(w[6:]-.5*batch[6:],[.16667516,.50290610,-.41406614],atol=1e-8)
assert np.allclose(w-.5*batch,w-1*(batch/2))
assert np.isclose(4*expit(2)**2*(1-expit(2)),.369912172919)
# Central differences of the complete two-pattern batch loss.
def batchloss(v):
    return evaluate(v,[1,0],1)[0]+evaluate(v,[0,1],0)[0]
fd_batch=np.array([(batchloss(w+np.eye(9)[j]*1e-6)-batchloss(w-np.eye(9)[j]*1e-6))/2e-6 for j in range(9)])
assert np.max(np.abs(fd_batch-batch))<1e-10
# The scalar self-check's separate finite-difference step.
fd_single=(expit(2*1.001)**2-expit(2*.999)**2)/.002
assert abs(fd_single-4*expit(2)**2*(1-expit(2)))<2e-7
EXPECT=["0.166675","0.502906","0.009549"]

source = (ROOT / "research" / "content" / (SLUG + ".md")).read_text()
article = (ROOT / "articles" / (SLUG + ".qmd")).read_text().split("## See also", 1)[0]
assert "Motivating example" in article and "Your turn" in article
assert "## Check yourself {#check-yourself}" in article
citations = list(re.finditer(r'<sup[^>]*class="cite-ref"[^>]*>.*?</sup>', article))
assert len(citations) >= 5
assert len(set(re.findall(r'data-cite-key="([^"]+)"', article))) >= 2
for mark in citations:
    assert re.match(r"^\s*\((?:ch\.|Chs\.|§|Thm\.|Lem\.|Lems\.|p\.|pp\.|Glossary|Ex\.|Summary|Def\.|Sec\.|Props\.|Introduction|Description|Format|Source|References|Examples|Notes|Basic Theory)", article[mark.end():mark.end()+60], re.I), article[mark.end():mark.end()+100]
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
