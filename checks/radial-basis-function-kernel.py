"""Recompute the mathematical claims and printed values for radial-basis-function-kernel."""
from pathlib import Path
import math
import numpy as np
from scipy import stats,integrate,special
ROOT=Path(__file__).resolve().parents[1]
article=(ROOT/"articles"/"radial-basis-function-kernel.qmd").read_text(encoding="utf-8")
count=0
def eq(actual,expected,tol=1e-10):
 global count
 assert np.allclose(actual,expected,rtol=tol,atol=tol),(actual,expected)
 count+=1
x=np.arange(3.);K=np.exp(-np.subtract.outer(x,x)**2/2)
eq(K[0,1],np.exp(-.5));eq(K[0,2],np.exp(-2));eq(np.diag(K),np.ones(3))
c=np.array([1.,-1.,0.]);eq(c@K@c,2*(1-np.exp(-.5)))
eq(np.exp(-1/8),.8824969025845955);eq(1/(2*2**2),1/8)
assert np.linalg.eigvalsh(K).min()>0
for a in [.5,2,10]:eq(np.exp(-np.subtract.outer(a*x,a*x)**2/(2*a*a)),K)
eq(math.comb(2+2,2),6)
import os,re,subprocess
import shutil
rhome=os.environ.get('STATWIKI_R_HOME')
rscript=shutil.which('Rscript')
rexec=shutil.which('R')
if rscript:
 rcommand=[rscript,'--vanilla','-']
elif rhome:
 rcommand=[str(Path(rhome)/'bin'/'exec'/'R'),'--vanilla','--slave']
elif rexec:
 rcommand=[rexec,'--vanilla','--slave']
else:
 raise RuntimeError('R with e1071 is required for the complete iris refit; install R or set STATWIKI_R_HOME.')
rblock=next(block for block in re.findall(r'```r\n(.*?)\n```',article,re.S) if 'set.seed(17006)' in block and 'grid$CV_error' in block)
probe=rblock+"\ncat('CV_COUNTS',paste(round(grid$CV_error*nrow(train)),collapse=','),'\\n')\ncat('FIT_SUMMARY',nrow(train),nrow(test),best$cost,best$gamma,sum(predict(svm_fit,iris_scaled$test)!=test$Species),'\\n')\n"
run=subprocess.run(rcommand,input=probe,text=True,capture_output=True,check=True)
cm=re.search(r'CV_COUNTS ([0-9,]+)',run.stdout)
assert cm,run.stdout
eq([int(v) for v in cm.group(1).split(',')],[12,8,7,11,10,10,10,10,13])
eq([float(v) for v in re.search(r'FIT_SUMMARY ([0-9. ]+)',run.stdout).group(1).split()],[105,45,10,.1,0])
for expected in [.114286,.076190,.066667,.104762,.095238,.123810]:
 assert f'{expected:.6f}' in article
 count+=1

for token in ['0.606531', '0.135335', '0.786939']:
 assert token in article,token
 count+=1
assert "## Check yourself {#check-yourself}" in article
print(f"radial-basis-function-kernel: {count} mathematical and printed-value checks passed")
