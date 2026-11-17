from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
from fractions import Fraction as F
from math import isclose
adj=lambda n,p,sse,sst:1-F(sse)/F(n-p-1)/(F(sst)/F(n-1))
assert f'{float(adj(20,2,40,100)):.6f}'=='0.552941'
assert adj(20,3,38,100)==F(439,800)
assert f'{float(F(2)/(F(38)/16)):.6f}'=='0.842105'
assert adj(20,3,37,100)==F(897,1600)
assert adj(20,2,85,100)==F(1,20)
assert adj(10,1,F(44,5),9)==-F(1,10)
assert 20-3-1==16
# Rounded summary in the embedded survey example.
assert abs(float(adj(100,2,F(5699,10000),1))-0.4184)<0.0001
printed=['0.552941','0.54875','0.842105','0.560625']

from scipy.stats import t as student_t, f as fisher_f
n,df=100,97
for estimate,se,tprinted,ptarget in [(132.2677,5.2473,25.207,None),(.5304,.1962,2.703,.0081),(.3744,.0572,6.546,2.82e-9)]:
 ratio=estimate/se
 assert abs(ratio-tprinted)<.002
 if ptarget is not None:
  p=2*student_t.sf(abs(ratio),df)
  assert abs(p-ptarget)<max(.0001,ptarget*.01)
for estimate,se,lo,hi in [(132.2677,5.2473,121.8533072,142.6821199),(.5304,.1962,.1410087,.9198251),(.3744,.0572,.2608887,.4879514)]:
 half=student_t.ppf(.975,df)*se
 assert abs((estimate-half)-lo)<.0002 and abs((estimate+half)-hi)<.0002
R2=.4301;Fstat=R2/2/((1-R2)/97)
assert abs(Fstat-36.61)<.02
# Propagate the stated four-decimal rounding of R-squared.
rlo,rhi=.4301-.00005,.4301+.00005
flo,fhi=rlo/2/((1-rlo)/97),rhi/2/((1-rhi)/97)
assert fisher_f.sf(fhi,2,97)<=1.429e-12<=fisher_f.sf(flo,2,97)

article=(ROOT/"articles"/"adjusted-r-squared.qmd").read_text()
for token in printed:
    assert token in article,("adjusted-r-squared",token)
questions=json.loads((ROOT/"research/self-checks.json").read_text())["adjusted-r-squared"]
assert len(questions) in (2,3)
assert article.count("## Check yourself {#check-yourself}") == 1
assert "Your turn" in article
print("adjusted-r-squared: numerical examples, self-checks and generated text verified")
