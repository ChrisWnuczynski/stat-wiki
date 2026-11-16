"""Check rank-63 numerical statements and rendered practice."""
from pathlib import Path
import math
import statistics

root = Path(__file__).resolve().parents[1]
page = (root / 'articles/monte-carlo-method.qmd').read_text()
body = page.split('## See also')[0]
values = [0.2, 0.7, 0.9, 0.4, 0.6]
h = [x*x for x in values]
assert math.isclose(sum(h), 1.86)
assert math.isclose(statistics.mean(h), 0.372)
assert math.isclose(sum((x-statistics.mean(h))**2 for x in h), 0.36108)
assert math.isclose(statistics.variance(h), 0.09027)
assert math.isclose(math.sqrt(statistics.variance(h)/5), 0.13436517405935217)
assert math.isclose(statistics.mean(h)-1/3, 0.03866666666666668)
practice = [0.1, 0.3, 0.7, 0.9]
assert math.isclose(sum(x*x for x in practice), 1.40)
assert math.isclose(sum(x*x for x in practice)/4, 0.35)
assert math.isclose(0.35-1/3, 1/60)
assert math.isclose(1/5-1/9, 4/45)
assert math.isclose(math.sqrt(100), 10)
assert 100*100 == 10**4
for printed in ('1.86', '0.372', '0.3333', '0.0387', '0.36108', '0.09027',
                '0.13437', '1.40', '0.35', '0.0167', '100\\times100', '10^4'):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
for heading in ('Motivating example', 'Worked example', 'Common misconceptions',
                'Assumptions and limits', 'History', 'Check yourself'):
    assert f'## {heading}' in body
assert '**Your turn.**' in body and body.count('title="Answer"') >= 3
for key in ('dasgupta2011_graduate_probability', 'hastings1970', 'metropolis_ulam1949'):
    assert f'data-cite-key="{key}"' in body
for qid in ('c-11','c-15'):
    assert f'../questions/{qid}.qmd' in page
print('Monte Carlo estimates, variance, rate and practice passed')
