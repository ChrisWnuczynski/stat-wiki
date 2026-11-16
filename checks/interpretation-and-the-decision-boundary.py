"""Check rank-163 logistic decision arithmetic and preserved links."""
from pathlib import Path
import json
import math

root = Path(__file__).resolve().parents[1]
page = (root / 'articles/interpretation-and-the-decision-boundary.qmd').read_text()
body = page.split('## See also')[0]
sigmoid = lambda x: 1 / (1 + math.exp(-x))

assert -2 + 1 + .5 * 1 == -.5
assert -2 + 2 + .5 * 1 == .5
assert abs(sigmoid(-.5) - .3775406688) < 1e-10
assert abs(sigmoid(.5) - .6224593312) < 1e-10
assert abs(math.exp(-.5) - .6065306597) < 1e-10
assert abs(math.exp(.5) - 1.6487212707) < 1e-10
assert abs(math.exp(.5)/math.exp(-.5) - 2.7182818285) < 1e-10
assert abs(sigmoid(.5)-sigmoid(-.5)-.2449186624) < 1e-10
assert abs(2 + math.log(.7/.3) - 2.8472978604) < 1e-10
assert .2/(1-.2) == .25
assert (.25 * 3)/(1 + .25 * 3) == 3/7
assert abs(3/7-.4285714286) < 1e-10
assert 1/(1+4) == .2
for value in ('0.49', '0.51', '0.3775', '0.6065', '0.6225', '1.6487',
              '2.7183', '0.2449', '2.8473', '0.4286', '0.2', '0.7',
              '1944', '1958', 'N(0,1)', 'N(0,4)'):
    assert value in body, value
assert body.count('title="Proof"') == 1
assert '**Your turn.**' in body and 'title="Answer"' in body
for heading in ('Motivating example', 'Worked example', 'Common misconceptions', 'History'):
    assert f'## {heading}' in body, heading
assert body.count('![') == 0
for qid in ('ex-sl-08-1', 'ex-sl-08-4', 'ex-sl-08-7', 'ex-sl-10-7',
            'ex-sl-13-5', 'ex-sl-17-8', 'ex-sl-17-9'):
    assert f'../questions/{qid}.qmd' in page
pending = root / 'research/pending/interpretation-and-the-decision-boundary.json'
selected = (json.loads(pending.read_text())['self_checks'] if pending.exists()
            else json.loads((root / 'research/self-checks.json').read_text())['interpretation-and-the-decision-boundary'])
assert selected == ['ex-sl-10-7', 'ex-sl-08-3']
if not pending.exists():
    assert '## Check yourself' in body and body.count('title="Answer"') >= 3
print('rank 163 logistic boundary calculations and preservation checks passed')
