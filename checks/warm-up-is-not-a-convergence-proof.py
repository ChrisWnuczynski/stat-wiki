"""Verify the two-state-chain arithmetic and preservation on the warm-up page."""
import math
from pathlib import Path

def values(p, t):
    no_switch = (1-p)**t
    at_a = (1+(1-2*p)**t)/2
    return no_switch, at_a

no_switch, at_a = values(.001, 1000)
assert math.isclose(no_switch, .36770, abs_tol=5e-6)
assert math.isclose(at_a, .56753, abs_tol=5e-6)
assert math.isclose((1-.001), .999)
assert math.isclose((1-2*.001), .998)
no_switch, at_a = values(.0001, 1000)
assert math.isclose(no_switch, .90483, abs_tol=5e-6)
assert math.isclose(at_a, .90936, abs_tol=5e-6)
assert math.isclose((1-.0001), .9999)
assert math.isclose((1-2*.0001), .9998)
assert math.isclose(.5, .5)
root=Path(__file__).resolve().parents[1]
source=(root/'research/content/warm-up-is-not-a-convergence-proof.md').read_text()
for number in ('0.36770', '0.56753', '0.90483', '0.90936', '0.9999', '0.9998', '1{,}000'):
    assert number in source
page=root/'articles/warm-up-is-not-a-convergence-proof.qmd'
if page.exists():
    rendered=page.read_text()
    for preserved in ('part1-fig-04-proposal-scale.png', 'example-c-15', 'example-q-19', 'q-25.qmd', 'ex-gibbs-mh.qmd'):
        assert preserved in rendered
    assert 'title="Proof"' in rendered
