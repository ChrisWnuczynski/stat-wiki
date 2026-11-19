"""Recompute numerical examples and inspect the generated article."""
from pathlib import Path
import re
import numpy as np
from scipy.stats import norm, f, t, gamma, beta, betabinom, invgamma
from scipy.special import expit, betaln, gammaln
ROOT = Path(__file__).resolve().parents[1]
SLUG = Path(__file__).stem

eta=.5;ws=[0.]
for k in range(3):ws.append(ws[-1]-eta*(ws[-1]-3))
assert np.allclose(ws,[0,1.5,2.25,2.625])
assert np.allclose(.5*(np.array(ws)-3)**2,[4.5,1.125,.28125,.0703125])
assert np.allclose(1-.1*np.array([1,10]),[.9,0]) and np.allclose(1-.25*np.array([1,10]),[.75,-1.5])
assert np.isclose(2*(expit(-8)-1)*expit(-8)*(1-expit(-8)),-.0006702504975197)
assert np.isclose(2*(expit(-1)-1)*expit(-1)*(1-expit(-1)),-.28746968091443)
# Exact sigmoid symmetry needs the downstream bias adjustment.
for u in [-8.,-1.,0.,2.,9.]:
    h=expit(u);w,b=1.3,-.4
    assert np.isclose(expit(-u),1-h)
    assert np.isclose(-w*expit(-u)+(b+w),w*h+b)
assert np.allclose([expit(-8),expit(-1),expit(-8)-1,expit(-1)-1],[.0003353501304664781,.2689414213699951,-.9996646498695335,-.7310585786300049])
EXPECT=["0.0703125","-1.5","0.00067025"]

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
