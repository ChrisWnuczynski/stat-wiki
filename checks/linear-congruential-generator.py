"""Recompute the worked calculations and inspect the generated article."""
from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
source = (root / "research" / "content" / (Path(__file__).stem + ".md")).read_text()
article = (root / "articles" / (Path(__file__).stem + ".qmd")).read_text()
body = article.split("## See also", 1)[0]
assert len(re.findall(r"\{\{cite:", source)) >= 5
assert len(set(re.findall(r"\{\{cite:([^}]+)", source))) >= 2
assert "Your turn" in body and 'collapse="true"' in body

from fractions import Fraction as F
def cycle(a,c,m):
    x=0;result=[]
    while x not in result:
        result.append(x);x=(a*x+c)%m
    return result,x
full,end=cycle(5,1,16)
assert full==[0,1,6,15,12,13,2,11,8,9,14,7,4,5,10,3]
assert end==0 and len(full)==16
short,end=cycle(3,1,16)
assert short==[0,1,4,13,8,9,12,5] and end==0
assert sum(F(x,16) for x in full)/16==F(15,32)
assert sum(F(2*x+1,32) for x in full)/16==F(1,2)
assert [F(x,16) for x in full[1:4]]==[F(1,16),F(3,8),F(15,16)]
assert '0.46875' in body and '0.9375' in body


# Parallel-line relation for a multiplicative congruential generator.
for x in range(16):
    next_x=(5*x)%16
    relation=F(next_x,16)-5*F(x,16)
    assert relation.denominator==1
assert F(10)+5*F(2,5)==12
from math import exp,log
for x in [.1,1.,3.]:
    assert abs(-log(exp(-10*x))/10-x)<1e-12

# Eight-state cycle in the interpretation, and a noninvertible transient.
x=1;eight=[]
for _ in range(8):
    eight.append(x);x=(5*x+1)%8
assert eight==[1,6,7,4,5,2,3,0] and x==1
x=1;transient=[]
for _ in range(5):
    transient.append(x);x=2*x%8
assert transient==[1,2,4,0,0]

print("linear-congruential-generator checks passed")
