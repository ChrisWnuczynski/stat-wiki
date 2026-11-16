"""Verify mixture moments, membership, parameter count and page practice."""

import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / 'articles/finite-mixture-model.qmd').read_text()
body = page.split('## See also', 1)[0]

weights = (.3, .7)
means = (0, 4)
variances = (1, 1)
mu = sum(w * m for w, m in zip(weights, means))
within = sum(w * v for w, v in zip(weights, variances))
between_terms = [w * (m - mu) ** 2 for w, m in zip(weights, means)]
assert mu == 2.8
assert within == 1 and [round(v, 3) for v in between_terms] == [2.352, 1.008]
assert round(within + sum(between_terms), 2) == 4.36
assert round(math.sqrt(4.36), 4) == 2.0881


def posterior_first(x):
    a = .3 * math.exp(-x * x / 2)
    b = .7 * math.exp(-(x - 4) ** 2 / 2)
    return a / (a + b)


assert round(posterior_first(1), 4) == .9590
assert round(1 - posterior_first(1), 4) == .0410
assert round(posterior_first(3), 6) == .007788
assert round(1 - posterior_first(3), 6) == .992212
assert 3 * 2 + 3 * 2 * 3 // 2 + 2 == 17
# The first bank question has a second-component variance of 4.
assert round(.3 * 1 + .7 * 4 + sum(between_terms), 2) == 6.46
assert round(.3 * 1 + .7 * 4, 1) == 3.1

for printed in ('2.8', '4.36', '2.352', '1.008', '2.0881',
                '0.9590', '0.0410', '0.007788', '0.992212',
                '6+9+2=17', '6.46'):
    assert printed in body, f'Missing displayed number: {printed}'
assert body.count('title="Proof"') == 1
assert '## Motivating example' in body and '## Worked example' in body
assert '**Your turn.**' in body and '## Check yourself' in body
assert body.count('title="Answer"') >= 3
for qid in ('ex-sl-05-1', 'ex-sl-05-4'):
    assert f'../questions/{qid}.qmd' in page
for key in ('mclachlan_peel2000_book', 'sklearn_mixture2026',
            'pearson1894_mixture', 'dempster_laird_rubin1977'):
    assert f'data-cite-key="{key}"' in body
print('mixture moments, membership, proof and practice passed')
