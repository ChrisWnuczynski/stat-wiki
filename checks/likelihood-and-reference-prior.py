"""Check the regression reference-prior posterior examples."""

from math import isclose, sqrt
from pathlib import Path

root = Path(__file__).resolve().parents[1]
body = (root / 'articles/likelihood-and-reference-prior.qmd').read_text().split('## See also', 1)[0]

y = [2, 4, 3, 5]
mean = sum(y) / len(y)
sse = sum((v - mean) ** 2 for v in y)
assert mean == 3.5 and sse == 5
assert [v - mean for v in y] == [-1.5, .5, -.5, 1.5]
assert len(y) - 1 == 3
assert isclose(sqrt((sse / 3) / 4), sqrt(5 / 12))
assert round(sqrt(5 / 12), 4) == .6455
assert 3 / (3 - 2) * 5 / 12 == 1.25
y2 = [1, 2, 3]
assert sum(y2) / len(y2) == 2
assert sum((v - 2) ** 2 for v in y2) == 2
assert (len(y2) - 1) / 2 == 1 and 2 / 2 == 1
for printed in ('3.5', '-1.5', '0.5', '1.5', 's=5', '0.6455', '1.25', 's=2', 'n=3', 'p=1'):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert '## Motivating example' in body and '## Worked example' in body
assert '**Your turn.**' in body and 'title="Answer"' in body
print('reference-prior examples and structure passed')
