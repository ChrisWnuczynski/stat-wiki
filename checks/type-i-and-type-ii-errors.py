"""Check rank-166 error probabilities, examples and preservation."""
from pathlib import Path
import json
from scipy.stats import norm, binom

root = Path(__file__).resolve().parents[1]
page = (root / 'articles/type-i-and-type-ii-errors.qmd').read_text()
body = page.split('## See also')[0]

assert abs(norm.ppf(.975)-1.960) < .001
assert abs(2*norm.sf(2.30)-.021) < .001
beta_two = norm.cdf(1.960-2)-norm.cdf(-1.960-2)
assert abs(beta_two-.484) < .001 and abs(1-beta_two-.516) < .001
assert abs(binom.sf(12,15,.6)-.0271) < .0001
assert abs(binom.sf(12,15,.8)-.398) < .001
assert abs(binom.sf(12,15,.9)-.816) < .001
assert abs(binom.sf(11,15,.6)-.0905) < .0001
assert abs(1-binom.sf(12,15,.8)-.602) < .001
assert abs(norm.sf(1.645)-.0500) < .0001
assert abs(norm.cdf(1.645-1)-.7405) < .0001
assert abs(norm.sf(1.645-1)-.2595) < .0001
assert abs(norm.cdf(1.645-2)-.3612) < .0001
assert abs(norm.sf(1.645-2)-.6388) < .0001
assert abs(1-.95**20-.642) < .001

for number in ('0.0271','0.398','0.816','0.0905','0.7405','0.2595',
               '0.3612','0.6388','0.602','0.642','1.960','2.30','0.021',
               '0.484','0.516','1.645','1928'):
    assert number in body, number
assert page.count('inf-04-hypothesis-tests-errors.png') == 1
assert page.count('inf-power-curve.png') == 1
assert body.count('![') == 2
assert body.count('title="Proof"') == 1
assert '**Your turn.**' in body and 'title="Answer"' in body
for heading in ('Motivating example', 'Definition', 'Interpretation', 'Worked example',
                'Common misconceptions', 'History'):
    assert f'## {heading}' in body, heading
pending = root / 'research/pending/type-i-and-type-ii-errors.json'
ids = json.loads(pending.read_text())['self_checks']
assert ids == ['ex-inf-serve-power', 'ex-inf-np-critical']
print('rank 166 type I/II numeric and preservation checks passed')
