from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
import numpy as np
from fractions import Fraction as F
y=np.array([1.,2.,6.]);H=np.ones((3,3))/3;e=y-H@y
assert np.array_equal(e,[-2,-1,3]) and e.sum()==0 and e@e==14
cov=9*(np.eye(3)-H)
assert np.allclose(np.diag(cov),6) and cov[0,1]==-3
assert F(-3,6)==-F(1,2) and F(14,2)==7
assert np.allclose((y+5)-H@(y+5),e) and np.allclose(H@(y+5),8)
assert 12-9==3
printed=['14','-1/2']

article=(ROOT/"articles"/"error-and-residual.qmd").read_text()
for token in printed:
    assert token in article,("error-and-residual",token)
questions=json.loads((ROOT/"research/self-checks.json").read_text())["error-and-residual"]
assert len(questions) in (2,3)
assert article.count("## Check yourself {#check-yourself}") == 1
assert "Your turn" in article
print("error-and-residual: numerical examples, self-checks and generated text verified")
