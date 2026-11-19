"""Recompute confusion-matrix rates, prevalence transport and linked exercises."""
from fractions import Fraction as F
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
tp,fn,fp,tn = 72,8,12,108
n = tp+fn+fp+tn
assert n == 200
assert F(tp,tp+fn) == F(tn,tn+fp) == F(tp+tn,n) == F(9,10)
assert F(tp,tp+fp) == F(6,7)
assert F(tn,tn+fn) == F(27,29)
assert F(tp+fn,n)*F(fn,tp+fn)+F(tn+fp,n)*F(fp,tn+fp) == F(1,10)
prevalence = F(1,20)
ppv = F(9,10)*prevalence/(F(9,10)*prevalence+F(1,10)*(1-prevalence))
assert ppv == F(9,28)
assert round(float(ppv),4) == .3214
assert F(12+16,200) == F(14,100)
assert F(120,200)*F(12,120)+F(80,200)*F(16,80) == F(14,100)
assert F(18+32,60) == F(5,6)
assert F(40,60) == F(2,3)
body = (root/"articles/confusion-matrix.qmd").read_text().split("## See also",1)[0]
for text in ["0.8571", "0.3214", "0.9310", "Your turn", "## Check yourself {#check-yourself}"]:
    assert text in body, text
assert len(re.findall('class="cite-ref"',body)) >= 5
for qid in ["depth-confusion-matrix-q1", "depth-confusion-matrix-q2"]:
    assert f"../questions/{qid}.qmd" in body
print("confusion-matrix: rates and article checks passed")
