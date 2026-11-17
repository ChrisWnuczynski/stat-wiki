"""Recompute the article's displayed examples and inspect the generated article."""
from pathlib import Path
import math,re,json
import numpy as np
import sympy as sp
from itertools import product
ROOT=Path(__file__).resolve().parents[1]
SLUG='multiple-linear-regression'
article=(ROOT / "articles" / (SLUG+".qmd")).read_text(encoding="utf-8")
body=article.split("## See also",1)[0]
checks=0
def check(condition):
    global checks
    assert condition, SLUG
    checks+=1
def close(actual,expected,rtol=1e-10,atol=1e-12):
    check(np.allclose(np.asarray(actual,dtype=float),np.asarray(expected,dtype=float),rtol=rtol,atol=atol))

X=np.array([[1,0,0],[1,1,0],[1,0,1],[1,1,1]],float);y=np.array([1,3,4,7.])
beta=np.linalg.lstsq(X,y,rcond=None)[0]; fitted=X@beta;e=y-fitted
close(beta,[.75,2.5,3.5]);close(fitted,[.75,3.25,4.25,6.75]);close(e,[.25,-.25,-.25,.25]);close(X.T@e,0)
close(e@e,.25);close(np.linalg.inv(X.T@X),[[.75,-.5,-.5],[-.5,1,0],[-.5,0,1]])
close(np.sqrt(np.diag((e@e)*np.linalg.inv(X.T@X)))[1:],[.5,.5])
close(np.linalg.lstsq(X,y+2,rcond=None)[0],[2.75,2.5,3.5])
check(np.linalg.matrix_rank(np.c_[X,X[:,1]+X[:,2]])==3)
# Refit the full published birth-weight example using the repository's raw CSV.
import csv
from scipy.stats import t as t_law,f as f_law
rows=list(csv.DictReader((ROOT/'sources/stat1301/data/birthwt.csv').open()))
Z=np.array([[1,float(r['lwt']),float(r['age']),float(r['race']=='2'),float(r['race']=='3'),float(r['smoke'])] for r in rows]); yy=np.array([float(r['bwt']) for r in rows])
b=np.linalg.lstsq(Z,yy,rcond=None)[0];res=yy-Z@b;df=len(yy)-Z.shape[1];s2=res@res/df;se=np.sqrt(np.diag(s2*np.linalg.inv(Z.T@Z)));ts=b/se;pv=2*t_law.sf(abs(ts),df)
close(b,[2839.433,4.000,-1.948,-510.501,-398.644,-401.720],rtol=0,atol=.0006)
close(se,[321.435,1.738,9.820,157.077,119.579,109.241],rtol=0,atol=.0006)
check(df==183);close(np.sqrt(s2),682.1,atol=.05)
r2=1-(res@res)/sum((yy-yy.mean())**2);adj=1-(1-r2)*(len(yy)-1)/df
close([r2,adj],[.1483,.125],rtol=0,atol=.0001)
fstat=(r2/5)/((1-r2)/df);close(fstat,6.373,atol=.0006);close(f_law.sf(fstat,5,df),1.758e-5,rtol=.001)
close(pv[1:],[.02249,.84299,.00137,.00104,.00031],atol=.000006)
# Student-survey raw data are absent: recompute every inference recoverable from printed rounded summaries.
survey_b=np.array([132.2677,.5304,.3744]);survey_se=np.array([5.2473,.1962,.0572]);tt=survey_b/survey_se
close(tt,[25.207,2.703,6.546],atol=.001)
close(2*t_law.sf(abs(tt[1:]),97),[.0081,2.82e-9],rtol=.01,atol=.00001)
close(survey_b@[1,30,75],176.3,atol=.05)
ci=survey_b[:,None]+np.array([-1,1])*t_law.ppf(.975,97)*survey_se[:,None]
close(ci,[[121.8533072,142.6821199],[.1410087,.9198251],[.2608887,.4879514]],atol=.0002)
close(1-(1-.4301)*99/97,.4184,atol=.0001)
close((.4301/2)/((1-.4301)/97),36.61,atol=.01)
close(f_law.sf(36.61,2,97),1.429e-12,rtol=.01)

# Verify citation coverage in the composed article, including copied source blocks.
check(len(re.findall(r'class="cite-ref"',body))>=5)
proper_keys=set(re.findall(r'data-cite-key="([^" ]+)"',body))-{'r_faraway_leafblotch2026'}
check(len(proper_keys)>=2)

for token in ['0.75', '2.5', '3.5', '0.25', '0.5']:
    check(token in body)
check("**Your turn.**" in body)
check(len(re.findall(r"^## Check yourself \{#check-yourself\}",body,re.M))==1)
print(f"{SLUG}: {checks} numerical, algebraic and rendered-content checks passed")
