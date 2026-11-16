"""Check rank-169 nearest-neighbour numbers and page preservation."""
from pathlib import Path
import json

root=Path(__file__).resolve().parents[1]
page=(root/'articles/apparent-error.qmd').read_text()
body=page.split('## See also')[0]

x=[0,2,5,9]
def loo(labels):
    predictions=[]
    for i,xi in enumerate(x):
        j=min((j for j in range(len(x)) if j!=i),key=lambda j:abs(xi-x[j]))
        predictions.append(labels[j])
    return predictions,sum(a!=b for a,b in zip(predictions,labels))/len(x)
assert loo([0,0,1,1])==([0,0,0,1],.25)
assert loo([0,1,1,0])==([1,0,1,1],.75)
assert all(x[i]!=x[j] for i in range(4) for j in range(i))

for token in ('0/4=0','1/4=0.25','3/4=0.75','(0,2,5,9)',
              'one-nearest-neighbour'):
    assert token in body,token
assert body.count('title="Proof"')==1
assert '**Your turn.**' in body and 'title="Answer"' in body
for heading in ('Motivating example','Definition','Interpretation','Worked example',
                'Common misconceptions','History'):
    assert f'## {heading}' in body,heading
for link in ('cross-validation.qmd','bootstrap.qmd','fixed-rule-error.qmd',
             'nearest-neighbours.qmd','ex-sl-11-5.qmd','ex-sl-12-6.qmd'):
    assert link in page,link
assert json.loads((root/'research/pending/apparent-error.json').read_text())['self_checks']==['ex-sl-11-5','ex-sl-12-7']
print('rank 169 apparent-error numeric and preservation checks passed')
