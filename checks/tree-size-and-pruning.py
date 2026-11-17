"""Recompute numerical examples and exercise answers for tree-size-and-pruning."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'tree-size-and-pruning'
text = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked = text.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
answer = worked.split('title="Answer"}', 1)[1]

import math
import numpy as np
from scipy import stats, special, linalg, integrate

risks=np.array([20,8,4]);leaves=np.array([1,3,5])
for alpha,expected in [(0,5),(1,5),(3,3),(5,3),(7,1)]:assert leaves[np.argmin(risks+alpha*leaves)]==expected
assert np.allclose(risks+4*leaves,[24,20,24])
assert (15-6)/(4-1)==3
assert 6+2*4==14 and 15+2==17 and 6+4*4==22 and 15+4==19
import os,subprocess
import shutil
configured_r_home = os.environ.get("STATWIKI_R_HOME")
configured_r = Path(configured_r_home) / "bin" / "exec" / "R" if configured_r_home else None
R = str(configured_r) if configured_r is not None and os.access(configured_r, os.X_OK) else shutil.which("R")
if R is None:
    raise RuntimeError("R is required: configure STATWIKI_R_HOME or install R on PATH")
code='library(rpart);for (small in c(FALSE,TRUE)) for(cp in c(.1,.001)){ctrl<-if(small)rpart.control(cp=cp,xval=0,minsplit=2,minbucket=1) else rpart.control(cp=cp,xval=0);f<-rpart(Species~Petal.Length+Petal.Width,iris,method="class",control=ctrl);cat(sum(f$frame$var=="<leaf>")," ")}'
out=subprocess.run([R,'--vanilla','--slave','-e',code],capture_output=True,text=True,check=True)
assert list(map(int,out.stdout.split()))==[3,3,3,7]
assert 2.5<3

# Match computed worked-example and practice results to their generated text.
first_cross=(risks[1]-risks[2])/(leaves[2]-leaves[1]);second_cross=(risks[0]-risks[1])/(leaves[1]-leaves[0])
assert rf"\alpha={first_cross:g}" in worked and rf"\alpha={second_cross:g}" in worked
assert f"three-leaf score is ${risks[1]+4*leaves[1]:g}$" in worked
assert f"threshold is $(15-6)/(4-1)={(15-6)/(4-1):g}$" in answer
assert f"scores are ${6+4*4}$ and ${15+4}$" in answer
leaf_counts=list(map(int,out.stdout.split()));count_words={3:'three',7:'seven'}
assert f"give {count_words[leaf_counts[2]]} and {count_words[leaf_counts[3]]} leaves respectively" in text
print("tree-size-and-pruning: numerical checks passed")
