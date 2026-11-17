"""Recompute numerical examples and inspect the generated article."""
from pathlib import Path
import re
import numpy as np
from scipy.stats import norm, f, t, gamma, beta, betabinom, invgamma
from scipy.special import expit, betaln, gammaln
ROOT = Path(__file__).resolve().parents[1]
SLUG = Path(__file__).stem

a,b,m=10,4,5;k=np.arange(m+1)
pm=np.exp(gammaln(m+1)-gammaln(k+1)-gammaln(m-k+1)+betaln(a+k,b+m-k)-betaln(a,b))
assert np.allclose(pm,betabinom.pmf(k,m,a,b)) and np.isclose(pm.sum(),1)
assert np.isclose(pm[4:].sum(),.5674603174603177)
mean=k@pm;var=((k-mean)**2)@pm
assert np.allclose([mean,var],[25/7,190/147]) and np.isclose(m*(a/(a+b))*(b/(a+b)),50/49)
assert np.isclose((190/147)/(50/49),19/15)
assert np.isclose(a*(a+1)/((a+b)*(a+b+1)),11/21)
assert np.isclose(11/21-(5/7)**2,2/147)
assert np.isclose(190/147-50/49,5*(5-1)*2/147)
assert np.isclose(25*2/147,50/147) and np.isclose(5*2/147,10/147)
EXPECT=["0.5674603","1.292517","1/15"]

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
