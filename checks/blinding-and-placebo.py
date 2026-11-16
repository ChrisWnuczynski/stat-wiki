"""Check blinding examples, including the original caffeine data."""

from pathlib import Path

root = Path(__file__).resolve().parents[1]
body = (root / 'articles/blinding-and-placebo.qmd').read_text().split('## See also', 1)[0]

caf = [17, 22, 21, 16, 6, -2, 27, 15, 16, 20]
decaf = [4, 10, 7, -9, 5, 4, 5, 7, 6, 12]
assert len(caf) == len(decaf) == 10
assert sum(caf) / 10 == 15.8 and sum(decaf) / 10 == 5.1
assert sum(caf) / 10 - sum(decaf) / 10 == 10.700000000000001
assert 80 / 100 == .8 and 60 / 100 == .6
assert round(80 / 100 - 60 / 100, 2) == .2
assert 18 / 30 == .6 and 12 / 30 == .4
assert round(18 / 30 - 12 / 30, 2) == .2
assert 45 / 60 == .75 and 30 / 60 == .5
assert 45 / 60 - 30 / 60 == .25
for printed in ('250 mL', '15.8', '5.1', '10.7', '0.80', '0.60', '0.20', '18/30', '12/30'):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert '## Motivating example' in body and '## Worked example' in body
assert '**Your turn.**' in body and 'title="Answer"' in body
print('blinding design numbers and structure passed')
