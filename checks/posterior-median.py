"""Check the posterior-median examples and numerical claims."""

import math
from pathlib import Path

from scipy.stats import beta

root = Path(__file__).resolve().parents[1]
body = (root / 'articles/posterior-median.qmd').read_text().split('## See also', 1)[0]

m = beta.ppf(.5, 3, 9)
assert round(m, 4) == .2358
assert 3 / 12 == .25 and (3 - 1) / (3 + 9 - 2) == .2
lo, hi = beta.ppf([.025, .975], 3, 9)
assert round(lo, 4) == .0602 and round(hi, 4) == .5178
assert round((lo + hi) / 2, 4) == .2890
assert .2 * 0 + .3 * 1 + .5 * 4 == 2.3
for a in (1, 2, 4):
    assert math.isclose(.2 * abs(a) + .3 * abs(a - 1) + .5 * abs(a - 4), 1.7)
assert .25 / (1 - .25) == 1 / 3
assert .5 * (2 - 1)**2 + .5 * (2 - 5)**2 == 5
for printed in ('0.2358', '0.0602', '0.5178', '0.2890', '2.3', '1.7', '0.25', '0.20'):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert '## Motivating example' in body and '## Worked example' in body
assert '**Your turn.**' in body and 'title="Answer"' in body
print('posterior-median numerical examples and structure passed')
