"""Check printed improper-prior examples and their propriety criteria."""

from math import isclose, sqrt
from pathlib import Path
from scipy.integrate import quad
from scipy.stats import beta, norm

page = (Path(__file__).resolve().parents[1] / 'articles/improper-prior.qmd').read_text()
body = page.split('## See also', 1)[0]

assert isclose(quad(lambda mu: norm.pdf(mu, 3, sqrt(3)), -100, 100)[0], 1)
assert (1 + 3 + 5) / 3 == 3
assert 9 / 3 == 3
assert beta.mean(3, 1) == .75
assert isclose(quad(lambda t: 3*t*t, 0, 1)[0], 1)
assert beta.mean(2, 3) == .4
assert (2, 3) == (2, 5-2)
assert quad(lambda t: (1-t)**4 / t, 1e-6, .5)[0] > 10
assert quad(lambda t: t**3 / (1-t), 0, 1-1e-6)[0] > 10
for printed in ('0.75', '3/(3+1)', 'N(3,3)', '9/3', '3\\theta^2', 'Beta}(4,0)', 'n=3'):
    assert printed in body, f'Missing printed value {printed}'
assert body.count('title="Proof"') == 1
assert '**Your turn.**' in body and 'title="Answer"' in body
for key in ('gelman_bda2013', 'taraldsen2022_improper'):
    assert f'data-cite-key="{key}"' in body
print('Improper prior numerical and propriety checks passed')
