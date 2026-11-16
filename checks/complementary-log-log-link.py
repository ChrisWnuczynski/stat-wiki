"""Verify link, inverse, hazard-scale examples, and preserved page material."""
import math
from pathlib import Path

def inverse(eta): return 1-math.exp(-math.exp(eta))
def link(p): return math.log(-math.log(1-p))

assert math.isclose(inverse(0), .63212, abs_tol=5e-6)
assert math.isclose(link(.5), -.36651, abs_tol=5e-6)
assert math.isclose(inverse(-2), .12658, abs_tol=5e-6)
assert math.isclose(inverse(2), .99938, abs_tol=5e-6)
for eta, rounded in [(-1,.31),(0,.63),(1,.93),(-2,.13),(2,.999)]:
    assert math.isclose(inverse(eta),rounded,abs_tol=.005)
assert math.isclose(inverse(0)-inverse(-1),.32,abs_tol=.005)
assert math.isclose(inverse(1)-inverse(0),.30,abs_tol=.005)
h0=-math.log(.8)
assert math.isclose(h0,.22314,abs_tol=5e-6)
assert math.isclose(math.log(h0),-1.49994,abs_tol=5e-6)
assert math.isclose(math.log(2),.69315,abs_tol=5e-6)
assert math.isclose(2*h0,.44629,abs_tol=5e-6)
assert math.isclose(1-math.exp(-2*h0),.36)
assert math.isclose(.9**3,.729)
assert math.isclose(1-.9**3,.271)
assert math.isclose(math.log(3),1.09861,abs_tol=5e-6)
for p in (.1,.2,.5,.8): assert math.isclose(inverse(link(p)),p)
root=Path(__file__).resolve().parents[1]
source=(root/'research/content/complementary-log-log-link.md').read_text()
for number in ('0.63212','-0.36651','0.12658','0.99938','0.22314','-1.49994','0.69315','0.44629','0.36','0.729','0.271','1.09861'):
    assert number in source
page=root/'articles/complementary-log-log-link.qmd'
if page.exists():
    rendered=page.read_text()
    for preserved in ('g(p)=', 'Any event, or none', 'logit-link.qmd', 'probit-link.qmd', 'title="Proof"'):
        assert preserved in rendered
