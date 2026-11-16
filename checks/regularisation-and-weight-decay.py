"""Check the ridge and update arithmetic for weight decay."""
import math
from pathlib import Path

assert 8/4==2 and 8/(4+2)==4/3
assert math.isclose(4/3,1.33333,abs_tol=5e-6)
w,g,eps,lam=4,6,.1,.2
assert math.isclose(w-eps*g,3.4)
factor=1-eps*lam
assert math.isclose(factor,.98)
assert math.isclose(factor*w-eps*g,3.32)
M=.5
assert math.isclose(w-eps*M*(g+lam*w),3.66)
assert math.isclose(factor*w-eps*M*g,3.62)
w,g,eps,lam=-2,-3,.1,.4
factor=1-eps*lam
assert math.isclose(factor,.96)
assert math.isclose(factor*w-eps*g,-1.62)
assert math.isclose(w-eps*.5*(g+lam*w),-1.81)
assert math.isclose(factor*w-eps*.5*g,-1.77)
assert math.isclose((1/10)**2,1/100)
root=Path(__file__).resolve().parents[1]
source=(root/'research/content/regularisation-and-weight-decay.md').read_text()
for number in ('1.33333','0.98','3.4','3.32','3.66','3.62','0.96','-1.62','-1.81','-1.77'):
    assert number in source
page=root/'articles/regularisation-and-weight-decay.qmd'
if page.exists():
    rendered=page.read_text()
    for preserved in ('Krogh', 'Loshchilov', 'title="Proof"', 'Your turn'):
        assert preserved in rendered
