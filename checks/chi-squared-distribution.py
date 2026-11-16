"""Check rank-164 chi-squared values, examples, plots and bank links."""
from pathlib import Path
import json
import math
from scipy.stats import chi2

root = Path(__file__).resolve().parents[1]
page = (root / 'articles/chi-squared-distribution.qmd').read_text()
body = page.split('## See also')[0]

# Density family, four-coordinate example and new practice.
assert sum(z*z for z in (1, -1, 2, 0)) == 6
assert chi2.mean(4) == 4 and chi2.var(4) == 8
assert abs(chi2.sf(6, 4) - 4*math.exp(-3)) < 1e-14
assert abs(chi2.sf(6, 4) - .1991482735) < 1e-10
assert chi2.mean(2) == 2 and chi2.var(2) == 4
assert abs(chi2.sf(4, 2) - math.exp(-2)) < 1e-14
assert abs(chi2.sf(4, 2) - .1353352832) < 1e-10
assert chi2.mean(12) == 12 and chi2.var(12) == 24
assert abs(math.sqrt(8/4) - math.sqrt(2)) < 1e-14

# Preserved aspirin variance interval and normal square transformation.
assert 25-1 == 24 and abs(1.3**2-1.69) < 1e-14
assert abs(24*1.69-40.56) < 1e-14
assert abs(chi2.ppf(.025, 24)-12.40) < .01
assert abs(chi2.ppf(.975, 24)-39.36) < .01
assert abs(40.56/39.36-1.03) < .01
assert abs(40.56/12.40-3.27) < .01
assert abs(math.sqrt(40.56/39.36)-1.02) < .01
assert abs(math.sqrt(40.56/12.40)-1.81) < .01
assert 1.0 < math.sqrt(40.56/39.36)

# Preserved tuning fork variance test.
fork = 6*.488/1.1
assert abs(fork-2.66) < .01
assert abs(chi2.cdf(fork, 6)-.15) < .001
assert abs(chi2.ppf(.05, 6)-1.635) < .001
assert fork > 1.635
assert abs(1.1*chi2.ppf(.05, 6)/6 - .30) < .001

for number in ('0.1991', '0.1353', '1.3', '1.69', '40.56',
               '12.40', '39.36', '1.03', '3.27', '1.02', '1.81',
               '0.488', '1.1', '2.66', '0.15', '1.635', '0.30',
               '1860', '1863', '1838', '1881', '1900'):
    assert number in body, number
assert body.count('title="Proof"') == 1
assert '**Your turn.**' in body and 'title="Answer"' in body
for heading in ('Motivating example', 'Worked example', 'Common misconceptions', 'History'):
    assert f'## {heading}' in body, heading
assert 'chi-squared-distribution-pdf.png' in page
assert 'chi-squared-distribution-cdf.png' in page
assert body.count('![') == 2
for link in ('normal-sample-theorem.qmd', 'pearson-chi-squared-approximation.qmd',
             'pearson-test-with-estimated-parameters.qmd', 'gamma-distribution.qmd',
             'f-distribution.qmd', 'wishart-distribution.qmd'):
    assert link in page, link
pending = root / 'research/pending/chi-squared-distribution.json'
selected = (json.loads(pending.read_text())['self_checks'] if pending.exists()
            else json.loads((root / 'research/self-checks.json').read_text())['chi-squared-distribution'])
assert selected == ['ex-inf-die-fairness', 'ex-inf-degrees-of-freedom']
if not pending.exists():
    assert '## Check yourself' in body and body.count('title="Answer"') >= 3
print('rank 164 chi-squared numeric and preservation checks passed')
