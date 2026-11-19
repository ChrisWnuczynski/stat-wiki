"""Recompute numerical examples and inspect the generated article."""
from pathlib import Path
import re
import numpy as np
from scipy.stats import norm, f, t, gamma, beta, betabinom, invgamma
from scipy.special import expit, betaln, gammaln
ROOT = Path(__file__).resolve().parents[1]
SLUG = Path(__file__).stem

q=np.array([.9,.2,.6]);y=np.array([1,0,1]);assert np.isclose(np.mean((q-y)**2),.07)
p=np.array([.2,.8]);q=np.array([.3,.7]);assert np.isclose(np.mean(p*(1-q)**2+(1-p)*q*q),.17)
assert np.allclose([np.mean(p*(1-p)),np.mean((p-q)**2),np.var(p)],[.16,.01,.09])
for p in [.01,.2,.5,.8,.99]:
 for q in np.linspace(0,1,31):assert np.isclose(p*(1-q)**2+(1-p)*q*q,p*(1-p)+(q-p)**2)
assert np.allclose(np.exp([.4618,.2484,.6851]),[1.58692789,1.28197262,1.98397022])
assert np.allclose(expit(-3.70568+.04618*np.array([60,70])),[.28193572,.38388751])
EXPECT=["0.17","0.07","0.101952"]

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
