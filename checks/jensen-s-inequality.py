"""Check new Jensen examples and preserved source inequalities."""
import math
from pathlib import Path

mean=.25*1+.75*3
second=.25*1**2+.75*3**2
assert mean==2.5 and second==7
assert mean**2==6.25 and second-mean**2==.75
elog=.75*math.log(3)
assert math.isclose(elog,.82396,abs_tol=5e-6)
assert math.isclose(math.log(mean),.91629,abs_tol=5e-6)
mean2=(1+4)/2
square2=(1+16)/2
assert mean2==2.5 and square2==8.5
assert square2-mean2**2==2.25
assert math.isclose(math.log(4)/2,.69315,abs_tol=5e-6)
assert math.isclose(math.log(mean2),.91629,abs_tol=5e-6)
assert ((-2+1)/2)**3 > ((-2)**3+1**3)/2
for r in [0,.1,.25,.5]:
    assert 2*r*(1-r)<=2*r
root=Path(__file__).resolve().parents[1]
source=(root/'research/content/jensen-s-inequality.md').read_text()
for number in ('2.5','6.25','0.75','0.82396','0.91629','8.5','2.25','0.69315'):
    assert number in source
page=root/'articles/jensen-s-inequality.qmd'
if page.exists():
    rendered=page.read_text()
    for preserved in ('Cover–Hart bound', 'Gini index', 'title="Proof"'):
        assert preserved in rendered
