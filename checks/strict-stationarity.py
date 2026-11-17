"""Recompute the finite-law and dependence examples in strict stationarity."""
from pathlib import Path
from itertools import product
import re
import sympy as sp

root = Path(__file__).resolve().parents[1]
even = {-1: sp.Rational(1,2), 1: sp.Rational(1,2)}
odd = {0: sp.Rational(1,2), -sp.sqrt(2): sp.Rational(1,4), sp.sqrt(2): sp.Rational(1,4)}
def moment(law, k):
    return sp.simplify(sum(w*x**k for x,w in law.items()))
assert moment(even,1) == moment(odd,1) == 0
assert moment(even,2) == moment(odd,2) == 1
assert moment(even,4) == 1 and moment(odd,4) == 2
assert even.get(0,0) == 0 and odd[0] == sp.Rational(1,2)
assert sum(x*y*px*py for (x,px),(y,py) in product(even.items(),odd.items())) == 0
# Uniform random phase of the alternating deterministic chain.
for k in range(1,6):
    law = {tuple((phase+j)%2 for j in range(k)):sp.Rational(1,2) for phase in [0,1]}
    shifted = {tuple((phase+j+1)%2 for j in range(k)):sp.Rational(1,2) for phase in [0,1]}
    assert law == shifted
for z in [0,1]:
    assert sum([z]*17)/17 == z
body = (root/"articles/strict-stationarity.qmd").read_text().split("## See also",1)[0]
for text in ["1/2", "fourth moment", "Your turn", "## Check yourself {#check-yourself}"]:
    assert text in body, text
assert len(re.findall('class="cite-ref"',body)) >= 5
for qid in ["depth-strict-finite-shift", "depth-stationarity-changing-laws"]:
    assert f"../questions/{qid}.qmd" in body
print("strict-stationarity: moments, shifted laws, and article checks passed")
