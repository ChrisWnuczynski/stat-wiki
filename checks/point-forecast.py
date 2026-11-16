"""Check the point-forecast arithmetic and generated page structure."""

from math import isclose
from pathlib import Path

root = Path(__file__).resolve().parents[1]
body = (root / "articles/point-forecast.qmd").read_text().split("## See also", 1)[0]

phi, sig2, last = 0.5, 4, 10
assert [phi**h * last for h in (1, 2, 3, 4)] == [5, 2.5, 1.25, 0.625]
assert [sig2 * sum(phi ** (2 * j) for j in range(h)) for h in (1, 2, 3, 4)] == [4, 5, 5.25, 5.3125]
assert isclose(sig2 / (1 - phi**2), 16 / 3)
assert (5 - 1.96 * 2, 5 + 1.96 * 2) == (1.08, 8.92)
assert 20 + .6 * 10 == 26 and 20 + .6**2 * 10 == 23.6
assert isclose(9 * (1 + .6**2), 12.24)
assert .8 * 10 + .2 * 30 == 14
for printed in ('5.3333', '5.3125', '0.625', '1.08', '8.92', '16/3', '5.25', '2.5', '1.25'):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert '## Motivating example' in body and '## Worked example' in body
assert '**Your turn.**' in body and 'title="Answer"' in body
print('point-forecast arithmetic and structure passed')
