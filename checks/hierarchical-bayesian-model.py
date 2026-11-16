"""Verify hierarchical shrinkage numbers, original examples and figures."""

import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
body = (root / 'articles/hierarchical-bayesian-model.qmd').read_text().split('## See also', 1)[0]

def normal_update(mu, sig2, tau2, n, ybar):
    w = n * tau2 / (sig2 + n * tau2)
    return w, w * ybar + (1 - w) * mu, sig2 * tau2 / (sig2 + n * tau2)

w_a, mean_a, var_a = normal_update(70, 100, 25, 100, 75)
w_b, mean_b, var_b = normal_update(70, 100, 25, 2, 95)
assert math.isclose(w_a, 25 / 26) and math.isclose(w_b, 1 / 3)
assert round(w_a, 4) == .9615 and round(mean_a, 2) == 74.81
assert round(mean_b, 2) == 78.33 and round(mean_b - mean_a, 2) == 3.53
assert 95 - 75 == 20 and var_a < var_b
assert normal_update(50, 100, 25, 4, 60) == (.5, 55, 12.5)
assert normal_update(50, 100, 25, 16, 60) == (.8, 58, 5)
assert normal_update(40, 36, 9, 4, 55) == (.5, 47.5, 4.5)
assert (2 + 4) / (2 + 8 + 10) == .3
assert round((2 + 40) / (2 + 8 + 100), 4) == .3818
assert 2 / 10 == .2 and 4 / 10 == .4 and 40 / 100 == .4
assert math.isclose(1 / 3 - (.5)**2, 1 / 12)
for printed in ('74.81', '78.33', '3.53', '0.9615', '12.5', '0.3818', '14', '19'):
    assert printed in body, printed
assert body.count('![') == 2
assert body.count('title="Proof"') == 1
assert '## Motivating example' in body and '## Worked example' in body
assert '**Your turn.**' in body and 'title="Answer"' in body
print('hierarchical model numbers, figures and structure passed')
