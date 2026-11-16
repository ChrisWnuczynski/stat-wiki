"""Check odds identities and every numerical example added to prior odds."""

from math import isclose
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
page = (ROOT / "articles/prior-odds.qmd").read_text()
content = (ROOT / "research/content/prior-odds.md").read_text()

def near(a, b):
    assert isclose(a, b, abs_tol=1e-12), (a,b)

prior = .1
prior_odds = prior/(1-prior)
near(prior_odds, 1/9)
bf = .8/.1
near(bf, 8)
post_odds = prior_odds * bf
near(post_odds, 8/9)
near(post_odds/(1+post_odds), 8/17)
assert isclose(8/17, .471, abs_tol=.0005)
near((.25/.75)*(.6/.2), 1)
near(1/(1+1), .5)
near((.1/.9)*(.8/.4), 2/9)
near((2/9)/(1+2/9), 2/11)
near((.25/.75)*6, 2)
near(2/(1+2), 2/3)
near(4*(1/9), 4/9)
near((4/9)/(1+4/9), 4/13)
for p, factor in ((.1,2),(.25,6),(.6,.4)):
    odds = p/(1-p)
    updated = factor*odds
    direct = factor*p/(factor*p+1-p)
    near(updated/(1+updated), direct)
assert '::: {.callout-note collapse="true" title="Proof"}' in page
assert '::: {.callout-tip collapse="true" title="Answer"}' in page
assert '## Worked example {#worked-example}' in page
assert '{#assumptions-and-limits}' in page
assert 'Lead context' not in content
print("prior odds numbers, identities and structure passed")
