from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
from fractions import Fraction as F
groups=[[F(1),F(3)],[F(4),F(5),F(6)]]
means=[sum(g)/len(g) for g in groups];grand=sum(map(sum,groups))/5
within=sum(sum((y-m)**2 for y in g) for g,m in zip(groups,means))
between=sum(len(g)*(m-grand)**2 for g,m in zip(groups,means))
total=sum((y-grand)**2 for g in groups for y in g)
assert means==[2,5] and grand==F(19,5)
assert within==4 and between==F(54,5) and total==F(74,5)
assert total==within+between and between/(within/3)==F(81,10)
assert sum((y+10-(grand+10))**2 for g in groups for y in g)==total
printed=['10.8','14.8','8.1','3.8']

# Deepened research calculations.
from fractions import Fraction as F
grand = F(0+2+6, 3)
assert grand == F(8, 3)
ssw = (0-1)**2 + (2-1)**2 + (6-6)**2
ssb = 2*(1-grand)**2 + 1*(6-grand)**2
assert ssw == 2 and ssb == F(50, 3) and ssw + ssb == F(56, 3)
assert (5*1 + 1*4 + 4*10)/10 == 4.9
assert abs(10.8/(4/3) - 8.1) < 1e-12

article=(ROOT/"articles"/"anova-sum-of-squares-decomposition.qmd").read_text()
for token in printed:
    assert token in article,("anova-sum-of-squares-decomposition",token)
questions=json.loads((ROOT/"research/self-checks.json").read_text())["anova-sum-of-squares-decomposition"]
assert len(questions) in (2,3)
assert article.count("## Check yourself {#check-yourself}") == 1
assert "Your turn" in article
print("anova-sum-of-squares-decomposition: numerical examples, self-checks and generated text verified")
