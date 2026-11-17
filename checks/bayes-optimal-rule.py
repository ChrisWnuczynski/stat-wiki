"""Recompute numerical examples and inspect the generated article."""
from pathlib import Path
import re
import numpy as np
from scipy.stats import norm, f, t, gamma, beta, betabinom, invgamma
from scipy.special import expit, betaln, gammaln
ROOT = Path(__file__).resolve().parents[1]
SLUG = Path(__file__).stem

post=np.array([[.2,.55,.25],[.4,.4,.2]]);px=np.array([.6,.4])
assert np.allclose(post.sum(1),1) and np.isclose(px@(1-post.max(1)),.51)
assert np.isclose(px@(1-post[[0,1],[0,2]]),.8)
assert np.isclose(.8-.51,.29)
# Exhaust all deterministic classifiers on the two support points.
risks=[px@(1-post[[0,1],[i,j]]) for i in range(3) for j in range(3)]
assert np.isclose(min(risks),.51) and sum(np.isclose(risks,.51))==2
boundary=1+.5*np.log(7/3)
assert np.isclose(boundary,1.4236489301936017)
assert np.isclose(.7*norm.sf(boundary)+.3*norm.cdf(boundary-2),.13874852997086579)
assert np.allclose([.7*1,.3*5,1/(1+5)],[.7,1.5,1/6])
EXPECT=["0.51","0.80","0.29"]

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
