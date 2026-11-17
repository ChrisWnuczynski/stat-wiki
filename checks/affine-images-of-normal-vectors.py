"""Recompute numerical examples and inspect the generated article."""
from pathlib import Path
import re
import numpy as np
from scipy.stats import norm, f, t, gamma, beta, betabinom, invgamma
from scipy.special import expit, betaln, gammaln
ROOT = Path(__file__).resolve().parents[1]
SLUG = Path(__file__).stem

mu=np.array([1.,2]);S=np.array([[4.,1],[1,9]]);A=np.array([[1,1],[2,-1]])
assert np.allclose(A@mu+[-1,3],[2,3]) and np.allclose(A@S@A.T,np.diag([15,21]))
assert np.isclose(np.array([2,-1])@np.diag([15,21])@np.array([2,-1]),81)
assert np.linalg.matrix_rank([[1,2],[2,4]])==1
assert np.isclose(norm.cdf(.1/np.sqrt(.05)),.6726395769907115)
assert np.isclose(norm.cdf(1)-norm.cdf(-5/3),.7935543937957282)
assert np.isclose(norm.cdf(5)-norm.cdf(-25/3),.9999997133484281)
# Independent Gaussian partial sums: covariance is min(m,n).
L=np.tril(np.ones((5,5)));assert np.allclose(L@L.T,np.minimum.outer(np.arange(1,6),np.arange(1,6)))
# Self-check transformations use the question's displayed CDF approximations.
assert np.isclose(norm.cdf((3-1)/2),.8413447460685429)
assert np.isclose(norm.cdf(.5)-norm.cdf(-1),.532807207342556)
assert np.isclose(.6915-(1-.8413),.5328)
assert np.isclose(.674-(1-.560),.234)
EXPECT=["0.67264","0.79355","0.9999997133"]

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
