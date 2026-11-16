"""Check all new numerical examples and preserved ensemble formula."""
import math
from pathlib import Path

var=lambda n,rho,sigma2=1:sigma2*(rho+(1-rho)/n)
assert math.isclose(var(5,.3),.44,abs_tol=1e-12)
assert math.isclose(var(5,0),.20,abs_tol=1e-12)
assert math.isclose(var(4,.5),.625,abs_tol=1e-12)
assert math.isclose(var(4,0),.25,abs_tol=1e-12)
preds=(2,4,6)
avg=sum(preds)/3
assert avg==4
assert math.isclose(sum((p-5)**2 for p in preds)/3,11/3)
assert (avg-5)**2==1
assert math.isclose(11/3-1,8/3)
assert math.isclose(sum((p-avg)**2 for p in preds)/3,8/3)
root=Path(__file__).resolve().parents[1]
page=root/'articles/ensemble-method.qmd'
if page.exists():
    rendered=page.read_text()
    for value in ('0.44','0.20','0.625','0.25','11/3','8/3','500','title="Proof"','title="Answer"','ex-sl-13-6.qmd'):
        assert value in rendered,value
