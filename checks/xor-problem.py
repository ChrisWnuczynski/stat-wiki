"""Check XOR truth tables, representation limits and numeric examples."""

from itertools import product
from pathlib import Path
from math import isclose

page = (Path(__file__).resolve().parents[1] / 'articles/xor-problem.qmd').read_text()
body = page.split('## See also', 1)[0]
points = list(product((0, 1), repeat=2))
f = lambda u: int(u >= 0)
xor = lambda x1, x2: x1 != x2
assert points == [(0,0),(0,1),(1,0),(1,1)]
assert [int(xor(*p)) for p in points] == [0,1,1,0]
assert [f(x+y-.5) for x,y in points] == [0,1,1,1]
assert [f(x+y-1.5) for x,y in points] == [0,0,0,1]
assert [f(x+y-.5)-f(x+y-1.5) for x,y in points] == [0,1,1,0]
assert [f(f(x+y-.5)-f(x+y-1.5)-.5) for x,y in points] == [0,1,1,0]
assert [1-f(x+y-.5)+f(x+y-1.5) for x,y in points] == [1,0,0,1]
assert [x+y-2*x*y for x,y in points] == [0,1,1,0]
assert [x+y-2*x*y-.5 for x,y in points] == [-.5,.5,.5,-.5]
assert isclose(.8+.8-2*.8*.8,.32)
assert f(.8+.8-.5)-f(.8+.8-1.5)==0
for printed in ('(0,1,1,0)', '(1,0,0,1)', '0.32', '(0.8,0.8)', '-1/2,1/2,1/2,3/2', 'x_1x_2'):
    assert printed in body, f'Missing printed value: {printed}'
assert body.count('title="Proof"') == 1
assert '**Your turn.**' in body and 'title="Answer"' in body
for key in ('goodfellow_bengio_courville2016', 'rumelhart_hinton_williams1986'):
    assert f'data-cite-key="{key}"' in body
print('XOR arithmetic, logic, and representation checks passed')
