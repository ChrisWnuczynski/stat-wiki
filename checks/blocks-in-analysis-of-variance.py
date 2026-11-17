"""Recompute numerical examples and inspect the generated article."""
from pathlib import Path
import re
import numpy as np
from scipy.stats import norm, f, t, gamma, beta, betabinom, invgamma
from scipy.special import expit, betaln, gammaln
ROOT = Path(__file__).resolve().parents[1]
SLUG = Path(__file__).stem

Y=np.array([[9.3,9.4,9.2,9.7],[9.4,9.3,9.4,9.6],[9.6,9.8,9.5,10],[10,9.9,9.7,10.2]])
def sums(Z):
    gm=Z.mean();ssb=4*np.sum((Z.mean(1)-gm)**2);sst=4*np.sum((Z.mean(0)-gm)**2)
    sse=np.sum((Z-Z.mean(1)[:,None]-Z.mean(0)+gm)**2)
    return np.array([ssb,sst,sse])
ssb,sst,sse=sums(Y)
assert np.allclose([ssb,sst,sse],[.825,.385,.08])
assert np.isclose(sst/3/(sse/9),14.4375) and np.isclose(f.sf(14.4375,3,9),.0008712720711116723)
assert np.isclose(sst/3/((ssb+sse)/12),1.701657458563536)
contrast=Y.mean(0)[3]-Y.mean(0)[2];se=np.sqrt(2*(sse/9)/4)
assert np.isclose(contrast,.425) and np.isclose(se,1/15)
assert np.allclose(contrast+np.array([-1,1])*t.ppf(.975,9)*se,[.27418952,.57581048])
shift=Y.copy();shift[-1]+=5;assert np.allclose(sums(shift)[1:],sums(Y)[1:])
d=np.array([.4,.4,.5,.6,.5]);T=d.mean()/(d.std(ddof=1)/np.sqrt(5))
assert np.isclose(T*T,164.5714285714286)
EXPECT=["14.4375","0.27419","0.57581"]

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
