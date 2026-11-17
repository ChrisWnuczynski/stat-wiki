"""Recompute the numerical examples and exercises for this article."""
import math
from fractions import Fraction as F
import numpy as np
from scipy import stats

from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SLUG='mine-injury-data'
ARTICLE=(ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
WORKED=ARTICLE.split("{#worked-example}",1)[1].split("\n## ",1)[0]
EXAMPLE,TURN=WORKED.split("**Your turn.**",1)
ANSWER=TURN.split('title="Answer"}',1)[1].split("\n:::",1)[0]

def close(a,b,tol=1e-6):
    assert np.allclose(a,b,rtol=0,atol=tol), (a,b)

import os,subprocess,shutil
close(math.exp(-3.7207),.024216927,tol=1e-6)
close([math.exp(-.0015),math.exp(-.015),math.exp(.0627),math.exp(-.0317)],[.998501124,.985111940,1.064707379,.968797149],tol=1e-6)
close(math.exp(.3598),1.4330427773);close(math.exp(.627),1.8719861883)
close(math.exp(.9868),2.6826362865);close(math.exp(-.317),.7283307551);close(math.exp(.3135),1.3682054628)
r_home=os.environ.get('STATWIKI_R_HOME')
R=os.path.join(r_home,'bin','exec','R') if r_home else None
if not R or not os.path.isfile(R):R=shutil.which('R')
assert R,'R is required for the mine-data refit'
# Fracture counts from Myers (1990), as shipped in locfit::mine (44 mines).
# Embedded so the Poisson refit does not need the locfit package or a local rda.
frac=[2,1,0,4,1,2,0,0,4,4,1,4,1,5,2,5,5,5,0,5,1,1,3,3,2,2,0,1,5,2,3,3,3,0,0,2,0,0,3,2,3,5,0,3]
inb=[50,230,125,75,70,65,65,350,350,160,145,145,180,43,42,42,45,83,300,190,145,510,65,470,300,275,420,65,40,900,95,40,140,150,80,80,145,100,150,150,210,11,100,50]
extrp=[70,65,70,65,65,70,60,60,90,80,65,85,70,80,85,85,85,85,65,90,90,80,75,90,80,90,50,80,75,90,88,85,90,50,60,85,65,65,80,80,75,75,65,88]
time=[1,6,1,0.5,0.5,3,1,0.5,0.5,0,10,0,2,0,12,0,0,10,10,6,12,10,5,9,9,4,17,15,15,35,20,10,7,5,5,5,9,9,3,0,2,0,25,20]
code=r"""
y<-c(FRAC)
x1<-c(INB)
x2<-c(EXTRP)
x3<-c(TIME)
d=data.frame(y=y,x1=x1,x2=x2,x3=x3)
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
""".replace("FRAC",",".join(repr(float(v)) for v in frac)).replace("INB",",".join(repr(float(v)) for v in inb)).replace("EXTRP",",".join(repr(float(v)) for v in extrp)).replace("TIME",",".join(repr(float(v)) for v in time))
subprocess.run([R,'--vanilla','--slave'],input=code,text=True,check=True)
# Compare computed values with the worked example and hidden answer.
assert rf"\approx{math.exp(.3598):.6f}" in EXAMPLE
assert rf"\approx{math.exp(.627):.6f}" in EXAMPLE
assert rf"\approx{math.exp(-.317):.6f}" in EXAMPLE
assert rf"\approx{math.exp(5*.0627):.6f}" in ANSWER
print("mine-injury-data: numerical checks passed")
