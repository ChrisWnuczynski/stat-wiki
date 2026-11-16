"""Independent arithmetic for the scalar conjugate-regression examples."""
import math
from pathlib import Path

def posterior(ys, a0=2, b0=3, m0=0, v0=1):
    n = len(ys)
    vn = 1/(1/v0+n)
    mn = vn*(m0/v0+sum(ys))
    an = a0+n/2
    bn = b0+(sum(y*y for y in ys)+m0*m0/v0-mn*mn/vn)/2
    return vn,mn,an,bn

assert posterior([2,4]) == (1/3,2,3,7)
assert 7/(3-1) == 3.5 and 7/(3+1) == 1.75
assert math.isclose(math.sqrt(7)/3, .88192, abs_tol=5e-6)
vn,mn,an,bn = posterior([1,3])
assert math.isclose(vn,1/3) and math.isclose(mn,4/3)
assert an == 3 and math.isclose(bn,16/3)
assert math.isclose(bn/(an-1),8/3)
assert math.isclose(bn/(an+1),4/3)
root=Path(__file__).resolve().parents[1]
source=(root/"research/content/normal-inverse-gamma-conjugacy.md").read_text()
for number in ("0.88192","3.5","1.75","16/3","2.667","1.333"):
    assert number in source
page=root/"articles/normal-inverse-gamma-conjugacy.qmd"
if page.exists():
    rendered=page.read_text()
    for old in ("ex-reg-nichisq", "ex-norm-nig", "q-58", 'title="Proof"'):
        assert old in rendered
