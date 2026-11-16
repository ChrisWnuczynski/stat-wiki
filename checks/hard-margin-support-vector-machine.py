"""Check rank-172 SVM geometry, dual arithmetic and preserved content."""
from pathlib import Path
import json
import math
import sympy as sp

root = Path(__file__).resolve().parents[1]
page = (root / 'articles/hard-margin-support-vector-machine.qmd').read_text()
body = page.split('## See also')[0]


def check_fit(xs, ys, w, b, alphas, full_margin, objective):
    xs = [sp.Rational(x) for x in xs]
    w, b = sp.Rational(w), sp.Rational(b)
    alphas = [sp.Rational(a) for a in alphas]
    assert all(y * (w * x + b) >= 1 for x, y in zip(xs, ys))
    assert all(a >= 0 for a in alphas)
    assert sum(a * y for a, y in zip(alphas, ys)) == 0
    assert w == sum(a * y * x for x, y, a in zip(xs, ys, alphas))
    assert all(a * (y * (w * x + b) - 1) == 0
               for x, y, a in zip(xs, ys, alphas))
    primal = w * w / 2
    dual = sum(alphas) - w * w / 2
    assert primal == dual == sp.Rational(objective)
    assert 2 / abs(w) == sp.Rational(full_margin)


check_fit([-2, -1, 1, 2], [-1, -1, 1, 1], 1, 0,
          [0, sp.Rational(1, 2), sp.Rational(1, 2), 0], 2, sp.Rational(1, 2))
check_fit([-2, -1, sp.Rational(1, 2), 2], [-1, -1, 1, 1],
          sp.Rational(4, 3), sp.Rational(1, 3),
          [0, sp.Rational(8, 9), sp.Rational(8, 9), 0],
          sp.Rational(3, 2), sp.Rational(8, 9))
assert sp.Rational(4, 3) * sp.Rational(-1, 4) + sp.Rational(1, 3) == 0
assert sp.Rational(1, 2) - (-1) == sp.Rational(3, 2)
assert sp.Rational(-1, 4) == (-1 + sp.Rational(1, 2)) / 2

# Retained two-dimensional, three-observation example.
points = [sp.Matrix([1, 0]), sp.Matrix([3, 1]), sp.Matrix([3, -1])]
labels = [-1, 1, 1]
weight = sp.Matrix([1, 0])
alpha = [sp.Rational(1, 2), sp.Rational(1, 4), sp.Rational(1, 4)]
assert all(y * (weight.dot(x) - 2) == 1 for x, y in zip(points, labels))
assert sum((a * y * x for a, y, x in zip(alpha, labels, points)), sp.zeros(2, 1)) == weight
assert sum(a * y for a, y in zip(alpha, labels)) == 0
assert sum(alpha) - weight.dot(weight) / 2 == weight.dot(weight) / 2 == sp.Rational(1, 2)
assert 2 / sp.sqrt(weight.dot(weight)) == 2
assert -1 - weight.dot(points[0]) == -2

# The alternative source-chapter soft-margin convention rescales C by one half.
assert sp.simplify((2 * sp.Symbol('P') + sp.Symbol('C') * sp.Symbol('S')) / 2 -
                   (sp.Symbol('P') + sp.Symbol('C') * sp.Symbol('S') / 2)) == 0

# Both XOR classes have the same convex-hull midpoint; a duplicate with opposite
# labels would require the same score to be at least +1 and at most -1.
assert (sp.Matrix([0, 0]) + sp.Matrix([1, 1])) / 2 == sp.Matrix([sp.Rational(1, 2)] * 2)
assert (sp.Matrix([0, 1]) + sp.Matrix([1, 0])) / 2 == sp.Matrix([sp.Rational(1, 2)] * 2)
assert not any(t <= -1 and t >= 1 for t in [-2, -1, 0, 1, 2])

for token in ('-2,-1,1,2', '1/2', '4/3', '1/3', '3/2', '8/9', '-1/4',
              '(1,0)', '(3,1)', '(3,-1)', '\\tfrac12', '\\tfrac14',
              '1992', '1995'):
    assert token in body, token
assert body.count('title="Proof"') == 1
assert '**Your turn.**' in body and 'title="Answer"' in body
for section in ('motivating-example', 'intuition', 'definition', 'interpretation',
                'properties', 'statistical-use', 'worked-example',
                'common-misconceptions', 'assumptions-and-limits',
                'connections', 'history'):
    assert f'{{#{section}}}' in body, section
for link in ('hard-margin-dual.qmd', 'hard-margin-primal.qmd',
             'support-vectors-and-their-multipliers.qmd',
             'ex-sl-17-2.qmd', 'ex-sl-17-9.qmd'):
    assert link in page, link
ids = json.loads((root / 'research/self-checks.json').read_text())['hard-margin-support-vector-machine']
assert ids == ['ex-sl-17-2', 'ex-sl-17-9']
print('rank 172 hard-margin SVM numeric and preservation checks passed')
