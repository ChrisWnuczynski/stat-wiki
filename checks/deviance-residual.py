"""Check Poisson likelihood differences, residual sums and local expansion."""
from pathlib import Path
from math import log,sqrt,isclose
import sympy as s
import re
root=Path(__file__).resolve().parents[1]
def dev(y,mu):return 2*((y*log(y/mu) if y else 0)-(y-mu))
ys=[0,2,5];mus=[1,2,3]
ds=[dev(y,mu) for y,mu in zip(ys,mus)]
res=[(1 if y>mu else -1 if y<mu else 0)*sqrt(d) for y,mu,d in zip(ys,mus,ds)]
assert ds[:2]==[2,0] and round(ds[2],6)==1.108256
assert [round(v,6) for v in res]==[-1.414214,0,1.052737]
assert isclose(sum(v*v for v in res),sum(ds)) and round(sum(ds),6)==3.108256
assert dev(0,4)==8 and round(-sqrt(8),6)==-2.828427
delta,mu=s.symbols("delta mu",positive=True)
expr=2*((mu+delta)*s.log((mu+delta)/mu)-delta)
assert s.series(expr,delta,0,4).removeO()==delta**2/mu-delta**3/(3*mu**2)
assert isclose(1.016**2,1.032256) and round(354.97+1.016**2,4)==356.0023
body=(root/"articles/deviance-residual.qmd").read_text().split("## See also",1)[0]
for text in ["1.108256","3.108256","-2.828427","Your turn","## Check yourself {#check-yourself}"]:
    assert text in body,text
assert len(re.findall('class="cite-ref"',body))>=5
for q in ["c-29","ex-sl-10-6"]:assert f"../questions/{q}.qmd" in body
print("deviance-residual: likelihood contributions, local series and article checks passed")
