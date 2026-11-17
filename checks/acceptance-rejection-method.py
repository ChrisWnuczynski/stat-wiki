from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
from fractions import Fraction as F
import sympy as s
x=s.symbols('x',real=True);f=6*x*(1-x)
assert s.integrate(f,(x,0,1))==1
assert s.simplify(f-(s.Rational(3,2)-6*(x-s.Rational(1,2))**2))==0
assert f.subs(x,F(1,4))/F(3,2)==s.Rational(3,4)
assert F(4,5)>F(3,4)
assert F(3,2)*(F(3,2)-1)==F(3,4)
assert 2*F(3,2)==3 and 2*2==4
printed=['3/4','2/3']

article=(ROOT/"articles"/"acceptance-rejection-method.qmd").read_text()
for token in printed:
    assert token in article,("acceptance-rejection-method",token)
questions=json.loads((ROOT/"research/self-checks.json").read_text())["acceptance-rejection-method"]
assert len(questions) in (2,3)
assert article.count("## Check yourself {#check-yourself}") == 1
assert "Your turn" in article
print("acceptance-rejection-method: numerical examples, self-checks and generated text verified")
