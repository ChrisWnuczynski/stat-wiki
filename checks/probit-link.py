"""Verify printed probit-link numbers and proof structure."""
from math import erf, exp, pi, sqrt
from pathlib import Path


body = Path("articles/probit-link.qmd").read_text().split("## See also", 1)[0]
for token in ("0.39894", "0.62666", "0.30854", "0.61791", "0.86433",
              "0.30511", "0.625", "0.15866", "0.84134", 'title="Proof"',
              'title="Answer"'):
    assert token in body, token
assert body.count('title="Proof"') == 1
assert 'data-cite-key="nelder_wedderburn1972"' in body
assert 'data-locator="§3.3, pp. 379–380"' in body
Phi = lambda z: (1 + erf(z/sqrt(2)))/2
phi = lambda z: exp(-z*z/2)/sqrt(2*pi)
for z, displayed in [(-.5,.30854),(.3,.61791),(1.1,.86433),(-1,.15866),(1,.84134)]:
    assert round(Phi(z), 5) == displayed
assert round(phi(0),5) == .39894
assert round(sqrt(pi/8),5) == .62666
# Matching the two inverse-link slopes at probability one half scales a
# probit coefficient by this factor on the logit scale.
assert round(4 * phi(0), 3) == 1.596
assert round(.8*phi(.3),5) == .30511
assert round(.5*phi(0),5) == .19947
assert (-(-.5))/.8 == .625
assert round(Phi(0),5) == .5
print("probit-link normal probabilities and structure passed")
