"""Check the LLN numeric examples and retained figure."""

from math import isclose
from pathlib import Path
from scipy.stats import binom, cauchy

root = Path(__file__).resolve().parents[1]
body = (root / 'articles/law-of-large-numbers.qmd').read_text().split('## See also', 1)[0]

for n, bound, inclusive in ((100, .25, .05688793364098089),
                            (400, .0625, .00007426568076372613)):
    assert isclose(.25 / (n * .1**2), bound)
    exact = binom.cdf(int(.4*n), n, .5) + binom.sf(int(.6*n)-1, n, .5)
    assert isclose(exact, inclusive, rel_tol=1e-10)
assert isclose(cauchy(scale=1).cdf(1), .75)
assert isclose(1/2, .5)
for printed in ('0.25', '0.056888', '0.0625', '0.0000743', '6.25'):
    assert printed in body, printed
assert body.count('![') == 1
assert body.count('title="Proof"') == 1
assert '## Statement {#statement}' in body
assert '## Motivating example' in body and '## Examples {#examples}' in body
assert '**Your turn.**' in body and 'title="Answer"' in body
for key in ('siegrist2022_lln', 'dodge2008'):
    assert f'data-cite-key="{key}"' in body
print('law-of-large-numbers arithmetic and structure passed')
