"""Check the underdispersion examples and Poisson comparisons."""

import math
from pathlib import Path

from scipy.stats import poisson

root = Path(__file__).resolve().parents[1]
body = (root / 'articles/underdispersion.qmd').read_text().split('## See also', 1)[0]

counts = [1, 3] + [2] * 8
n = len(counts)
mu = sum(counts) / n
sse = sum((v - mu) ** 2 for v in counts)
assert n == 10 and mu == 2 and sse == 2
assert math.isclose(sse / (n - 1), 2 / 9)
assert round(2 / 9, 4) == .2222
assert math.isclose((sse / (n - 1)) / mu, 1 / 9)
assert sse / mu == 1
assert round(poisson.cdf(13, 7) - poisson.cdf(2, 7), 4) == .9576
assert 4 * .5 == 2 and 4 * .5 * .5 == 1
assert 5 * .4 == 2 and math.isclose(5 * .4 * .6, 1.2)
pooled = [1] * 5 + [5] * 5
assert sum(pooled) / 10 == 3
assert sum((x - 3) ** 2 for x in pooled) == 40
assert round(40 / 9, 3) == 4.444
for printed in ('0.2222', '0.1111', '1/9', '0.5', '2/9'):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert '## Motivating example' in body and '## Worked example' in body
assert '**Your turn.**' in body and 'title="Answer"' in body
print('underdispersion numeric examples and structure passed')
