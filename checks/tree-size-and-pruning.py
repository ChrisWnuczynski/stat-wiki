"""Recompute numerical examples and exercise answers for tree-size-and-pruning."""
import math
import numpy as np
from scipy import stats, special, linalg, integrate

risks=np.array([20,8,4]);leaves=np.array([1,3,5])
for alpha,expected in [(0,5),(1,5),(3,3),(5,3),(7,1)]:assert leaves[np.argmin(risks+alpha*leaves)]==expected
assert np.allclose(risks+4*leaves,[24,20,24])
assert (15-6)/(4-1)==3
assert 6+2*4==14 and 15+2==17 and 6+4*4==22 and 15+4==19
import os,subprocess
R=os.environ['STATWIKI_R_HOME']+'/bin/exec/R'
code='library(rpart);for (small in c(FALSE,TRUE)) for(cp in c(.1,.001)){ctrl<-if(small)rpart.control(cp=cp,xval=0,minsplit=2,minbucket=1) else rpart.control(cp=cp,xval=0);f<-rpart(Species~Petal.Length+Petal.Width,iris,method="class",control=ctrl);cat(sum(f$frame$var=="<leaf>")," ")}'
out=subprocess.run([R,'--vanilla','--slave','-e',code],capture_output=True,text=True,check=True)
assert list(map(int,out.stdout.split()))==[3,3,3,7]
assert 2.5<3
print("tree-size-and-pruning: numerical checks passed")
