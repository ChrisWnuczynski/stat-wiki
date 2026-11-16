"""Check rank-171 whitening and numerical examples."""
from pathlib import Path
import json
import math
import numpy as np
from scipy.stats import chi2

root=Path(__file__).resolve().parents[1]
page=(root/'articles/squared-mahalanobis-distance.qmd').read_text()
body=page.split('## See also')[0]
S=np.diag([4.,1.])
assert np.allclose(np.linalg.eigvalsh(S),[1,4])
assert math.isclose(np.array([2,0])@np.linalg.inv(S)@np.array([2,0]),1)
assert math.isclose(np.array([0,2])@np.linalg.inv(S)@np.array([0,2]),4)
S=np.array([[4.,1.],[1.,1.]])
Sinv=np.linalg.inv(S)
assert math.isclose(np.linalg.det(S),3) and np.allclose(Sinv,np.array([[1,-1],[-1,4]])/3)
for x,dist in [([2,1],4/3),([2,-1],4),([1,1],1),([1,-1],7/3)]:
    v=np.array(x)
    assert math.isclose(v@Sinv@v,dist)
assert sum(np.array([2,1])**2)==5 and sum(np.array([2,-1])**2)==5
assert sum(np.array([1,1])**2)==2 and sum(np.array([1,-1])**2)==2
assert math.isclose(4/3,1.333,abs_tol=.001)
assert math.isclose(7/3,2.333,abs_tol=.001)
assert chi2.mean(2)==2

for token in ('(2,0)','(0,2)','1.333','2.333','4/3','7/3',
              '1930','1936'):
    assert token in body,token
assert body.count('title="Proof"')==1
assert '**Your turn.**' in body and 'title="Answer"' in body
for heading in ('Motivating example','Definition','Intuition','Properties','Statistical use',
                'Worked example','Common misconceptions','History'):
    assert f'## {heading}' in body,heading
for link in ('chi-squared-distribution.qmd','cholesky-decomposition.qmd',
             'ex-sl-01-4.qmd','ex-applied-bvn-rwmh.qmd'):
    assert link in page,link
ids = json.loads((root / 'research/self-checks.json').read_text())['squared-mahalanobis-distance']
assert ids==['ex-sl-01-4','ex-applied-bvn-rwmh']
assert 'squared-mahalanobis-distance' in json.loads((root/'article_leads.json').read_text())
print('rank 171 Mahalanobis numeric and preservation checks passed')
