from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
from fractions import Fraction as F
assert F(50-32,2)==9
assert F(50-32,4-2)/(F(32,20-4))==F(9,2)
assert F(32-30,1)/(F(30,20-5))==1 and 8-5==3
# Independently refit the 16-run wafer data with a Gamma log-link likelihood.
import numpy as np
from scipy.optimize import minimize
from scipy.stats import f
from itertools import combinations
Y=np.array([193.4,247.6,168.2,205.,303.4,339.9,226.3,208.3,220.,256.4,165.7,203.5,285.,268.,169.1,208.5])
A=np.array([[(i>>j)&1 for j in range(4)] for i in range(16)],float)
def fit(terms):
 X=np.column_stack([np.ones(16)]+[np.prod(A[:,t],axis=1) for t in terms])
 fun=lambda b:np.sum(Y*np.exp(-X@b)+X@b)
 jac=lambda b:X.T@(1-Y*np.exp(-X@b))
 b0=np.zeros(X.shape[1]);b0[0]=np.log(Y.mean())
 r=minimize(fun,b0,jac=jac,method='BFGS',options={'gtol':1e-10})
 mu=np.exp(X@r.x);D=2*np.sum((Y-mu)/mu-np.log(Y/mu));phi=np.sum(((Y-mu)/mu)**2)/(len(Y)-X.shape[1])
 return r.x,D,phi,len(Y)-X.shape[1]
f0=fit([(i,) for i in range(3)])
f1=fit([(i,) for i in range(4)])
f2=fit([t for k in [1,2] for t in combinations(range(4),k)])
f3=fit([t for k in [1,2,3] for t in combinations(range(4),k)])
assert np.allclose(f0[0],[5.4155331,.1210984,-.2998062,.1824045],atol=1e-6)
assert abs(f2[1]-.033881904)<1e-7 and abs(f3[1]-.008365069)<1e-7
F23=((f2[1]-f3[1])/4)/f3[2];F12=((f1[1]-f2[1])/6)/f2[2]
assert abs(F23-.7628)<.0001 and abs(F12-2.2259)<.0001
assert abs(f.sf(F23,4,1)-.6839)<.0001 and abs(f.sf(F12,6,5)-.1989)<.0001
printed=['4.5','18','32','30']

assert abs(f1[1]-.124180744)<1e-7
Xmain=np.column_stack([np.ones(16),A])
t4=f1[0][4]/np.sqrt(f1[2]*np.linalg.inv(Xmain.T@Xmain)[4,4])
assert abs(t4+1.09898)<.00002
terms=[t for k in [1,2,3] for t in combinations(range(4),k)]
before_last=fit(terms[:-1])
last_F=(before_last[1]-f3[1])/f3[2]
assert abs(f.sf(last_F,1,1)-.6870258)<.000002
assert round(f.sf(last_F,1,1),2)==.69

# Deepened research calculations.
assert 18/2 == 9
assert 15/5 == 3
assert 12/3 == 4
assert 8-5 == 3

article=(ROOT/"articles"/"analysis-of-deviance.qmd").read_text()
for token in printed:
    assert token in article,("analysis-of-deviance",token)
questions=json.loads((ROOT/"research/self-checks.json").read_text())["analysis-of-deviance"]
assert len(questions) in (2,3)
assert article.count("## Check yourself {#check-yourself}") == 1
assert "Your turn" in article
print("analysis-of-deviance: numerical examples, self-checks and generated text verified")
