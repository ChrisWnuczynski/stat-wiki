"""Check the treatment article's new numerical comparisons and proof."""

from pathlib import Path

root = Path(__file__).resolve().parents[1]
body = (root / 'articles/treatment.qmd').read_text().split('## See also', 1)[0]

assert len([1 for x in range(12)]) == 12
assert len([1 for x in range(6)]) == 6
tr = [12, 11, 15, 14, 10, 13]
co = [9, 8, 11, 10, 7, 9]
assert sum(tr) == 75 and sum(co) == 54
assert sum(tr)/6 == 12.5 and sum(co)/6 == 9
assert sum(tr)/6 - sum(co)/6 == 3.5
tr = [8, 9, 7, 10]
co = [6, 7, 5, 8]
assert sum(tr) == 34 and sum(co) == 26
assert sum(tr)/4 == 8.5 and sum(co)/4 == 6.5
assert sum(tr)/4 - sum(co)/4 == 2
for printed in ('12.5', '3.5', '8.5', '6.5', '34/4', '26/4'):
    assert printed in body, printed
assert body.count('![') == 0
assert body.count('title="Proof"') == 1
assert '## Motivating example' in body and '## Worked example' in body
assert '**Your turn.**' in body and 'title="Answer"' in body
for key in ('hernan_robins2020', 'dodge2008'):
    assert f'data-cite-key="{key}"' in body
print('treatment arithmetic and practice passed')
