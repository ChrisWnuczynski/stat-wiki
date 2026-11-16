"""Check rank-168 sandwich calculations and preserved links."""
from pathlib import Path
import json
import math
import numpy as np

root = Path(__file__).resolve().parents[1]
page = (root/'articles/sandwich-estimator.qmd').read_text()
body = page.split('## See also')[0]

x = np.array([[1,2],[2,3],[4,5],[6,7]],dtype=float)
mu = x.mean()
cluster_scores = (x-mu).sum(axis=1)
A = x.size
B = float(cluster_scores@cluster_scores)
assert mu == 3.75 and A == 8
assert np.allclose(cluster_scores,[-4.5,-2.5,1.5,5.5])
assert B == 59 and B/A**2 == .921875
assert math.isclose(math.sqrt(B/A**2),.960,abs_tol=.001)
naive_var=float(x.var(ddof=1)/A)
assert naive_var == .5625 and math.sqrt(naive_var)==.75
y=np.array([[1,2],[3,4],[5,6]],dtype=float)
scores=(y-y.mean()).sum(axis=1)
assert y.mean()==3.5 and np.allclose(scores,[-4,0,4])
assert scores@scores==32 and math.isclose(32/6**2,.8889,abs_tol=.0001)

for number in ('3.75','-4.5','-2.5','1.5','5.5','20.25','6.25','2.25',
               '30.25','59','0.921875','0.960','0.5625','0.750','3.5',
               '0.8889','1967','1980','1986'):
    assert number in body, number
assert body.count('title="Proof"')==1
assert '**Your turn.**' in body and 'title="Answer"' in body
for heading in ('Motivating example','Definition','Interpretation','Worked example',
                'Common misconceptions','History'):
    assert f'## {heading}' in body,heading
for link in ('generalised-estimating-equations.qmd','marginal-model.qmd',
             'working-correlation.qmd','c-40.qmd'):
    assert link in page,link
pending=json.loads((root/'research/pending/sandwich-estimator.json').read_text())
assert pending['self_checks']==['c-40','depth-sandwich-cluster-calculation']
assert pending['new_bank_questions'][0]['id']=='depth-sandwich-cluster-calculation'
print('rank 168 sandwich numeric and preservation checks passed')
