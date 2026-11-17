"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SLUG='quasi-likelihood'
ARTICLE=(ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
WORKED=ARTICLE.split("{#worked-example}",1)[1].split("\n## ",1)[0]
EXAMPLE,TURN=WORKED.split("**Your turn.**",1)
ANSWER=TURN.split('title="Answer"}',1)[1].split("\n:::",1)[0]

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

y=np.array([1,3,2,6],float);mu=y.mean();ss=((y-mu)**2).sum();phi=(ss/mu)/(len(y)-1)
close(mu,3);close(ss,14);close(phi,14/9);close(phi*mu/4,7/6)
close(math.sqrt(phi*mu/4),1.0801234497);close(math.sqrt(mu/4),.8660254038)
close((3-2)/(1.5*2),1/3);close(1/(1.5*2),1/3);close(.4*.6,.24);assert .48>.24
# Numeric derivative verifies the integrated Poisson quasi-score.
from scipy.optimize._numdiff import approx_derivative
Q=lambda u:(3*math.log(u/3)-u+3)/1.5
close(approx_derivative(lambda v:Q(v[0]),[2])[0],(3-2)/(1.5*2))
assert 9*10==90 and 1+8+9==18 and 90-18==72
for u in [.1,.5,.9]:
 assert u*u*(1-u)**2<u*(1-u)
close(.5*.5,.25);close(.5**2*(1-.5)**2,.0625)
import os,subprocess,shutil
r_home=os.environ.get('STATWIKI_R_HOME')
R=os.path.join(r_home,'bin','exec','R') if r_home else None
if not R or not os.path.isfile(R):R=shutil.which('R')
assert R,'R required for the leaf-blotch fit'
# Proportions from the faraway::leafblotch table, ordered by site then variety.
# Embedded so the quasi-binomial refit does not need the faraway package.
blotch=[0.0005, 0.0, 0.0, 0.001, 0.0025, 0.0005, 0.005, 0.013, 0.015, 0.015, 0.0, 0.0005, 0.0005, 0.003, 0.0075, 0.003, 0.03, 0.075, 0.01, 0.127, 0.0125, 0.0125, 0.025, 0.166, 0.025, 0.025, 0.0, 0.2, 0.375, 0.2625, 0.025, 0.005, 0.0001, 0.03, 0.025, 0.0001, 0.25, 0.55, 0.05, 0.4, 0.055, 0.01, 0.06, 0.011, 0.025, 0.08, 0.1658, 0.295, 0.2, 0.435, 0.01, 0.05, 0.05, 0.05, 0.05, 0.05, 0.1, 0.05, 0.5, 0.75, 0.05, 0.001, 0.05, 0.05, 0.5, 0.1, 0.5, 0.25, 0.5, 0.75, 0.05, 0.1, 0.05, 0.05, 0.25, 0.75, 0.5, 0.75, 0.75, 0.75, 0.175, 0.25, 0.425, 0.5, 0.375, 0.95, 0.625, 0.95, 0.95, 0.95]
code=r"""
blotch<-c(BLOTCH)
d<-data.frame(blotch=blotch,site=rep(1:9,each=10),variety=rep(1:10,9))
stopifnot(nrow(d)==90,length(unique(d$site))==9,length(unique(d$variety))==10)
a=glm(blotch~factor(site)+factor(variety),d,family=quasibinomial)
sa=coef(summary(a));stopifnot(abs(summary(a)$dispersion-.08878094)<1e-7,abs(coef(a)[1]+8.0546)<1e-4,abs(sa['factor(variety)2',3]-.207)<.001)
stopifnot(all(sa[paste0('factor(variety)',2:4),4]>.05),all(sa[paste0('factor(variety)',5:10),4]<.05))
v=quasi(link='logit',variance=list(varfun=function(mu)mu^2*(1-mu)^2,validmu=function(mu)all(mu>0 & mu<1),dev.resids=function(y,mu,wt)wt*(y-mu)^2/(mu^2*(1-mu)^2),initialize=expression({n=rep.int(1,nobs);mustart=pmax(.001,pmin(.999,y))}),name='mu^2(1-mu)^2'))
b=glm(blotch~factor(site)+factor(variety),d,family=v);sb=coef(summary(b))[paste0('factor(variety)',2:10),]
stopifnot(max(abs(sb[,1]-c(-.47,.08,.95,1.35,1.33,2.34,3.26,3.14,3.89)))<.005)
stopifnot(max(abs(sb[,2]-.4686803))<1e-6,df.residual(b)==72)
""".replace("BLOTCH",",".join(repr(float(v)) for v in blotch))
subprocess.run([R,'--vanilla','--slave'],input=code,text=True,check=True)
close((3**2-1.5*2-2**2)/(2*1.5*2**2),1/6)
# Compare computed values with the worked example and hidden answer.
assert rf"\widehat\mu={mu:g}" in EXAMPLE
assert f"={F(float(phi)).limit_denominator()}$" in EXAMPLE
assert rf"\approx{math.sqrt(phi*mu/4):.6f}" in EXAMPLE
assert rf"\approx{math.sqrt(mu/4):.6f}" in EXAMPLE
turn_score=F(3-2)/(F(3,2)*2)
assert rf"score is $(3-2)/(1.5\times2)={turn_score}$" in ANSWER
assert rf"variance under the specified moments is $1/(1.5\times2)={F(1)/(F(3,2)*2)}$" in ANSWER
print("quasi-likelihood: numerical checks passed")
