"""Check uniform-distribution numbers, source examples and page structure."""

from math import isclose
from pathlib import Path
from scipy.stats import uniform
from scipy.integrate import quad

root = Path(__file__).resolve().parents[1]
body = (root / 'articles/uniform-distribution.qmd').read_text().split('## See also', 1)[0]

assert isclose(uniform(loc=2, scale=6).pdf(4), 1/6)
assert isclose(uniform(loc=2, scale=6).cdf(6)-uniform(loc=2, scale=6).cdf(3), .5)
assert uniform(loc=2, scale=6).mean() == 5
assert uniform(loc=2, scale=6).var() == 3
assert isclose(uniform(loc=2, scale=6).ppf(.9), 7.4)
assert isclose(uniform(loc=-2, scale=6).cdf(3)-uniform(loc=-2, scale=6).cdf(0), .5)
assert uniform(loc=-2, scale=6).mean() == 1
assert uniform(loc=-2, scale=6).var() == 3
assert isclose(uniform(loc=-2, scale=6).ppf(.75), 2.5)
assert isclose(uniform(loc=2, scale=4).cdf(5)-uniform(loc=2, scale=4).cdf(3), .5)
assert isclose(10+5*.2, 11)
assert isclose(quad(lambda x: x, 0, 1)[0]+quad(lambda x: 2-x, 1, 2)[0], 1)
for printed in ('1/6', '0.5', '7.4', '2.5', '6^2/12=3', 'U=0.2'):
    assert printed in body, printed
assert body.count('![') == 2
assert body.count('title="Proof"') == 1
assert '## Motivating example' in body and '### Worked example' in body
assert '**Your turn.**' in body and 'title="Answer"' in body
for key in ('siegrist2022_uniform_interval', 'von_neumann1951_random_digits'):
    assert f'data-cite-key="{key}"' in body
print('uniform-distribution arithmetic and practice passed')
