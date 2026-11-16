"""Check rank-167 covariance and example arithmetic."""
from pathlib import Path
import json
import math
import numpy as np

root = Path(__file__).resolve().parents[1]
page = (root / 'articles/repeated-measures.qmd').read_text()
body = page.split('## See also')[0]

assert 9/(9+1) == .9
assert math.isclose(9/10 + 1/20, .95)
assert abs(math.sqrt(.95)-.975) < .001
assert (9+1)/20 == .5
assert abs(math.sqrt(.5)-.707) < .001
assert 4/(4+1) == .8
assert math.isclose(4/5 + 1/10, .9)
assert (4+1)/10 == .5
assert abs(.9-.5-.4) < 1e-12
for m,rho in [(4,-1/3),(4,1),(2,-1),(6,-.2)]:
    cov=(1-rho)*np.eye(m)+rho*np.ones((m,m))
    assert min(np.linalg.eigvalsh(cov)) > -1e-12
assert min(np.linalg.eigvalsh((1+.34)*np.eye(4)-.34*np.ones((4,4)))) < 0

for number in ('0.9','0.95','0.975','0.50','0.707','0.8','0.4'):
    assert number in body, number
assert body.count('title="Proof"') == 1
assert '**Your turn.**' in body and 'title="Answer"' in body
for heading in ('Motivating example','Definition','Intuition','Statistical use',
                'Worked example','Common misconceptions','History'):
    assert f'## {heading}' in body, heading
for link in ('linear-mixed-model.qmd','marginal-model.qmd','intraclass-correlation.qmd',
             'ex-toenail-glmm.qmd'):
    assert link in page, link
assert json.loads((root/'research/pending/repeated-measures.json').read_text())['self_checks'] == ['ex-orthodont-lmm','ex-toenail-glmm']
print('rank 167 repeated-measures numeric and preservation checks passed')
