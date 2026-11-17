"""Recompute the article's displayed examples and inspect the generated article."""
from pathlib import Path
import math,re,json
import numpy as np
import sympy as sp
from itertools import product
ROOT=Path(__file__).resolve().parents[1]
SLUG='leaf-blotch-data'
article=(ROOT / "articles" / (SLUG+".qmd")).read_text(encoding="utf-8")
body=article.split("## See also",1)[0]
checks=0
def check(condition):
    global checks
    assert condition, SLUG
    checks+=1
def close(actual,expected,rtol=1e-10,atol=1e-12):
    check(np.allclose(np.asarray(actual,dtype=float),np.asarray(expected,dtype=float),rtol=rtol,atol=atol))

# Values from the public CRAN faraway leafblotch object, ordered by site then variety.
y=np.array([0.0005, 0.0, 0.0, 0.001, 0.0025, 0.0005, 0.005, 0.013, 0.015, 0.015, 0.0, 0.0005, 0.0005, 0.003, 0.0075, 0.003, 0.03, 0.075, 0.01, 0.127, 0.0125, 0.0125, 0.025, 0.166, 0.025, 0.025, 0.0, 0.2, 0.375, 0.2625, 0.025, 0.005, 0.0001, 0.03, 0.025, 0.0001, 0.25, 0.55, 0.05, 0.4, 0.055, 0.01, 0.06, 0.011, 0.025, 0.08, 0.1658, 0.295, 0.2, 0.435, 0.01, 0.05, 0.05, 0.05, 0.05, 0.05, 0.1, 0.05, 0.5, 0.75, 0.05, 0.001, 0.05, 0.05, 0.5, 0.1, 0.5, 0.25, 0.5, 0.75, 0.05, 0.1, 0.05, 0.05, 0.25, 0.75, 0.5, 0.75, 0.75, 0.75, 0.175, 0.25, 0.425, 0.5, 0.375, 0.95, 0.625, 0.95, 0.95, 0.95])
site=np.repeat(np.arange(1,10),10);variety=np.tile(np.arange(1,11),9)
check(len(y)==90 and sum(y==0)==4);close(y.sum(),18.6455)
X=np.c_[np.ones(90),np.eye(9)[site-1,1:],np.eye(10)[variety-1,1:]]
check(X.shape==(90,18) and np.linalg.matrix_rank(X)==18);check(90-np.linalg.matrix_rank(X)==72)
# R's own glm provides the quasi-likelihood fits, including the nonstandard variance function.
import os,subprocess,tempfile
rhome=Path(os.environ.get('STATWIKI_R_HOME','/workspace/statwiki-sources/r-runtime/extracted/usr/lib/R'))
rbin=rhome/'bin/exec/R'
if not rbin.exists():
 import shutil
 found=shutil.which('R')
 assert found,'R is required for the leaf-blotch model refit'
 rbin=Path(found)
