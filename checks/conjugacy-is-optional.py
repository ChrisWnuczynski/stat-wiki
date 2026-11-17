from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
from fractions import Fraction as F
import sympy as s
from scipy.integrate import quad
from scipy.special import expit
from scipy.stats import norm
x=s.symbols('x');prior=s.Rational(1,2)+s.Rational(3,2)*x**2
z=s.integrate(x**2*prior,(x,0,1));m=s.integrate(x**3*prior,(x,0,1))/z
assert z==s.Rational(7,15) and m==s.Rational(45,56)
assert F(1,3)/(F(1,3)+F(3,5))==F(5,14)
assert F(3,5)/(F(1,3)+F(3,5))==F(9,14)
assert f'{float(m):.6f}'=='0.803571'
for b in [.1,1,2]:
 integ=quad(lambda t:__import__('math').exp(-abs(t-.5)/b),0,1,points=[.5])[0]
 assert abs(integ-2*b*(1-__import__('math').exp(-1/(2*b))))<1e-12
# Numerical claims in the embedded logit-normal example.
from scipy.optimize import minimize_scalar
mean=quad(lambda z:expit(z)*norm.pdf(z,loc=1),-12,14)[0]
mode=expit(minimize_scalar(lambda z:-(norm.logpdf(z,loc=1)-__import__('math').log(expit(z)*(1-expit(z)))),bounds=(-5,5),method='bounded').x)
assert abs(mean-.6967)<.0001 and abs(mode-.84)<.01
printed=['45/56','0.803571','7/15']

# Deepened research calculations.
from fractions import Fraction as F
assert F(1,2)*F(1,3) + F(1,2)*F(3,5) == F(7, 15)
assert F(9, 2)*F(2, 9) == 1
assert F(2, 7) == F(2, 2+5)
assert F(3, 11) == F(3, 3+8)
assert F(3, 5) == F(3, 3+2)

article=(ROOT/"articles"/"conjugacy-is-optional.qmd").read_text()
for token in printed:
    assert token in article,("conjugacy-is-optional",token)
questions=json.loads((ROOT/"research/self-checks.json").read_text())["conjugacy-is-optional"]
assert len(questions) in (2,3)
assert article.count("## Check yourself {#check-yourself}") == 1
assert "Your turn" in article
print("conjugacy-is-optional: numerical examples, self-checks and generated text verified")
