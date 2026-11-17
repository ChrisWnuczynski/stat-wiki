from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
from fractions import Fraction as F
from math import factorial
import itertools
p=[F(1,2),F(1,3),F(1,6)];x=[2,1,1];n=4
coef=factorial(n)
for k in x:coef//=factorial(k)
assert coef==12
prob=F(coef)
for pi,xi in zip(p,x):prob*=pi**xi
assert prob==F(1,6) and -n*p[0]*p[1]==-F(2,3)
assert n*p[0]==2 and n*p[1]==F(4,3)
assert [F(t,7) for t in [3,2,2]]==[F(3,7),F(2,7),F(2,7)]
assert F(3,8)==F(2+1,7+1) and F(1,7)==F(0+1,4+3)
printed=['1/6','-2/3','3/7','3/8']

article=(ROOT/"articles"/"categorical-and-multinomial-models.qmd").read_text()
for token in printed:
    assert token in article,("categorical-and-multinomial-models",token)
questions=json.loads((ROOT/"research/self-checks.json").read_text())["categorical-and-multinomial-models"]
assert len(questions) in (2,3)
assert article.count("## Check yourself {#check-yourself}") == 1
assert "Your turn" in article
print("categorical-and-multinomial-models: numerical examples, self-checks and generated text verified")