r_code="""
options(digits=17)
y<-c(Y[0.0005, 0.0, 0.0, 0.001, 0.0025, 0.0005, 0.005, 0.013, 0.015, 0.015, 0.0, 0.0005, 0.0005, 0.003, 0.0075, 0.003, 0.03, 0.075, 0.01, 0.127, 0.0125, 0.0125, 0.025, 0.166, 0.025, 0.025, 0.0, 0.2, 0.375, 0.2625, 0.025, 0.005, 0.0001, 0.03, 0.025, 0.0001, 0.25, 0.55, 0.05, 0.4, 0.055, 0.01, 0.06, 0.011, 0.025, 0.08, 0.1658, 0.295, 0.2, 0.435, 0.01, 0.05, 0.05, 0.05, 0.05, 0.05, 0.1, 0.05, 0.5, 0.75, 0.05, 0.001, 0.05, 0.05, 0.5, 0.1, 0.5, 0.25, 0.5, 0.75, 0.05, 0.1, 0.05, 0.05, 0.25, 0.75, 0.5, 0.75, 0.75, 0.75, 0.175, 0.25, 0.425, 0.5, 0.375, 0.95, 0.625, 0.95, 0.95, 0.95])
d<-data.frame(y=y,site=factor(rep(1:9,each=10)),variety=factor(rep(1:10,9)))
f1<-glm(y~site+variety,data=d,family=quasibinomial())
v2<-list(varfun=function(mu)mu^2*(1-mu)^2,
 validmu=function(mu)all(mu>0 & mu<1),
 dev.resids=function(y,mu,wt)wt*(y-mu)^2/(mu^2*(1-mu)^2),
 initialize=expression({n<-rep.int(1,nobs);mustart<-pmax(.001,pmin(.999,y))}),name='mu^2(1-mu)^2')
f2<-glm(y~site+variety,data=d,family=quasi(link='logit',variance=v2))
cat('FIT1 ',coef(f1),summary(f1)$coefficients[,2],summary(f1)$coefficients[,4],summary(f1)$dispersion,df.residual(f1),'\\n',sep=' ')
cat('FIT2 ',coef(f2),summary(f2)$coefficients[,2],summary(f2)$dispersion,df.residual(f2),'\\n',sep=' ')
""".replace('Y[0.0005, 0.0, 0.0, 0.001, 0.0025, 0.0005, 0.005, 0.013, 0.015, 0.015, 0.0, 0.0005, 0.0005, 0.003, 0.0075, 0.003, 0.03, 0.075, 0.01, 0.127, 0.0125, 0.0125, 0.025, 0.166, 0.025, 0.025, 0.0, 0.2, 0.375, 0.2625, 0.025, 0.005, 0.0001, 0.03, 0.025, 0.0001, 0.25, 0.55, 0.05, 0.4, 0.055, 0.01, 0.06, 0.011, 0.025, 0.08, 0.1658, 0.295, 0.2, 0.435, 0.01, 0.05, 0.05, 0.05, 0.05, 0.05, 0.1, 0.05, 0.5, 0.75, 0.05, 0.001, 0.05, 0.05, 0.5, 0.1, 0.5, 0.25, 0.5, 0.75, 0.05, 0.1, 0.05, 0.05, 0.25, 0.75, 0.5, 0.75, 0.75, 0.75, 0.175, 0.25, 0.425, 0.5, 0.375, 0.95, 0.625, 0.95, 0.95, 0.95]',','.join(repr(float(z)) for z in y))
env=os.environ.copy();env.setdefault('R_HOME',str(rhome))
result=subprocess.run([str(rbin),'--vanilla','--slave'],input=r_code,text=True,capture_output=True,env=env,check=True)
parsed={line.split()[0]:np.array([float(z) for z in line.split()[1:]]) for line in result.stdout.splitlines() if line.startswith('FIT')}
z=parsed['FIT1'];b=z[:18];se=z[18:36];pv=z[36:54];phi=z[54];df=z[55]
check(f"{b[0]:.6f}"=="-8.054596");check([f"{v:.6f}" for v in [b[9],se[9],b[9]/se[9],math.exp(b[9]),phi]]==["0.150083","0.723685","0.207388","1.161931","0.088781"]);close([b[9],se[9],b[9]/se[9],math.exp(b[9]),phi,df],[.150083,.723685,.207388,1.161931,.088781,72],rtol=0,atol=.000001)
# Rounded summaries displayed with the model output.
close(b[0],-8.05,atol=.005);close(phi,.089,atol=.0005);close(b[9]/se[9],.21,atol=.005)
check(all(pv[9:12]>.05) and all(pv[12:]<.05))
z2=parsed['FIT2'];b2=z2[:18];se2=z2[18:36];phi2=z2[36]
close(b2[9:],[-.467277,.078774,.954185,1.352755,1.328586,2.340659,3.262684,3.135564,3.887357],rtol=0,atol=.000002)
close(se2[9:],.4686804,atol=.000001);close(phi2,.9884757,atol=.000002)
# Both the precise worked fit and the source table's two-decimal contrasts.
close(np.r_[0,b2[9:]],[0,-.47,.08,.95,1.35,1.33,2.34,3.26,3.14,3.89],atol=.005)
close(np.sqrt(np.diag(phi2*np.linalg.inv(X.T@X))),se2,rtol=1e-5)
mu=.1;V=mu*(1-mu);close([V,V*V,V*V/V],[.09,.0081,.09])
mu=.5;derivative=mu*(1-mu);close([derivative,derivative**2,derivative**2/derivative,derivative**2/(derivative**2)],[.25,.0625,.25,1])

# Verify citation coverage in the composed article, including copied source blocks.
check(len(re.findall(r'class="cite-ref"',body))>=5)
proper_keys=set(re.findall(r'data-cite-key="([^" ]+)"',body))-{'r_faraway_leafblotch2026'}
check(len(proper_keys)>=2)

for token in ['0.150083', '0.723685', '0.207388', '0.468680', '72 residual']:
    check(token in body)
check("**Your turn.**" in body)
check(len(re.findall(r"^## Check yourself \{#check-yourself\}",body,re.M))==1)
print(f"{SLUG}: {checks} numerical, algebraic and rendered-content checks passed")
