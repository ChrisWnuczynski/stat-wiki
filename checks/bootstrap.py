"""Enumerate bootstrap examples and check source-page numerical claims."""

from collections import Counter
from itertools import product
from math import isclose, sqrt, e
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
page = (ROOT / "articles/bootstrap.qmd").read_text()
content = (ROOT / "research/content/bootstrap.md").read_text()

def near(a, b, tol=5e-4):
    assert isclose(a, b, abs_tol=tol), (a, b)

sample = (2, 4, 6)
means = [sum(draw)/3 for draw in product(sample, repeat=3)]
counts = Counter(means)
assert sum(counts.values()) == 27
assert [counts[x] for x in (2, 8/3, 10/3, 4, 14/3, 16/3, 6)] == [1, 3, 6, 7, 6, 3, 1]
near(sum(means)/27, 4)
var = sum((x-4)**2 for x in means)/27
near(var, 8/9)
near(sqrt(var), sqrt(8)/3)
near(sqrt(var), .943, .0005)
means2 = [sum(draw)/2 for draw in product((1,3), repeat=2)]
assert means2 == [1,2,2,3]
near(sum(means2)/4, 2)
near(sum((x-2)**2 for x in means2)/4, .5)
near(sqrt(.5), .707, .0005)
for n, printed in ((10, .651), (100, .634)):
    near(1-(1-1/n)**n, printed, .0006)
near(1-1/e, .632, .0002)
near(1/e, .368, .0002)
near(1-(1-1/5)**5, .672, .0004)
near(1-(1-1/20)**20, .642, .0005)
near(.368*.05+.632*.20, .145, .0003)
assert '::: {.callout-note collapse="true" title="Proof"}' in page
assert '::: {.callout-tip collapse="true" title="Answer"}' in page
assert '## Worked example {#worked-example}' in page
assert '{#assumptions-and-limits}' in page
assert 'Lead context' not in content

# The chapter's occupancy calculation is copied into Definition, separately
# from the authored Properties proof. Both the calculation and its limit must
# survive there, inside a closed Proof rather than above the self-check.
definition = page.split('## Definition {#definition}', 1)[1].split('\n## ', 1)[0]
folded_proof = re.compile(
    r'^::: \{\.callout-note collapse="true" title="Proof"\}\n'
    r'::: \{\.proof\}\n(.*?)^:::\n:::', re.M | re.S)
proofs = folded_proof.findall(definition)
assert len(proofs) == 1, 'Definition needs one folded source proof'
visible_definition = folded_proof.sub('', definition)
for formula in (
    r'1-\Bigl(1-\frac1n\Bigr)^n',
    r'\log(1-1/n)=-1/n-1/(2n^2)+O(n^{-3})',
    r'\to 1-e^{-1}\approx 0.632',
):
    assert formula in proofs[0], ('missing source derivation', formula)
    assert formula not in visible_definition, ('visible source derivation', formula)

# The scoring definition is outside the proof; the source question still has
# its own folded answer, so hiding the derivation does not swallow either one.
assert '#def-sl-09-bootstrap-error' in visible_definition
assert r'=0.368\,' in visible_definition and r'+0.632\,' in visible_definition
self_check_headings = list(re.finditer(
    r'^### [^\n]+ \{#self-check-ex-sl-09-3\}$', page, re.M))
assert len(self_check_headings) == 1, 'Expected exactly one bootstrap self-check heading'
self_check = page[self_check_headings[0].end():]
assert 'collapse="true" title="Answer"' in self_check.split('\n### ', 1)[0]
print("bootstrap enumeration, inclusion numbers and structure passed")
