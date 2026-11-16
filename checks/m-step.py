"""Verify printed M-step arithmetic and preserved updates."""
import math
from pathlib import Path

x=(0,2)
r1=(.8,.4)
r2=tuple(1-r for r in r1)
n1=sum(r1);n2=sum(r2)
assert math.isclose(n1,1.2)
assert math.isclose(n2,.8)
assert math.isclose(n1/2,.6)
assert math.isclose(n2/2,.4)
mu1=sum(r*v for r,v in zip(r1,x))/n1
mu2=sum(r*v for r,v in zip(r2,x))/n2
assert math.isclose(mu1,2/3)
assert math.isclose(mu1,.66667,abs_tol=5e-6)
assert math.isclose(mu2,1.5)
v1=sum(r*(v-mu1)**2 for r,v in zip(r1,x))/n1
v2=sum(r*(v-mu2)**2 for r,v in zip(r2,x))/n2
assert math.isclose(v1,8/9)
assert math.isclose(v1,.88889,abs_tol=5e-6)
assert math.isclose(v2,3/4)
assert math.isclose(v2,.75)
t1=(.75,.25);t2=(.25,.75)
assert math.isclose(sum(t1)/2,.5)
assert math.isclose(sum(t2)/2,.5)
assert math.isclose(sum(a*b for a,b in zip(t1,x))/sum(t1),.5)
assert math.isclose(sum(a*b for a,b in zip(t2,x))/sum(t2),1.5)
root=Path(__file__).resolve().parents[1]
page=root/'articles/m-step.qmd'
if page.exists():
    rendered=page.read_text()
    for value in ('0.66667','0.88889','0.75','1.5','1.2','0.8','title="Proof"','title="Answer"','ex-sl-05-3.qmd'):
        assert value in rendered,value
