"""Enumerate exact critical-region probabilities and power."""
from fractions import Fraction as F
from math import comb,isclose
from pathlib import Path
from scipy.stats import binom
import re
root=Path(__file__).resolve().parents[1]
def tail(n,c,p):return sum(F(comb(n,k))*p**k*(1-p)**(n-k) for k in range(c,n+1))
assert tail(10,9,F(1,2))==F(11,1024)
assert tail(10,8,F(1,2))==F(56,1024)
assert tail(10,9,F(1,2))<=F(1,20)<tail(10,8,F(1,2))
assert 2*tail(10,9,F(1,2))==F(22,1024)
assert float(F(11,1024))==.0107421875 and float(F(56,1024))==.0546875
assert float(F(22,1024))==.021484375
assert sum(F(comb(10,k),2**10) for k in [0,1])==F(11,1024)
for p in [F(3,5),F(9,10)]:assert isclose(float(tail(15,13,p)),binom.sf(12,15,float(p)))
assert round(float(tail(15,13,F(3,5))),7)==.0271140
assert round(float(tail(15,13,F(9,10))),6)==.815939
body=(root/"articles/binomial-test.qmd").read_text().split("## See also",1)[0]
for text in ["11/1024","56/1024","22/1024","0.815939","Your turn","## Check yourself {#check-yourself}"]:
    assert text in body,text
assert len(re.findall('class="cite-ref"',body))>=5
for q in ["depth-binomial-test-q1", "depth-binomial-test-q2"]:assert f"../questions/{q}.qmd" in body
print("binomial-test: exact tails, critical region, power and article checks passed")
