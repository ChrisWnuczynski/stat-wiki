"""Verify Bernoulli sufficiency, posterior arithmetic and bank answers."""

import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / 'articles/sufficient-statistic.qmd').read_text()
body = page.split('## See also', 1)[0]

sample = (1, 0, 1, 1, 0)
s = sum(sample)
assert s == 3 and len(sample) == 5
assert math.comb(5, 3) == 10 and 1 / math.comb(5, 3) == .1
assert (2 + s, 2 + 5 - s) == (5, 4)
assert round(5 / 9, 4) == .5556
practice = (1, 0, 0, 1)
assert sum(practice) == 2 and math.comb(4, 2) == 6
assert round(1 / 6, 4) == .1667
assert (2 + sum(practice), 2 + 4 - sum(practice)) == (4, 4)
assert 4 / 8 == .5
assert 5 * 81 == 405 and 4 ** 5 == 1024
assert round(405 / 1024, 4) == .3955
assert round(math.exp(-5 / 4) * 5 / 4, 4) == .3581

for printed in ('(1,0,1,1,0)', 'S=3', '1/10=0.1', '5/9=0.5556',
                '(1,0,0,1)', 'S=2', '1/6=0.1667', '4/8=0.5',
                '405}{1024}', '0.3955', '0.3581'):
    assert printed in body, f'Missing printed value: {printed}'
assert body.count('title="Proof"') == 1
assert '## Motivating example' in body and '## Worked example' in body
assert '**Your turn.**' in body and '## Check yourself' in body
assert body.count('title="Answer"') >= 3
for qid in ('ex-inf-poisson-umvu', 'ex-inf-rao-blackwell-variance'):
    assert f'../questions/{qid}.qmd' in page
for key in ('fisher1922', 'dasgupta2011_exponential_family', 'brown1964_sufficiency', 'dasgupta2007_basu'):
    assert f'data-cite-key="{key}"' in body
print('sufficiency, Bernoulli and Poisson arithmetic and practice passed')
