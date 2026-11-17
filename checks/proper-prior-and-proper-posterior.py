"""Independently integrate the prior/posterior examples and inspect the article."""
from pathlib import Path
import re
import sympy as sp

root = Path(__file__).resolve().parents[1]
p = sp.symbols("p", positive=True)
flat = p**2 * (1-p)**3
haldane = p * (1-p)**2
assert sp.integrate(flat, (p, 0, 1)) == sp.Rational(1, 60)
assert sp.integrate(haldane, (p, 0, 1)) == sp.Rational(1, 12)
assert sp.integrate(p*60*flat, (p, 0, 1)) == sp.Rational(3, 7)
assert sp.integrate(p*12*haldane, (p, 0, 1)) == sp.Rational(2, 5)
eps = sp.symbols("eps", positive=True)
primitive = -sp.log(1-p)-p-p**2/2-p**3/3-p**4/4
assert sp.simplify(sp.diff(primitive,p)-p**4/(1-p)) == 0
assert sp.limit(primitive.subs(p,1-eps),eps,0,dir="+") == sp.oo
assert (1+1, 1+5-1) == (2, 5)
assert (1, 5-1) == (1, 4)
# The inverse-gamma integral is positive and finite when both parameters are positive.
v = sp.symbols("v", positive=True)
assert sp.integrate(v**-2*sp.exp(-1/v), (v, 0, sp.oo)) == 1
assert sp.integrate(v**-2, (v, 0, sp.oo)) == sp.oo
body = (root/"articles/proper-prior-and-proper-posterior.qmd").read_text()
before_refs = body.split("## See also", 1)[0]
for text in ["1/60", "1/12", "3/7", "2/5", "Your turn", "## Check yourself {#check-yourself}"]:
    assert text in before_refs, text
assert len(re.findall('class="cite-ref"', before_refs)) >= 5
for qid in ["ex-improper-normal", "q-43"]:
    assert f"../questions/{qid}.qmd" in before_refs
print("proper-prior-and-proper-posterior: integrals and article checks passed")
