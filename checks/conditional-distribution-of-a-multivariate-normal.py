from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
from fractions import Fraction as F
import numpy as np
S=np.array([[4.,3.],[3.,9.]])
assert np.all(np.linalg.eigvalsh(S)>0)
C=F(3,9);v=4-F(3*3,9)
assert 1+C*(5-2)==2 and v==3 and 1+C*(-1-2)==0
assert 1+C*(8-2)==3
T=np.array([[1.,-1/3],[0.,1.]])
assert np.allclose(T@S@T.T,np.diag([3.,9.]))
# The bivariate zero-mean source example.
assert F(1,2)*2==1 and 1-F(1,2)**2==F(3,4)
printed=['N(2,3)','sqrt3']

article=(ROOT/"articles"/"conditional-distribution-of-a-multivariate-normal.qmd").read_text()
for token in printed:
    assert token in article,("conditional-distribution-of-a-multivariate-normal",token)
questions=json.loads((ROOT/"research/self-checks.json").read_text())["conditional-distribution-of-a-multivariate-normal"]
assert len(questions) in (2,3)
assert article.count("## Check yourself {#check-yourself}") == 1
assert "Your turn" in article
print("conditional-distribution-of-a-multivariate-normal: numerical examples, self-checks and generated text verified")
