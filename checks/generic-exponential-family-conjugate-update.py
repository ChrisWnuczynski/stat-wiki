"""Check conjugate coefficient arithmetic, Gamma convention and practice."""

from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / 'articles/generic-exponential-family-conjugate-update.qmd').read_text()
body = page.split('## Related concepts', 1)[0] + page.split('## Related concepts', 1)[-1].split('## See also', 1)[0]

prior_shape, prior_rate = 3, 2
counts = (2, 0, 3, 3)
assert sum(counts) == 8 and len(counts) == 4
post_shape, post_rate = prior_shape + sum(counts), prior_rate + len(counts)
assert (post_shape, post_rate) == (11, 6)
assert round(post_shape / post_rate, 4) == 1.8333
assert sum(counts) / len(counts) == 2
assert prior_shape / prior_rate == 1.5
assert round((2 / 6) * 1.5 + (4 / 6) * 2, 4) == 1.8333
practice = (1, 0, 4)
assert sum(practice) == 5 and len(practice) == 3
assert (2 + sum(practice), 2 + len(practice)) == (7, 5)
assert (prior_shape + sum(practice), prior_rate + len(practice)) == (8, 5)
assert (prior_shape + sum(practice)) / (prior_rate + len(practice)) == 1.6

for printed in ('2,0,3,3', 'S=8', 'Gamma}(11,6)', '11/6=1.8333',
                '8/4=2', '3/2=1.5', '1,0,4', 'S=1+0+4=5',
                '(7,5)', 'Gamma}(8,5)', '8/5=1.6'):
    assert printed in body, f'Missing displayed value: {printed}'
assert body.count('title="Proof"') == 1
assert '## Motivating example' in body and '### Worked example' in body
assert '**Your turn.**' in body and '## Check yourself' in body
assert body.count('title="Answer"') >= 3
for qid in ('ex-applied-exp-rate', 'ex-applied-exp-scale'):
    assert f'../questions/{qid}.qmd' in page
for key in ('diaconis_ylvisaker1979', 'gelman_bda2013', 'dasgupta2011_exponential_family'):
    assert f'data-cite-key="{key}"' in body
print('conjugate update, Gamma convention and practice passed')
