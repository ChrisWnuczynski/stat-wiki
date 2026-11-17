"""Check Welch moment matching, quantiles and standard-error contributions."""
from pathlib import Path
from fractions import Fraction as F
from math import sqrt,isclose
from scipy.stats import t
import re
root=Path(__file__).resolve().parents[1]
a,b=F(4,10),F(36,20)
df=(a+b)**2/(a*a/9+b*b/19);se=sqrt(a+b);stat=3/se
assert round(float(df),4)==25.7031 and round(se,5)==1.48324
assert round(stat,5)==2.02260
assert round(2*t.sf(stat,float(df)),5)==.05363
width=t.ppf(.975,float(df))*se
assert round(3-width,4)==-.0506 and round(3+width,4)==6.0506
assert b/(a+b)==F(9,11)
assert round(sqrt((a+b)/2),5)==1.04881
assert round(3/sqrt((a+b)/2),5)==2.86039
assert isclose(2*float(a+b)**2/float(df),2*float(a*a/9+b*b/19))
for n1 in [2,5,10,30]:
    for n2 in [2,7,20,40]:
        for ratio in [F(1,100),F(1,2),F(1),F(10),F(1000)]:
            nu=(ratio+1)**2/(ratio**2/(n1-1)+F(1,n2-1))
            assert min(n1-1,n2-1)<=nu<=n1+n2-2
assert 80-1==79 and min(100,80-1)==79
body=(root/"articles/behrens-fisher-problem.qmd").read_text().split("## See also",1)[0]
for text in ["25.7031","2.02260","0.05363","9/11","Your turn","## Check yourself {#check-yourself}"]:
    assert text in body,text
assert len(re.findall('class="cite-ref"',body))>=5
for q in ["ex-sl-02-6","ex-sl-02-7"]:assert f"../questions/{q}.qmd" in body
print("behrens-fisher-problem: moment matching, t calibration and article checks passed")
