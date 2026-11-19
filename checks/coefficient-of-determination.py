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
sst=np.sum((y-y.mean())**2);ssr=np.sum((X@bh-y.mean())**2)
assert np.allclose([sst,sse,ssr],[6,4.4,1.6]) and np.isclose(1-sse/sst,4/15)
assert np.isclose(np.corrcoef(x,y)[0,1]**2,4/15) and np.isclose(1-(y@y)/sst,-10/3)
# Adding a predictor cannot increase the residual norm.
X2=np.c_[X,x*x];fit2=np.linalg.lstsq(X2,y,rcond=None)[0]
assert np.sum((y-X2@fit2)**2)<=sse+1e-12
advert=23.34**2/(.444*1600.9);assert abs(advert-.766)<.001
assert abs(np.sqrt(1600.9*(1-advert)/8)-6.84)<.01
# The printed height-output summaries must agree to their displayed precision.
T=1.0048/.2178
assert abs(T-4.613)<.001 and abs(T*T-21.28)<.01
assert abs(T*T/(T*T+98)-.1784)<.0001
assert abs(2*t.sf(T,98)-1.2e-5)<2e-7
EXPECT=["0.266667","4.4","-10/3"]

source = (ROOT / "research" / "content" / (SLUG + ".md")).read_text()
article = (ROOT / "articles" / (SLUG + ".qmd")).read_text().split("## See also", 1)[0]
assert "Motivating example" in article and "Your turn" in article
assert "## Check yourself {#check-yourself}" in article
citations = list(re.finditer(r'<sup[^>]*class="cite-ref"[^>]*>.*?</sup>', article))
assert len(citations) >= 5
assert len(set(re.findall(r'data-cite-key="([^"]+)"', article))) >= 2
for mark in citations:
    assert re.search(r'data-locator="[^"]+"', mark.group(0)), mark.group(0)[:220]
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
