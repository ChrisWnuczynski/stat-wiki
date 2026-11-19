"""Recompute numerical examples and inspect the generated article."""
from pathlib import Path
import re
import numpy as np
from scipy.stats import norm, f, t, gamma, beta, betabinom, invgamma
from scipy.special import expit, betaln, gammaln
ROOT = Path(__file__).resolve().parents[1]
SLUG = Path(__file__).stem

q=gamma.sf(10,189,scale=1/21)
assert np.isclose(q,.0670161919454404)
assert np.allclose([20*q,1-q,1/21],[1.340323838908808,.9329838080545596,.047619047619047616])
assert q<1-q and 20*q>1-q and 10*q<1-q
assert np.allclose(gamma.ppf([.025,.975],189,scale=1/21),[7.76258272,10.32758794])
assert np.isclose(.3*5,1.5) and np.isclose(1/(5+1),1/6)
boundary=1+.5*np.log(7/3);assert np.isclose(.7*norm.sf(boundary)+.3*norm.cdf(boundary-2),.13874852997086579)
# The comparison prior with one higher shape preserves all legacy numerical summaries.
assert np.isclose(gamma.cdf(10,190,scale=1/21),.92320087)
assert np.allclose(gamma.ppf([.025,.975],190,scale=1/21),[7.81,10.38],atol=.005)
EXPECT=["1.34032384","0.93298381","0.67016192"]

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
