"""Check numerical MGF examples and the generated article structure."""

import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
body = (root / 'articles/moment-generating-function.qmd').read_text().split('## See also', 1)[0]

p, n = .3, 4
assert n * p == 1.2
assert math.isclose(n * p * (1 - p), .84)
assert round((1 - p) ** n, 4) == .2401
lam = 2
assert lam + lam**2 == 6
assert round(math.exp(2), 4) == 7.3891
assert math.isclose(2 * .4 * .6, .48) and math.isclose(.4**2, .16)
assert 3 / (3 - 2) == 3 and 3 / (3 - 4) == -3
assert 1 / 3 > 0 and math.isclose(1 / 9, (1 / 3)**2)
for printed in ('0.3', '0.7', '1.2', '0.84', '0.2401', '7.3891', '6-2^2=2'):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert '## Motivating example' in body and '## Worked example' in body
assert '**Your turn.**' in body and 'title="Answer"' in body
print('MGF numerical examples and structure passed')
