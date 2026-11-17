"""Recompute the mathematical claims and printed values for singular-value-decomposition."""
from pathlib import Path
import math
import numpy as np
from scipy import stats,integrate,special
ROOT=Path(__file__).resolve().parents[1]
article=(ROOT/"articles"/"singular-value-decomposition.qmd").read_text(encoding="utf-8")
count=0
def eq(actual,expected,tol=1e-10):
 global count
 assert np.allclose(actual,expected,rtol=tol,atol=tol),(actual,expected)
 count+=1
A=np.array([[3.,0.],[0.,2.],[0.,0.]])
U,s,Vt=np.linalg.svd(A,full_matrices=False)
eq(s,[3,2]);eq(U@np.diag(s)@Vt,A);eq(U.T@U,np.eye(2));eq(Vt@Vt.T,np.eye(2))
A1=s[0]*np.outer(U[:,0],Vt[0]);eq(A1,[[3,0],[0,0],[0,0]])
eq(np.sum((A-A1)**2),4);eq(np.sum(A1*A1)/np.sum(A*A),9/13)
eq(np.linalg.pinv(A),[[1/3,0,0],[0,1/2,0]])
eq(np.linalg.eigvalsh(A.T@A),[4,9]);eq(3**2+1**2,10);eq(25+9+1,35);eq(10**2/(6-1),20)
import os,shutil,subprocess
rhome=os.environ.get('STATWIKI_R_HOME');rscript=shutil.which('Rscript');rexec=shutil.which('R')
if rscript:rcommand=[rscript,'--vanilla','-']
elif rhome:rcommand=[str(Path(rhome)/'bin'/'exec'/'R'),'--vanilla','--slave']
elif rexec:rcommand=[rexec,'--vanilla','--slave']
else:raise RuntimeError('R is required to verify the stated prcomp behavior; install R or set STATWIKI_R_HOME.')
rsource="A <- matrix(c(3,0,0,0,2,0),3,2); p <- prcomp(A,center=TRUE,scale.=FALSE); stopifnot(isTRUE(all.equal(p$sdev^2,svd(scale(A,center=TRUE,scale=FALSE))$d^2/(nrow(A)-1))))\n"
subprocess.run(rcommand,input=rsource,text=True,capture_output=True,check=True)
count+=1

for token in ['0.692308']:
 assert token in article,token
 count+=1
assert "## Check yourself {#check-yourself}" in article
print(f"singular-value-decomposition: {count} mathematical and printed-value checks passed")
