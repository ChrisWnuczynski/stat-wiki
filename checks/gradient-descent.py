"""Check rank-170 gradient steps, stability and preservation."""
from pathlib import Path
import json
import math
import sympy as sp

root=Path(__file__).resolve().parents[1]
page=(root/'articles/gradient-descent.qmd').read_text()
body=page.split('## See also')[0]
w=sp.symbols('w')
E=(w-3)**2
dE=sp.diff(E,w)
assert dE.subs(w,0)==-6
def step(x,rate):return x-rate*float(dE.subs(w,x))
w1=step(0,.1); w2=step(w1,.1)
assert math.isclose(w1,.6) and math.isclose(float(E.subs(w,w1)),5.76)
assert math.isclose(float(dE.subs(w,w1)),-4.8)
assert math.isclose(w2,1.08) and math.isclose(float(E.subs(w,w2)),3.6864)
assert math.isclose(step(0,1.1),6.6) and math.isclose(float(E.subs(w,6.6)),12.96)
assert step(0,.5)==3 and E.subs(w,3)==0
assert step(0,1)==6 and step(6,1)==0
assert math.isclose((float(E.subs(w,.01))-float(E.subs(w,-.01)))/.02,-6)
assert sp.diff(1-w*w,w).subs(w,0)==0 and sp.diff(1-w*w,w,2)<0
for token in ('[-0.5,0.5]','0.1','0.6','5.76','1.08','3.6864',
              '6.6','12.96','0.5','1.1','0.01','2.99','3.01','1847'):
    assert token in body,token
assert body.count('title="Proof"')==1
assert '**Your turn.**' in body and 'title="Answer"' in body
for heading in ('Motivating example','Definition','Worked example','Practical variants and checks',
                'Common misconceptions','History'):
    assert f'## {heading}' in body,heading
for link in ('basic-gradient-descent-learning.qmd','stochastic-gradient-descent.qmd',
             'ex-sl-15-4.qmd','ex-sl-15-7.qmd'):
    assert link in page,link
assert json.loads((root/'research/self-checks.json').read_text())['gradient-descent']==['ex-sl-15-4','ex-sl-15-7']
print('rank 170 gradient-descent numeric and preservation checks passed')
