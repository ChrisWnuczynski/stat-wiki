"""Recompute numerical examples and verify the generated article."""
from pathlib import Path
import math
import re
import numpy as np
from scipy import stats, integrate
ROOT=Path(__file__).resolve().parents[1]
SLUG='a-permutation-test'
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
from itertools import combinations
import subprocess,os,shutil
x=np.array([1,2,4,5]);diffs=[]
for ix in combinations(range(4),2):
 mask=np.zeros(4,dtype=bool);mask[list(ix)]=True
 diffs.append(x[mask].mean()-x[~mask].mean())
close(sorted(diffs),[-3,-1,0,0,1,3]);close(np.mean(np.abs(diffs)>=3),1/3)
# Recompute the seeded InsectSprays shuffle in base R. The chapter block calls
# dplyr and purrr, which the graph job does not install, so this check does not execute it.
r_home=os.environ.get('STATWIKI_R_HOME')
configured_r=Path(r_home)/'bin/exec/R' if r_home else None
rbin=configured_r if configured_r is not None and configured_r.is_file() else shutil.which('R')
assert rbin and Path(rbin).is_file() and os.access(rbin,os.X_OK), 'R executable not found'
script=r'''
counts <- datasets::InsectSprays$count[datasets::InsectSprays$spray %in% c("A","B")]
spray <- droplevels(datasets::InsectSprays$spray[datasets::InsectSprays$spray %in% c("A","B")])
observed <- mean(counts[spray=="A"]) - mean(counts[spray=="B"])
set.seed(1)
permuted <- replicate(1999, {
  label <- sample(spray)
  mean(counts[label=="A"]) - mean(counts[label=="B"])
})
p_mc <- (1 + sum(abs(permuted) >= abs(observed))) / 2000
cat("CHECK", observed, sum(abs(permuted) >= abs(observed)), p_mc, "\n")
'''
run=subprocess.run([str(rbin),'--vanilla','--slave'],input=script,text=True,capture_output=True,check=True)
m=re.search(r'CHECK\s+([-\d.]+)\s+(\d+)\s+([-\d.]+)',run.stdout);assert m,run.stdout
close([float(m[1]),float(m[2]),float(m[3])],[-5/6,1364,.6825],1e-6)
close((1364+1)/2000,.6825);close(1/2000,.0005);close(1/1000,.001)
close(np.sqrt(.6825*(1-.6825)/1999),.01041,.000005)
shown('1364','0.6825','0.01041','1/3','0.001')
finish()
