from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
from fractions import Fraction as F
import sympy as s
x=[-1,0,2];p=[F(1,4),F(1,2),F(1,4)]
E=lambda f:sum(pi*f(xi) for pi,xi in zip(p,x))
assert E(lambda t:t)==F(1,4) and E(lambda t:t*t)==F(5,4)
assert E(lambda t:t*t)-E(lambda t:t)**2==F(19,16)
assert E(abs)==F(3,4) and E(lambda t:max(t-1,0))==F(1,4)
u=s.symbols('u');assert s.integrate(u*u,(u,0,1))==s.Rational(1,3)
assert F(1,3)-F(1,4)==F(1,12)
assert E(lambda t:int(t>0))==F(1,4)
printed=['19/16','5/4','3/4']

# Deepened research calculations.
from fractions import Fraction as Fd
import sympy as sp
devs = [Fd(5,4), Fd(1,4), Fd(7,4)]
weights = [Fd(1,4), Fd(1,2), Fd(1,4)]
assert sum(d*w for d,w in zip(devs, weights)) == Fd(7,8)
t = sp.symbols("t", positive=True)
assert sp.integrate(t*sp.exp(-t), (t, 0, sp.oo)) == 1
assert sp.integrate(t**2*sp.exp(-t), (t, 0, sp.oo)) == 2
assert Fd(2,3)*6 == 4 and Fd(2,3)*36 == 24 and 24-16 == 8

article=(ROOT/"articles"/"expectation-of-a-function.qmd").read_text()
for token in printed:
    assert token in article,("expectation-of-a-function",token)
questions=json.loads((ROOT/"research/self-checks.json").read_text())["expectation-of-a-function"]
assert len(questions) in (2,3)
assert article.count("## Check yourself {#check-yourself}") == 1
assert "Your turn" in article
print("expectation-of-a-function: numerical examples, self-checks and generated text verified")
