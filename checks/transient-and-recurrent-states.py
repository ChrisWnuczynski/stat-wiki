"""Check Markov return probabilities, expected visits and page structure."""

from math import isclose
from pathlib import Path

root = Path(__file__).resolve().parents[1]
body = (root / 'articles/transient-and-recurrent-states.qmd').read_text().split('## See also', 1)[0]

P = [[.5, .5, 0], [0, 0, 1], [0, 0, 1]]
assert all(isclose(sum(row), 1) for row in P)
assert P[0][0] == .5 and 1 / (1 - P[0][0]) == 2
assert P[1][1] == 0 and P[2][2] == 1
assert 1 / (1 - .75) == 4
assert .7 * 1 + .3 * (1 + 1 / .4) == 1.75
assert 1 / (1 - .5) - 1 == 1  # original example counts later visits
for printed in ('0.5', '0.75', '0.25', '1/(1-0.5)=2', '1/(1-0.75)=4'):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert '## Motivating example' in body and '## Worked example' in body
assert '**Your turn.**' in body and 'title="Answer"' in body
print('Markov recurrence numbers and structure passed')
