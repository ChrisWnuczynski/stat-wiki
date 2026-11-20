"""Recompute confidence ellipsoid axes, quadratic tests and covariance scaling."""
from pathlib import Path
import re
import numpy as np
import sympy as s
from scipy.stats import f
root=Path(__file__).resolve().parents[1]
n,p=20,2;S=s.Matrix([[2,1],[1,2]])
mean=s.Matrix([1,s.Rational(1,2)])
assert set(S.eigenvals())=={1,3}
assert S.inv()==s.Matrix([[2,-1],[-1,2]])/3
q=f.ppf(.95,p,n-p);c=p*(n-1)/(n-p)*q
assert round(q,6)==3.554557 and round(c,6)==7.504065
axes=np.sqrt(c*np.array([3,1])/n)
assert round(axes[0],5)==1.06095 and round(axes[1],5)==.61254
assert (n*(mean.T*S.inv()*mean))[0]==10
d=mean-s.Matrix([1,0]);assert (n*(d.T*S.inv()*d))[0]==s.Rational(10,3)
assert 10>c and float(s.Rational(10,3))<c
assert np.allclose(np.sqrt(c*np.array([12,4])/n),2*axes)
# Divisor conversion: the source's covariance divisor n gives a larger statistic.
T_unbiased=10;T_divisor_n=n/(n-1)*T_unbiased
assert np.isclose((n-p)/(n*p)*T_divisor_n,(n-p)/(p*(n-1))*T_unbiased)
S6=s.Matrix([[4,1],[1,1]]);x6=s.Matrix([2,1])
assert (6*(x6.T*S6.inv()*x6))[0]==8
assert 4/(2*5)*8==3.2
assert round(f.ppf(.95,2,4),3)==6.944
body=(root/"articles/confidence-region-for-a-normal-mean-vector.qmd").read_text().split("## See also",1)[0]
for text in ["7.504065","1.06095","0.61254","10/3","Your turn","## Check yourself {#check-yourself}"]:
    assert text in body,text
assert len(re.findall('class="cite-ref"',body))>=5
for qid in ["ex-sl-02-5","ex-sl-01-4"]:assert f"../questions/{qid}.qmd" in body
print("confidence-region-for-a-normal-mean-vector: axes, tests, scaling and article checks passed")
