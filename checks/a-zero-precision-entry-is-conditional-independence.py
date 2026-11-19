"""Recompute numerical examples and inspect the generated article."""
from pathlib import Path
import re
import numpy as np
from scipy.stats import norm, f, t, gamma, beta, betabinom, invgamma
from scipy.special import expit, betaln, gammaln
ROOT = Path(__file__).resolve().parents[1]
SLUG = Path(__file__).stem

K=np.array([[2.,-1,0],[-1,2,-1],[0,-1,2]]);S=np.linalg.inv(K)
assert np.allclose(S,[[.75,.5,.25],[.5,1,.5],[.25,.5,.75]])
assert min(np.linalg.eigvalsh(K))>0 and np.allclose(K@S,np.eye(3))
conditional=S[np.ix_([0,2],[0,2])]-np.outer(S[[0,2],1],S[1,[0,2]])/S[1,1]
assert np.allclose(conditional,.5*np.eye(2)) and np.isclose(S[0,2]/np.sqrt(S[0,0]*S[2,2]),1/3)
assert np.allclose(-K[[0,1],[1,2]]/np.sqrt(K[[0,1],[0,1]]*K[[1,2],[1,2]]),.5)
oldS=np.array([[1,.5,0],[.5,1,0],[0,0,1]])
assert np.allclose(np.linalg.inv(oldS),[[4/3,-2/3,0],[-2/3,4/3,0],[0,0,1]])
Q=np.array([[2.,-1,0],[-1,3,-1],[0,-1,2]])
assert np.allclose(np.linalg.inv(Q),np.array([[5,2,1],[2,4,2],[1,2,5]])/8)
EXPECT=["1/3","1/2","conditional covariance"]

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
