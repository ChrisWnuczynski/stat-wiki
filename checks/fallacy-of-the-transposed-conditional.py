from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
from fractions import Fraction as F
ppv=lambda pi,s=F(9,10),f=F(1,20):s*pi/(s*pi+f*(1-pi))
assert ppv(F(1,100))==F(2,13)
assert f'{float(ppv(F(1,100))):.6f}'=='0.153846'
assert ppv(F(1,10))==F(2,3)
assert F(9900,20)==495 and 90+495==585
assert F(1,10)/F(1,2)==F(1,5) and F(1,10)/F(1,5)==F(1,2)
assert ppv(F(1,100))<ppv(F(1,10))
# The rounded source screening example uses prevalence .01, sensitivity .95 and FPR .10.
assert abs(float(F(95,100)*F(1,100)/(F(95,100)*F(1,100)+F(1,10)*F(99,100)))-.087)<.001
printed=['0.153846','2/13','495']

# Deepened research calculations.
from fractions import Fraction as F
assert F(2,10)/F(5,10) == F(2, 5)  # 0.2/0.5 = 0.4
assert F(2,10)/F(4,10) == F(1, 2)
def ppv(pi, s=F(9,10), f=F(5,100)):
    return s*pi / (s*pi + f*(1-pi))
assert ppv(F(1,10)) == F(2, 3)
assert ppv(F(1,100)) == F(2, 13)
assert F(9,10)/F(5,100) == 18
assert F(18, 99) == F(2, 11)
assert F(2,11)/(1+F(2,11)) == F(2, 13)
assert F(90 + 9900 - 495, 10000) == F(9495, 10000)

article=(ROOT/"articles"/"fallacy-of-the-transposed-conditional.qmd").read_text()
for token in printed:
    assert token in article,("fallacy-of-the-transposed-conditional",token)
questions=json.loads((ROOT/"research/self-checks.json").read_text())["fallacy-of-the-transposed-conditional"]
assert len(questions) in (2,3)
assert article.count("## Check yourself {#check-yourself}") == 1
assert "Your turn" in article
print("fallacy-of-the-transposed-conditional: numerical examples, self-checks and generated text verified")
