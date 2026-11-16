"""Check sample-space counts, induced probabilities and page structure."""

from math import comb, factorial, isclose
from pathlib import Path

root = Path(__file__).resolve().parents[1]
body = (root / 'articles/sample-space.qmd').read_text().split('## See also', 1)[0]

# Inherited three-toss questions and four counting formulas.
assert 2**3 == 8
assert [comb(3, k)/8 for k in range(4)] == [1/8, 3/8, 3/8, 1/8]
assert factorial(5)//factorial(5-2) == 20
assert comb(5, 2) == 10
assert comb(5+2-1, 2) == 15
# New labelled-ball example and hidden answer.
assert 5*4 == 20
assert 3*2 + 2*3 == 12
assert 12/20 == .6
assert 3*2/20 == .3 and 2*3/20 == .3 and 2*1/20 == .1
assert [2/20, 12/20, 6/20] == [.1, .6, .3]
assert isclose(sum([.1,.6,.3]), 1)
for printed in ('5\\cdot4=20', '12/20=0.6', '0.3,0.3,0.3,0.1',
                '2/20=0.1', '6/20=0.3'):
    assert printed in body, printed
assert body.count('![') == 0
assert body.count('title="Proof"') == 1
assert '## Motivating example' in body and '## Worked example' in body
assert '**Your turn.**' in body and 'title="Answer"' in body
for key in ('siegrist2022_events', 'vovk_shafer2003_kolmogorov'):
    assert f'data-cite-key="{key}"' in body
print('sample-space arithmetic and practice passed')
