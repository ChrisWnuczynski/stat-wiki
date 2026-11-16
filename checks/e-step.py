"""Check printed E-step quantities and retained baseline material."""
import math
from pathlib import Path

phi=lambda z: math.exp(-z*z/2)/math.sqrt(2*math.pi)
r0=phi(0)/(phi(0)+phi(2))
r2=phi(2)/(phi(2)+phi(0))
assert math.isclose(phi(0),.39894,abs_tol=5e-6)
assert math.isclose(phi(2),.05399,abs_tol=5e-6)
assert math.isclose(r0,.880797,abs_tol=5e-7)
assert math.isclose(r2,.119203,abs_tol=5e-7)
assert math.isclose(r0+r2,1,abs_tol=1e-12)
assert math.isclose(.8/(.8+.2),.8)
assert math.isclose(phi(0)/(phi(0)+phi(3)),.989013,abs_tol=5e-7)
root=Path(__file__).resolve().parents[1]
page=root/'articles/e-step.qmd'
if page.exists():
    rendered=page.read_text()
    for value in ('0.880797','0.119203','0.39894','0.05399','0.989','title="Proof"','title="Answer"'):
        assert value in rendered,value
