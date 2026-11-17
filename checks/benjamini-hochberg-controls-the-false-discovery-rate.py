from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
from fractions import Fraction as F
p=[F(4,1000),F(18,1000),F(21,1000),F(6,100),F(4,10)];q=F(1,20);m=5
threshold=[q*r/m for r in range(1,m+1)]
R=max([0]+[i for i,(pi,t) in enumerate(zip(p,threshold),1) if pi<=t])
assert R==3 and threshold==[F(1,100),F(2,100),F(3,100),F(4,100),F(5,100)]
assert F(900,1000)*q==F(45,1000)
assert abs(sum(1/i for i in range(1,1001))-7.49)<.005
# Exact integration for two independent Uniform null p-values: unit-square regions.
# Under the global null, any rejection iff min<=q/2 or both<=q.
area=(1-(1-q/2)**2)+(q-q/2)**2
assert area==q
assert F(3,20)==F(15,100)
printed=['0.004','0.045','3/20','0.15']

article=(ROOT/"articles"/"benjamini-hochberg-controls-the-false-discovery-rate.qmd").read_text()
for token in printed:
    assert token in article,("benjamini-hochberg-controls-the-false-discovery-rate",token)
questions=json.loads((ROOT/"research/self-checks.json").read_text())["benjamini-hochberg-controls-the-false-discovery-rate"]
assert len(questions) in (2,3)
assert article.count("## Check yourself {#check-yourself}") == 1
assert "Your turn" in article
print("benjamini-hochberg-controls-the-false-discovery-rate: numerical examples, self-checks and generated text verified")
