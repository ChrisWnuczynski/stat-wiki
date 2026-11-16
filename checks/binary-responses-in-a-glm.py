"""Verify new Bernoulli likelihood, mean, variance and logit numbers."""
import math
from pathlib import Path

logistic=lambda eta:1/(1+math.exp(-eta))
p0,p1,p2=[logistic(-1+.8*x) for x in (0,1,2)]
assert math.isclose(p0,.26894,abs_tol=5e-6)
assert math.isclose(p1,.45017,abs_tol=5e-6)
assert math.isclose(p2,.64566,abs_tol=5e-6)
assert math.isclose((1-p0)*p1,.32910,abs_tol=5e-6)
assert math.isclose(math.exp(.8),2.22554,abs_tol=5e-6)
assert math.isclose(p1-p0,.18122,abs_tol=5e-6)
assert math.isclose(p2*(1-p2),.22878,abs_tol=5e-6)
assert math.isclose(.8*(1-.8),.16)
assert math.isclose((1-.25)*.60,.45)
assert math.isclose(.5*(1-.5),.25)
root=Path(__file__).resolve().parents[1]
source=(root/'research/content/binary-responses-in-a-glm.md').read_text()
for number in ('0.26894','0.45017','0.64566','0.32910','2.22554','0.18122','0.22878','0.16'):
    assert number in source
page=root/'articles/binary-responses-in-a-glm.qmd'
if page.exists():
    rendered=page.read_text()
    for preserved in ('fig-links', 'ex-toenail-glmm.qmd', 'Three links', 'title="Proof"'):
        assert preserved in rendered
