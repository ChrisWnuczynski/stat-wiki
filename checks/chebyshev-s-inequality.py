"""Verify Chebyshev arithmetic, equality example and generated page."""

from math import isclose
from pathlib import Path

from scipy.stats import norm

root = Path(__file__).resolve().parents[1]
body = (root / 'articles/chebyshev-s-inequality.qmd').read_text().split('## See also', 1)[0]

assert 10**2 / 25**2 == .16
assert 1 / 2**2 == .25
xs, ps = [-2, 0, 2], [1/8, 3/4, 1/8]
assert sum(x*p for x,p in zip(xs,ps)) == 0
assert sum(x*x*p for x,p in zip(xs,ps)) == 1
assert ps[0] + ps[2] == .25
assert 16 / 64 == .25 and 16 / 100 == .16
assert 1 - .16 == .84 and 1 - .25 == .75
assert round(2 * norm.sf(2), 4) == .0455
assert 25 / 500 == .05
for printed in ('500', '0.16', '0.25', '0.84', '0.0455', '1/8', '3/4'):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert '## Motivating example' in body and '## Worked example' in body
assert '**Your turn.**' in body and 'title="Answer"' in body
print('Chebyshev calculations and structure passed')
