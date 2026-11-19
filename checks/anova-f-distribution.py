"""Recompute numerical examples and inspect the generated article."""
from pathlib import Path
import re
import numpy as np
from scipy.stats import norm, f, t, gamma, beta, betabinom, invgamma
from scipy.special import expit, betaln, gammaln
ROOT = Path(__file__).resolve().parents[1]
SLUG = Path(__file__).stem

Y=np.array([[1.,2,3],[2,3,4],[5,6,7]])
ssb=3*np.sum((Y.mean(1)-Y.mean())**2);sse=np.sum((Y-Y.mean(1)[:,None])**2)
assert np.allclose([ssb,sse,ssb+sse,ssb/2/(sse/6)],[26,6,32,13])
assert np.isclose(f.sf(13,2,6),.006591796875)
# Verify orthogonal projection ranks and exact SS identity.
PG=np.kron(np.eye(3),np.ones((3,3))/3);P1=np.ones((9,9))/9;B=PG-P1;R=np.eye(9)-PG
assert np.allclose(B@R,0) and np.linalg.matrix_rank(B)==2 and np.linalg.matrix_rank(R)==6
assert np.allclose([Y.ravel()@B@Y.ravel(),Y.ravel()@R@Y.ravel()],[26,6])
corn=np.array([[46.2,51.9,48.7],[49.2,58.6,57.4],[60.3,58.7,60.4],[48.9,51.4,44.6],[52.5,54,49.3]])
cB=3*np.sum((corn.mean(1)-corn.mean())**2);cE=np.sum((corn-corn.mean(1)[:,None])**2)
assert abs(cB-270.269333333333)<1e-9 and abs(cE-105.68)<1e-9
assert abs(cB/4/(cE/10)-6.393)<.002
# Two-group and paired-test identities used by the self-checks.
g1=np.array([1.,2,3]);g2=np.array([2.,3,4]);pool=(np.sum((g1-g1.mean())**2)+np.sum((g2-g2.mean())**2))/4
T=(g1.mean()-g2.mean())/np.sqrt(pool*(1/3+1/3))
assert np.isclose(T*T,1.5)
assert np.isclose(f.ppf(.95,1,4),t.ppf(.975,4)**2)
EXPECT=["0.0065918","26","N-k"]

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
