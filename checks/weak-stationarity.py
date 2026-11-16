"""Check stationary AR examples and the weak-not-strict construction."""

import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
body = (root / 'articles/weak-stationarity.qmd').read_text().split('## See also', 1)[0]

phi, sig2 = .6, 4
g0 = sig2 / (1 - phi**2)
assert g0 == 6.25 and phi * g0 == 3.75
assert phi**2 * g0 == 2.25 and round(phi**2, 2) == .36
assert 2 * (g0 - phi * g0) == 5
phi2 = -.5
g02 = 3 / (1 - phi2**2)
assert g02 == 4 and phi2 * g02 == -2 and phi2**2 * g02 == 1
assert phi2**2 == .25
assert .25 * 2 + .25 * 2 == 1  # odd-time three-point variance
assert math.isclose((math.sqrt(3))**2 / 3, 1)  # uniform bank example
assert round(9 / (1 - .4**2), 4) == 10.7143
assert round(.4 * 9 / (1 - .4**2), 4) == 4.2857
for printed in ('6.25', '3.75', '2.25', '0.36', '-0.5', '-2', '0.25', '4t'):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert '## Motivating example' in body and '## Worked example' in body
assert '**Your turn.**' in body and 'title="Answer"' in body
print('weak-stationarity numbers and structure passed')
