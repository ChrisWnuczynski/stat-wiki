"""Recompute numerical examples and exercise answers for warp-breaks-data."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'warp-breaks-data'
text = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked = text.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
answer = worked.split('title="Answer"}', 1)[1]

import math
import numpy as np
from scipy import stats, special, linalg, integrate

import os,subprocess,json
import shutil
configured_r_home = os.environ.get("STATWIKI_R_HOME")
configured_r = Path(configured_r_home) / "bin" / "exec" / "R" if configured_r_home else None
R = str(configured_r) if configured_r is not None and os.access(configured_r, os.X_OK) else shutil.which("R")
if R is None:
    raise RuntimeError("R is required: configure STATWIKI_R_HOME or install R on PATH")
code=r'''
options(digits=17)
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
assert f"{math.log(655/18):.6f}"=="3.594263" and "3.594263,-0.321320,-0.518488" in text
assert np.isclose(math.exp(math.log(.75))*40,30)
assert round(v[8]/v[11],2)==-2.51 and round(v[8]/v[14],2)==-1.44
assert round(math.exp(3.594))==36 and round(math.exp(-.321),2)==.73 and round(math.exp(-.518),2)==.60
assert np.isclose(.041**2,.001681) and np.isclose(.041**3,.000068921)
assert math.exp(-.5)<1

# Match computed worked-example and practice results to their generated text.
assert '&'.join(f'{z:.4f}' for z in v[[1,3,5]]) in worked
assert '&'.join(f'{z:.4f}' for z in v[[2,4,6]]) in worked
# Exact integer totals avoid R's printed-mean rounding in the independent GLM.
independent_coefs=np.array([math.log(655/18),math.log(475/655),math.log(390/655)])
assert ','.join(f'{z:.6f}' for z in independent_coefs) in worked
assert f'${475/655:.6f}$ and ${390/655:.6f}$' in worked
model_output = text.split("{#interpretation}", 1)[1].split("\n## ", 1)[0]
assert 'refitted coefficients are $'+','.join(f'{z:.6f}' for z in v[7:10])+'$' in model_output
assert f'Pearson scale is ${v[16]:.6f}$' in model_output
assert f'lag-one correlation ${v[21]:.6f}$' in model_output
assert f'40(0.75)={40*math.exp(math.log(.75)):g}$' in answer
assert f'30-40={40*.75-40:g}$' in answer
assert f'working correlation is ${v[17]:.6f}$' in model_output
assert 'approximately $('+','.join(f'{z:.6f}' for z in v[10:13])+')$ and $('+','.join(f'{z:.6f}' for z in v[13:16])+')$' in model_output
assert 'and coefficients $'+','.join(f'{z:.6f}' for z in v[18:21])+'$' in model_output
assert 'gives coefficients $'+','.join(f'{z:.6f}' for z in v[22:25])+'$' in model_output
assert f'and scale ${v[25]:.4f}$' in model_output
# The introductory table and rounded summaries display the same fitted outputs.
definition = text.split("{#definition}", 1)[1].split("\n## ", 1)[0]
table = definition.split('Estimate   Naive SE   Robust SE', 1)[1].split('```', 1)[0]
printed_rows = np.array([[float(z) for z in line.split()[1:]] for line in table.strip().splitlines()])
assert np.array_equal(printed_rows, np.round(np.column_stack([v[7:10], v[10:13], v[13:16]]), 3))
assert f'scale estimate is ${v[16]:.2f}$' in definition
assert f'is about ${v[17]:.3f}$' in definition
assert rf'\exp({v[7]:.3f})\approx {math.exp(v[7]):.0f}' in definition
assert rf'\exp({v[8]:.3f})={math.exp(v[8]):.2f}' in definition
assert rf'\exp({v[9]:.3f})={math.exp(v[9]):.2f}' in definition
assert f'($z={v[8]/v[11]:.2f}$)' in definition
assert f'($z={v[8]/v[14]:.2f}$)' in definition
assert f'lag-1 value is ${v[21]:.3f}$' in definition
assert f'intercept ${v[18]:.3f}$, medium ${v[19]:.3f}$, high ${v[20]:.3f}$' in definition
assert f'coefficients are again ${v[22]:.3f}$, ${v[23]:.3f}$, ${v[24]:.3f}$' in definition
assert f'scale estimate, ${v[25]:.0f}$' in definition
pooled_means=[(v[1]+v[2])/2,(v[3]+v[4])/2,(v[5]+v[6])/2]
assert 'tension means $'+','.join(f'{z:.4f}' for z in pooled_means)+'$' in worked
assert f'about ${v[3]/v[1]:.4f}$ for A and ${v[4]/v[2]:.4f}$ for B' in worked
print("warp-breaks-data: numerical checks passed")
