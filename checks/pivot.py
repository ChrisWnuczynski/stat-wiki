"""Check numerical pivot intervals, inherited examples and practice."""

from pathlib import Path
from scipy.stats import norm, t

root = Path(__file__).resolve().parents[1]
page = (root / 'articles/pivot.qmd').read_text()
body = page.split('## See also', 1)[0]

q15 = t.ppf(.975, 15)
assert round(q15, 5) == 2.13145
se16 = 2.4 / 16 ** .5
margin16 = q15 * se16
assert se16 == .6 and round(margin16, 5) == 1.27887
assert (round(12.4 - margin16, 3), round(12.4 + margin16, 3)) == (11.121, 13.679)
q8 = t.ppf(.975, 8)
assert round(q8, 5) == 2.30600
se9 = 1.5 / 9 ** .5
margin9 = q8 * se9
assert se9 == .5 and round(margin9, 5) == 1.15300
assert (round(5.2 - margin9, 3), round(5.2 + margin9, 3)) == (4.047, 6.353)

for printed in ('12.4', '2.4', '$15$', '2.13145', '0.6', '1.27887',
                '11.121', '13.679', '5.2', '1.5', '2.30600', '0.5',
                '1.15300', '4.047', '6.353', 'n-1', 'n-2'):
    assert printed in body, f'Missing displayed number: {printed}'
assert body.count('title="Proof"') == 1
assert '## Motivating example' in body and '## Worked example' in body
assert '**Your turn.**' in body and '## Check yourself' in body
assert body.count('title="Answer"') >= 3
assert round(2 * norm.cdf(2) - 1, 4) == .9545
assert round(norm.ppf(.995), 3) == 2.576
assert round(2.776 ** 2, 2) == 7.71
for printed in ('0.9545', '2.576', '2.776', '7.71'):
    assert printed in body
for qid in ('ex-inf-two-standard-errors', 'ex-inf-t-squared-is-f'):
    assert f'../questions/{qid}.qmd' in page
for key in ('siegrist2022_set_estimation', 'siegrist2022_normals',
            'student1908', 'neyman1937'):
    assert f'data-cite-key="{key}"' in body
print('pivot intervals, proof and practice passed')
