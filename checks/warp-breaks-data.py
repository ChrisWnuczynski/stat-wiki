"""Recompute numerical examples and exercise answers for warp-breaks-data."""
import math
import numpy as np
from scipy import stats, special, linalg, integrate

import os,subprocess,json
R=os.environ['STATWIKI_R_HOME']+'/bin/exec/R'
code=r'''
library(gee)
d<-warpbreaks;d$factory<-d$wool;d<-d[order(d$factory),]
f1<-gee(breaks~tension,id=factory,data=d,family=poisson,corstr="exchangeable")
f2<-gee(breaks~tension,id=factory,data=d,family=poisson,corstr="AR-M",Mv=1)
f3<-gee(breaks~tension,id=factory,data=d,family=gaussian(link="log"),corstr="AR-M",Mv=1)
cat("RESULT",nrow(d),as.numeric(tapply(d$breaks,list(d$wool,d$tension),mean)),coef(f1),sqrt(diag(f1$naive.variance)),sqrt(diag(f1$robust.variance)),f1$scale,f1$working.correlation[1,2],coef(f2),f2$working.correlation[1,2],coef(f3),f3$scale,"\n")
'''
out=subprocess.run([R,'--vanilla','--slave','-e',code],capture_output=True,text=True,check=True)
line=next(x for x in out.stdout.splitlines() if x.startswith('RESULT'));v=np.array(list(map(float,line.split()[1:])))
assert v[0]==54 and np.allclose(v[1:7],[44.55556,28.22222,24,28.77778,24.55556,18.77778],atol=1e-5)
assert np.allclose(v[7:10],[3.5942635,-.3213204,-.5184885],atol=1e-6)
assert np.allclose(v[10:13],[.09055356,.12808197,.136191],atol=1e-7)
assert np.allclose(v[13:16],[.15869419,.22270597,.06441329],atol=1e-7)
assert np.allclose(v[16:18],[4.601903,.02088982],atol=1e-6)
assert np.allclose(v[18:21],[3.5949833,-.3245601,-.5178782],atol=1e-6)
assert np.isclose(v[21],.041259814,atol=1e-8)
assert np.allclose(v[22:25],[3.5949425,-.3244928,-.5181423],atol=1e-6) and np.isclose(v[25],141.1501,atol=.0001)
assert round(24/(401/9),4)==.5387 and round((259/9)/(254/9),4)==1.0197
assert round((475/18)/(655/18),6)==.725191 and round((390/18)/(655/18),6)==.595420
assert np.isclose(math.exp(math.log(.75))*40,30)
assert round(v[8]/v[11],2)==-2.51 and round(v[8]/v[14],2)==-1.44
assert round(math.exp(3.594))==36 and round(math.exp(-.321),2)==.73 and round(math.exp(-.518),2)==.60
assert np.isclose(.041**2,.001681) and np.isclose(.041**3,.000068921)
assert math.exp(-.5)<1
print("warp-breaks-data: numerical checks passed")
