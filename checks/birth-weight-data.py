"""Recompute numerical examples and verify the generated article."""
from pathlib import Path
import math
import re
import numpy as np
from scipy import stats, integrate
ROOT=Path(__file__).resolve().parents[1]
SLUG='birth-weight-data'
body=(ROOT/"articles"/f'{SLUG}.qmd').read_text().split('## See also',1)[0]
def close(a,b,atol=1e-10):
    aa,bb,tt=np.broadcast_arrays(np.asarray(a),np.asarray(b),np.asarray(atol))
    for x,y,tol in zip(aa.flat,bb.flat,tt.flat):
        np.testing.assert_allclose(x,y,rtol=0,atol=float(tol))
def shown(*values):
    for value in values:
        assert value in body, (SLUG,value)
def finish():
    assert '**Your turn.**' in body
    assert '## Check yourself' in body
    assert body.count('data-cite-key=')>=5
    assert len(set(re.findall(r'data-cite-key="([^" ]+)"',body)))>=2
    assert not any(ord(c)<32 and c not in '\n\r\t' for c in body)
    print(SLUG+': numerical examples and article checks passed')
import subprocess,os,tempfile,csv
# Refit the actual R dataset and compare all copied table fields, not stored coefficients.
rbin=Path(os.environ['STATWIKI_R_HOME'])/'bin/exec/R'
script="""suppressMessages(library(MASS))
m<-lm(bwt~lwt+age+factor(race)+smoke,data=birthwt)
s<-summary(m)
cat("COEF",as.vector(t(coef(s))),"\\n")
cat("FIT",nrow(birthwt),df.residual(m),s$sigma,s$r.squared,s$adj.r.squared,s$fstatistic[1],pf(s$fstatistic[1],s$fstatistic[2],s$fstatistic[3],lower.tail=FALSE),"\\n")
cat("CI",confint(m)["smoke",],"\\n")
cat("PRED",predict(m,newdata=data.frame(lwt=c(130,130),age=c(25,25),race=c(1,1),smoke=c(0,1))),"\\n")
"""
run=subprocess.run([str(rbin),'--vanilla','--slave'],input='options(digits=15)\n'+script,text=True,capture_output=True,check=True)
parsed={}
for line in run.stdout.splitlines():
 parts=line.split()
 if parts and parts[0] in ['COEF','FIT','CI','PRED']:parsed[parts[0]]=np.array([float(z) for z in parts[1:]])
coef=parsed['COEF'].reshape(6,4)
close(coef[:,0],[2839.433,4.000,-1.948,-510.501,-398.644,-401.720],.00051)
close(coef[:,1],[321.435,1.738,9.820,157.077,119.579,109.241],.00051)
close(coef[:,2],[8.834,2.301,-.198,-3.250,-3.334,-3.677],.00051)
close(coef[:,3],[8.2e-16,.02249,.84299,.00137,.00104,.00031],[1e-18,.000005,.000005,.000005,.000005,.000005])
close(parsed['FIT'],[189,183,682.1,.1483,.125,6.373,1.758e-5],[1e-12,1e-12,.05,.00005,.00005,.0005,.0005e-5])
close(parsed['CI'],[-617.25379,-186.18718],.000005)
close(parsed['PRED'],[3310.72942,2909.00893],.000005)
close(parsed['PRED'][1]-parsed['PRED'][0],coef[-1,0])
close(coef[1,0]*10,39.99938,.000005)
shown('3310.72942','2909.00893','617.25379','186.18718','39.99938','183')
assert 'age adds nothing' not in body
finish()
