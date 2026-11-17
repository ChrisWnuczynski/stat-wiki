"""Enumerate joint masses, conditionals, expectations, and transformed outcomes."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
p={(0,0):F(1,10),(0,1):F(2,10),(1,0):F(3,10),(1,1):F(4,10)}
assert sum(p.values())==1
ex=sum(x*w for (x,y),w in p.items());ey=sum(y*w for (x,y),w in p.items());exy=sum(x*y*w for (x,y),w in p.items())
assert (ex,ey,exy)==(F(7,10),F(6,10),F(4,10))
assert exy-ex*ey==F(-1,50)
assert p[1,0]/(p[0,0]+p[1,0])==F(3,4)
assert p[1,1]/(p[0,1]+p[1,1])==F(2,3)
assert sum(w for (x,y),w in p.items() if x or y)==F(9,10)
assert p[0,0]/(p[0,0]+p[1,1])==F(1,5)
larger={(2,3):F(1,10),(2,6):F(1,10),(5,1):F(2,10),(6,3):F(2,10),(6,6):F(1,10),(6,8):F(3,10)}
assert sum(x*x*y*w for (x,y),w in larger.items())==F(691,5)
transformed={}
for u,v in product([1,-1],repeat=2):
    weight=(F(1,4) if u==1 else F(3,4))*(F(1,4) if v==1 else F(3,4))
    key=(u//v,u+v);transformed[key]=transformed.get(key,F(0))+weight
assert transformed=={(1,2):F(1,16),(-1,0):F(6,16),(1,-2):F(9,16)}
ex=sum(x*w for (x,y),w in transformed.items());ey=sum(y*w for (x,y),w in transformed.items());exy=sum(x*y*w for (x,y),w in transformed.items())
assert (ex,ey,exy,exy-ex*ey)==(F(1,4),-1,-1,F(-3,4))
body=(root/"articles/joint-probability-mass-function.qmd").read_text().split("## See also",1)[0]
for text in ["0.42","-0.02","691/5","6/16","Your turn","## Check yourself {#check-yourself}"]:
    assert text in body,text
assert len(re.findall('class="cite-ref"',body))>=5
for q in ["ex-prob-joint-table","ex-prob-sign-covariance"]:assert f"../questions/{q}.qmd" in body
print("joint-probability-mass-function: exact enumeration and article checks passed")
