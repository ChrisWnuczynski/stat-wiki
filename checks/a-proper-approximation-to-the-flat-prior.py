from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
from fractions import Fraction as F
assert F(6,40)==F(3,20)
assert 2*F(1,2)-F(1,2)**2==F(3,4)
assert 1-(2*F(1,4)-F(1,4)**2)==F(9,16)
assert F(2,200)==F(1,100)
from scipy.integrate import quad
L=lambda x:max(1-abs(x),0)
assert abs(quad(L,-1,1)[0]-1)<1e-12
for C in [.25,.5,1,2,10]:
 z=quad(L,-min(C,1),min(C,1))[0]
 assert abs(z-(2*C-C*C if C<=1 else 1))<1e-12
printed=['9/16','7/16','1/100']

# Deepened research calculations.
from fractions import Fraction as F
assert 2*F(1,2)-F(1,2)**2 == F(3,4)
assert 1-F(3,4) == F(1,4)
assert 2*F(1,4)-F(1,4)**2 == F(7,16)
assert 1-F(6,8) == F(1,4)
assert 1-F(4,5) == F(1,5)
assert F(6,40) == F(3,20)

article=(ROOT/"articles"/"a-proper-approximation-to-the-flat-prior.qmd").read_text()
for token in printed:
    assert token in article,("a-proper-approximation-to-the-flat-prior",token)
questions=json.loads((ROOT/"research/self-checks.json").read_text())["a-proper-approximation-to-the-flat-prior"]
assert len(questions) in (2,3)
assert article.count("## Check yourself {#check-yourself}") == 1
assert "Your turn" in article
print("a-proper-approximation-to-the-flat-prior: numerical examples, self-checks and generated text verified")
