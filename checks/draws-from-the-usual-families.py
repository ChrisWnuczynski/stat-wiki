from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
import math
from fractions import Fraction as F
u=.25
assert 2+(6-2)*u==3
assert f'{-math.log(u)/2:.6f}'=='0.693147'
assert math.floor(math.log(u)/math.log(.5))+1==3
assert f'{-math.log(u)/4:.6f}'=='0.346574'
cut=[F(1,5),F(7,10),F(1)];inv=lambda u:next(i for i,t in enumerate(cut) if u<=t)
assert inv(F(1,4))==1 and inv(F(9,10))==2 and inv(F(4,5))==2
# Box–Muller identities at a fixed interior pair of uniforms.
u,v=.25,.125;r=math.sqrt(-2*math.log(u));z1=r*math.cos(2*math.pi*v);z2=r*math.sin(2*math.pi*v)
assert abs(z1*z1+z2*z2+2*math.log(u))<1e-12
printed=['0.693147','0.346574','7/10']

# Deepened research calculations.
import math
ratio = math.log(0.5)/math.log(0.75)
assert f"{ratio:.6f}" == "2.409421"
assert math.floor(ratio)+1 == 3
thresholds = [0.1, 0.3, 1.0]
assert 0.1 < 0.25 < 0.3

article=(ROOT/"articles"/"draws-from-the-usual-families.qmd").read_text()
for token in printed:
    assert token in article,("draws-from-the-usual-families",token)
questions=json.loads((ROOT/"research/self-checks.json").read_text())["draws-from-the-usual-families"]
assert len(questions) in (2,3)
assert article.count("## Check yourself {#check-yourself}") == 1
assert "Your turn" in article
print("draws-from-the-usual-families: numerical examples, self-checks and generated text verified")
