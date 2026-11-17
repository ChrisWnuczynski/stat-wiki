"""Check rank-161 pooled and grand-mean covariance numbers and preservation."""
from pathlib import Path
import json
import sympy as sp

root=Path(__file__).resolve().parents[1]
page=(root/'articles/pooled-covariance.qmd').read_text()
body=page.split('## See also')[0]
A=[sp.Matrix(x) for x in [(-1,0),(1,0),(0,-1),(0,1)]]
B=[sp.Matrix(x) for x in [(3,1),(5,1),(4,0),(4,2)]]
mean=lambda group: sum(group,sp.zeros(2,1))/len(group)
scatter=lambda group,center: sum(((x-center)*(x-center).T for x in group),sp.zeros(2,2))
assert mean(A)==sp.Matrix([0,0]) and mean(B)==sp.Matrix([4,1])
assert scatter(A,mean(A))==sp.diag(2,2)
assert scatter(B,mean(B))==sp.diag(2,2)
pooled=(scatter(A,mean(A))+scatter(B,mean(B)))/(8-2)
assert pooled==sp.diag(sp.Rational(2,3),sp.Rational(2,3))
allx=A+B
grand=mean(allx)
assert grand==sp.Matrix([2,sp.Rational(1,2)])
between=sum((len(g)*(mean(g)-grand)*(mean(g)-grand).T for g in (A,B)),sp.zeros(2,2))
assert between==sp.Matrix([[32,8],[8,2]])
total=scatter(allx,grand)
assert total==sp.Matrix([[36,8],[8,6]])
assert total/7==sp.Matrix([[sp.Rational(36,7),sp.Rational(8,7)],[sp.Rational(8,7),sp.Rational(6,7)]])
assert total==scatter(A,mean(A))+scatter(B,mean(B))+between
one=[1,2,3];two=[5,6,7]
assert sum((x-2)**2 for x in one)==2 and sum((x-6)**2 for x in two)==2
assert (2+2)/(6-2)==1
assert sum((x-4)**2 for x in one+two)==28 and sp.Rational(28,5)==sp.Rational(56,10)
assert 6-2==4 and 5>4
assert 50+50-2==98

for literal in ('n-G','2/3','32&8','36&8','5.6','98','6-2=4','n_1+n_2-2'):
    assert literal in body,literal
assert body.count('title="Proof"')==1
assert '**Your turn.**' in body and 'title="Answer"' in body
assert body.count('![')==0
for heading in ('Motivating example','Worked example','Common misconceptions','When pooling misleads','History'):
    assert f'## {heading}' in body,heading
for q in ('ex-sl-02-2','ex-sl-02-6','ex-sl-18-7'):
    assert f'../questions/{q}.qmd' in page
selected = json.loads((root/'research/self-checks.json').read_text())['pooled-covariance']
assert selected==['ex-sl-02-2','ex-sl-18-7']
print('rank 161 covariance, rank and preservation checks passed')
