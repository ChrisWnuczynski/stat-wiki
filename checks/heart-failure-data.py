"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

import os,subprocess,shutil,csv
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
configured_home = os.environ.get("STATWIKI_R_HOME")
configured_r = Path(configured_home) / "bin" / "exec" / "R" if configured_home else None
r = str(configured_r) if configured_r is not None and configured_r.is_file() and os.access(configured_r, os.X_OK) else shutil.which("R")
if r is None:
 raise RuntimeError("R is required to reproduce the displayed R calculations; configure STATWIKI_R_HOME or put R on PATH")
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

# Compare recomputed results with the generated worked example and practice answer.
ROOT = Path(__file__).resolve().parents[1]
SLUG = 'heart-failure-data'
article = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked_section = article.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
worked_example, your_turn = worked_section.split("**Your turn.**", 1)

annual_odds=math.exp(.04618);decade_odds=annual_odds**10
updated_probability=decade_odds*.2/(.8+decade_odds*.2)
for value in (annual_odds,decade_odds,updated_probability,96/len(rows),203/len(rows)):
 assert f"{value:.4f}" in worked_example
practice_probability=2*.25/(.75+2*.25)
assert f"={practice_probability:.1f}" in your_turn
assert f"${practice_probability-.25:.2f}$" in your_turn
# Bind the independently refitted R output to the published coefficient table.
for coefficient in (-3.70568,.04618,.26920):
 assert f"{coefficient:.5f}" in article
for value in (375.35,354.97,360.97):
 assert f"{value:.2f}" in article

print("heart-failure-data: numerical checks passed")
