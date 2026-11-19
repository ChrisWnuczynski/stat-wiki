"""Recompute numerical examples and inspect the generated article."""
from pathlib import Path
import re
import numpy as np
from scipy.stats import norm, f, t, gamma, beta, betabinom, invgamma
from scipy.special import expit, betaln, gammaln
ROOT = Path(__file__).resolve().parents[1]
SLUG = Path(__file__).stem

assert np.isclose(.368*.1+.632*.25,.1948)
omit=(1-1/10)**10;assert np.allclose([10*(1-omit),omit,200*omit],[6.513215599,.3486784401,69.73568802])
assert np.allclose([1-.8**5,1-.95**20],[.67232,.6415140775914581])
assert np.isclose(.368*.05+.632*.2,.1448) and np.isclose(.632*.5,.316)
# Casewise weighting is not generally pooled-loss weighting.
losses=[[0,1],[1,1,1,0]];case=np.mean([np.mean(a) for a in losses]);pooled=np.mean(sum(losses,[]))
assert np.isclose(case,.625) and np.isclose(pooled,2/3)
EXPECT=["0.1948","6.51322","0.316"]

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
