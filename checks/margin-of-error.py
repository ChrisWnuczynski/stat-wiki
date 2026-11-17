"""Recompute normal margins, integer sample sizes and fixed-width scaling."""
from pathlib import Path
from math import ceil,sqrt,isclose
from fractions import Fraction
from scipy.stats import norm,t
import re
root=Path(__file__).resolve().parents[1]
z=norm.ppf(.975);margin=z*12/sqrt(64)
assert isclose(margin,2.939945976810081)
assert round(100-margin,4)==97.0601 and round(100+margin,4)==102.9399
assert ceil((z*12)**2)==554 and ceil((z*12/2)**2)==139
assert z*12/sqrt(553)>1 and z*12/sqrt(554)<=1
assert z*12/sqrt(256)==margin/2
assert ceil(100*((Fraction("82.5")-Fraction("59.3"))/2)**2)==13456
assert isclose(4*(7.39/2)**2,54.6121) and ceil(4*(7.39/2)**2)==55
assert 7.39*sqrt(4/54)>2 and 7.39*sqrt(4/55)<2
pilot_to_normal=13456*(z/t.ppf(.975,99))**2
assert round(pilot_to_normal,4)==13129.0665 and ceil(pilot_to_normal)==13130
body=(root/"articles/margin-of-error.qmd").read_text().split("## See also",1)[0]
for text in ["2.939946","554","139","13456","54.6121","Your turn","## Check yourself {#check-yourself}"]:
    assert text in body,text
assert len(re.findall('class="cite-ref"',body))>=5
for q in ["ex-da-pilot-width","ex-da-sleep-sample-size"]:assert f"../questions/{q}.qmd" in body
print("margin-of-error: quantiles, widths, sample sizes and article checks passed")
