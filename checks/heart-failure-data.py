"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

import os,subprocess,csv
root=Path(__file__).resolve().parents[1];p=root/'sources/stat1301/data/heart.csv'
rows=list(csv.DictReader(p.open()));assert len(rows)==299
assert sum(int(x['DEATH_EVENT']) for x in rows)==96 and 299-96==203
assert min(float(x['time']) for x in rows)==4 and max(float(x['time']) for x in rows)==285
assert all(len(x)==13 for x in rows)
assert min(float(x['age']) for x in rows)==40 and max(float(x['age']) for x in rows)==95
assert sum(int(x['sex']) for x in rows)==194

assert round(96/299,4)==.3211 and round(203/299,4)==.6789
assert round(math.exp(.04618),4)==1.0473
print('ten-year odds multiplier',math.exp(.4618),'probability',math.exp(.4618)*.2/(.8+math.exp(.4618)*.2))
assert math.isclose(2*.25/(.75+2*.25),.4)
r=Path(os.environ['STATWIKI_R_HOME'])/'bin/exec/R'
script=r"""
h<-read.csv(commandArgs(TRUE)[1]); f<-glm(DEATH_EVENT~age+high_blood_pressure,h,family=binomial());s<-summary(f);ci<-suppressMessages(confint(f))
stopifnot(max(abs(coef(f)-c(-3.70568,.04618,.26920)))<5e-6)
stopifnot(max(abs(s$coefficients[,2]-c(.71072,.01110,.26487)))<5e-6)
stopifnot(max(abs(ci-matrix(c(-5.14257577,.02483923,-.25344324,-2.34844333,.06851426,.78698218),3,2)))<1e-7)
stopifnot(round(f$null.deviance,2)==375.35,round(f$deviance,2)==354.97,round(AIC(f),2)==360.97,f$iter==4)
stopifnot(f$df.null==298,f$df.residual==296)
print(s$coefficients)
"""
subprocess.run([str(r),'--slave','-e',script,'--args',str(p)],check=True)
assert round(math.exp(.02483923),3)==1.025 and round(math.exp(.06851426),3)==1.071
assert round(math.exp(-.25344324),2)==.78 and round(math.exp(.78698218),2)==2.20
assert round(375.35-354.97,2)==20.38 and 354.97+6==360.97
assert round(math.exp(.4618),4)==1.5869
assert round(math.exp(.4618)*.2/(.8+math.exp(.4618)*.2),4)==.2840
print("heart-failure-data: numerical checks passed")
