"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

import os,subprocess,shutil
close(math.exp(-3.7207),.024216927,tol=1e-6)
close([math.exp(-.0015),math.exp(-.015),math.exp(.0627),math.exp(-.0317)],[.998501124,.985111940,1.064707379,.968797149],tol=1e-6)
close(math.exp(.3598),1.4330427773);close(math.exp(.627),1.8719861883)
close(math.exp(.9868),2.6826362865);close(math.exp(-.317),.7283307551);close(math.exp(.3135),1.3682054628)
R=os.path.join(os.environ.get('STATWIKI_R_HOME','/workspace/statwiki-sources/r-runtime/extracted/usr/lib/R'),'bin/exec/R')
if not os.path.isfile(R):R=shutil.which('R')
assert R,'R is required for the mine-data refit'
code=r"""
p='/workspace/statwiki-sources/r-packages/locfit/data/mine.rda'
if(file.exists(p)) load(p) else data(mine,package='locfit')
d=data.frame(y=mine$frac,x1=mine$inb,x2=mine$extrp,x3=mine$time)
stopifnot(nrow(d)==44)
a=glm(y~x1+x2+x3,data=d,family=poisson);b=update(a,family=quasipoisson)
stopifnot(max(abs(coef(a)-c(-3.7206821,-.0014793,.0627011,-.0316514)))<1e-7)
stopifnot(max(abs(coef(a)-coef(b)))<1e-10)
sa=coef(summary(a));sb=coef(summary(b));ph=summary(b)$dispersion
stopifnot(abs(ph-.9049145)<1e-7,abs(sqrt(ph)-.951269)<1e-6)
stopifnot(max(abs(sa[,2]-c(.978877,.0008244,.0122711,.0163095)))<1e-7)
stopifnot(max(abs(sb[,2]/sa[,2]-sqrt(ph)))<1e-10)
stopifnot(abs(sa[4,4]-.052298)<1e-6,abs(sb[4,4]-.047982)<1e-6)
stopifnot(abs(sa[2,4]-.072757)<1e-6,abs(sb[2,4]-.066533)<1e-6)
stopifnot(abs(sa[3,4]-3.23e-7)<1e-9,abs(sa[1,4]-.000144)<1e-6)
stopifnot(abs(sum(fitted(a))-sum(d$y))<1e-7,df.residual(a)==40)
"""
subprocess.run([R,'--vanilla','--slave'],input=code,text=True,check=True)
print("mine-injury-data: numerical checks passed")
