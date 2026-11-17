from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
from fractions import Fraction as F
from math import sqrt
risk=F(4,5)*F(1,10)+F(1,5)*F(2,5)
assert risk==F(4,25)
assert F(1,2)*F(1,10)+F(1,2)*F(2,5)==F(1,4)
assert f'{sqrt(float(risk*(1-risk)/400)):.6f}'=='0.018330'
assert F(4,5)*F(1,10)==F(1,5)*F(2,5)==F(2,25)
printed=['0.018330','4/25','1/4']

article=(ROOT/"articles"/"fixed-rule-error.qmd").read_text()
for token in printed:
    assert token in article,("fixed-rule-error",token)
questions=json.loads((ROOT/"research/self-checks.json").read_text())["fixed-rule-error"]
assert len(questions) in (2,3)
assert article.count("## Check yourself {#check-yourself}") == 1
assert "Your turn" in article
print("fixed-rule-error: numerical examples, self-checks and generated text verified")
