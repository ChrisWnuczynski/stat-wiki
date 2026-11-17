"""Independent calculations and generated-output checks for this article."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
import numpy as np
Y=np.r_[np.zeros(500),np.ones(500)]
R=np.r_[np.ones(100),np.zeros(400),np.ones(400),np.zeros(100)]
N=len(Y);n=int(R.sum());delta=Y[R==1].mean()-Y.mean()
rho=np.corrcoef(R,Y)[0,1];sigma=Y.std()
assert abs(delta-.3)<1e-14 and abs(rho-.6)<1e-14
assert abs(delta-rho*sigma*np.sqrt((N-n)/n))<1e-14
weights=np.where(Y==0,5.,1.25)
assert np.average(Y[R==1],weights=weights[R==1])==.5
R2=np.r_[np.ones(100),np.zeros(400),np.ones(100),np.zeros(400)]
assert Y[R2==1].mean()==.5
assert abs(np.mean(R2*Y)-R2.mean()*Y.mean())<1e-14
# Error rates for the linked accuracy table.
assert (2+8)/60==1/6 and 2/20==.1 and 8/40==.2
assert 40/60==2/3

# Constant outcomes make correlation undefined, but preserve the covariance identity.
constant=np.full(1000,7.0)
selection=np.r_[np.ones(500),np.zeros(500)]
assert constant[selection==1].mean()-constant.mean()==0
assert np.mean((selection-selection.mean())*(constant-constant.mean()))==0
# A biased response law still has decreasing sampling variance as n increases.
response_values=np.array([0.,1.]);response_prob=np.array([.2,.8])
response_mean=response_prob@response_values
response_variance=response_prob@((response_values-response_mean)**2)
assert response_variance/1000 < response_variance/100
assert abs(response_mean-Y.mean()-delta)<1e-14
source=(ROOT/"research/content/sampling-bias.md").read_text()
article=(ROOT/"articles/sampling-bias.qmd").read_text().split("## See also",1)[0]
for needle in ['0.6(0.5)', '0.3', '400(1.25)']:
    assert needle in source and needle in article, needle
assert len(re.findall(r"\{\{cite:[^}]+\}\}", source))>=5
assert len(set(re.findall(r"\{\{cite:([^}]+)\}\}",source)))>=2
assert "nonconstant" in article
assert "A larger sample can reduce random fluctuation" in article
assert "Your turn" in article and 'collapse="true" title="Answer"' in article
assert "## Check yourself {#check-yourself}" in article
print("sampling-bias: calculations and article checks passed")
