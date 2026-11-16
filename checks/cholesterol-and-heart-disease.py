"""Verify internal arithmetic of the printed fit; raw patient data are unavailable."""
import math
from pathlib import Path

def prob(male,chol):
    eta=-9.3203-.1094*male+1.5842*chol
    return eta,1/(1+math.exp(-eta))

assert math.isclose(prob(0,0)[1],8.96e-5,rel_tol=.001)
assert math.isclose(math.exp(1.5842),4.88,abs_tol=.005)
assert math.isclose(math.exp(1.5842),4.87539,abs_tol=5e-6)
assert math.isclose(math.exp(-.1094),.90,abs_tol=.005)
assert math.isclose(math.exp(-.1094),.89637,abs_tol=5e-6)
f55,pf55=prob(0,5.5)
f65,pf65=prob(0,6.5)
m55,pm55=prob(1,5.5)
m65,pm65=prob(1,6.5)
for actual,rounded in [(f55,-.6072),(pf55,.35270),(f65,.9770),(pf65,.72651),(m55,-.7166),(pm55,.32814),(m65,.8676),(pm65,.70425),(pf65-pf55,.37381),(pm65-pf65,-.02227),(pm55-pf55,-.02456)]:
    assert math.isclose(actual,rounded,abs_tol=5e-5)
assert math.isclose(pf65/pf55,2.06,abs_tol=.005)
root=Path(__file__).resolve().parents[1]
source=(root/'research/content/cholesterol-and-heart-disease.md').read_text()
for number in ('4.87539','0.89637','0.35270','0.72651','0.37381','0.70425','-0.02227','0.32814','-0.02456'):
    assert number in source
page=root/'articles/cholesterol-and-heart-disease.qmd'
if page.exists():
    rendered=page.read_text()
    for preserved in ('cholesterol-band.png', 'q-35.qmd', '-9.3203', '-0.1094', '1.5842', 'title="Proof"'):
        assert preserved in rendered
