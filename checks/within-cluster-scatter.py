"""Check within-cluster scatter, Stirling counts and objective distinction."""

from math import isclose
from pathlib import Path

from sympy.functions.combinatorial.numbers import stirling

root = Path(__file__).resolve().parents[1]
body = (root / 'articles/within-cluster-scatter.qmd').read_text().split('## See also', 1)[0]

def ss(xs):
    mu = sum(xs) / len(xs)
    return sum((x - mu) ** 2 for x in xs)

def pair(xs):
    return sum((x-y)**2 for i,x in enumerate(xs) for y in xs[i+1:])

A, B = [0,2], [10,11,12]
assert ss(A) == ss(B) == 2
assert pair(A) == 4 and pair(B) == 6
assert ss(A)+ss(B) == 4 and pair(A)+pair(B) == 10
assert len(A)*ss(A)+len(B)*ss(B) == 10
A2, B2 = [0,4], [10,11]
assert ss(A2) == 8 and ss(B2) == .5
assert pair(A2) == 16 and pair(B2) == 1
assert ss(A2)+ss(B2) == 8.5 and pair(A2)+pair(B2) == 17
oldA, oldB = [0,1,3], [2,7]
newA, newB = [0,1], [2,3,7]
assert isclose(ss(oldA)+ss(oldB), 103/6)
assert ss(newA)+ss(newB) == 14.5
assert pair(oldA)+pair(oldB) == 39
assert pair(newA)+pair(newB) == 43
assert (3-4.5)**2 < (3-4/3)**2
assert int(stirling(10,3)) == 9330
assert int(stirling(25,5)) == 2436684974110751
assert round(float(stirling(100,5))/10**67, 1) == 6.6
assert 100**2 == 10000
for printed in ('9330', '2436684974110751', '6.6', '17.17', '14.5', '39', '43', '8.5', '17'):
    assert printed in body, printed
assert body.count('title="Proof"') == 1
assert '## Motivating example' in body and '## Worked example' in body
assert '**Your turn.**' in body and 'title="Answer"' in body
print('within-cluster objective arithmetic and structure passed')
