from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
from fractions import Fraction as F
from math import comb,isqrt
p=F(7,10)
assert 2*p*(1-p)==F(21,50)
vote=sum(F(comb(3,j))*p**j*(1-p)**(3-j) for j in [2,3])
risk=p*(1-vote)+(1-p)*vote
assert vote==F(98,125) and risk==F(483,1250)
assert float(vote)==.784 and float(risk)==.3864
assert float(F(31,1000))==.031 and F(500,1000)==F(1,2)
for n in [100,10000,1000000]:
 k=isqrt(n);k-=1-k%2
 assert 0<k<n and k%2==1
printed=['0.42','0.784','0.3864','0.3']

article=(ROOT/"articles"/"bayes-consistency-of-nearest-neighbours.qmd").read_text()
for token in printed:
    assert token in article,("bayes-consistency-of-nearest-neighbours",token)
questions=json.loads((ROOT/"research/self-checks.json").read_text())["bayes-consistency-of-nearest-neighbours"]
assert len(questions) in (2,3)
assert article.count("## Check yourself {#check-yourself}") == 1
assert "Your turn" in article
print("bayes-consistency-of-nearest-neighbours: numerical examples, self-checks and generated text verified")
