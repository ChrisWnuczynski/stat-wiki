"""Recompute the worked calculations and inspect the generated article."""
from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
source = (root / "research" / "content" / (Path(__file__).stem + ".md")).read_text()
article = (root / "articles" / (Path(__file__).stem + ".qmd")).read_text()
body = article.split("## See also", 1)[0]
assert len(re.findall(r"\{\{cite:", source)) >= 5
assert len(set(re.findall(r"\{\{cite:([^}]+)", source))) >= 2
assert "Your turn" in body and 'collapse="true"' in body

from math import log, exp
ages=[71, 158, 128, 2, 1, 1, 61, 37, 113, 59, 82, 148, 18, 1, 168, 1, 78, 175, 80, 27, 22, 105, 96, 131, 15, 9, 8, 100, 4, 151, 31, 125, 130, 112, 140, 93, 1, 52, 20, 91, 73, 35, 143, 61, 97, 139, 136, 131, 121, 177, 68, 9, 139, 2, 140, 72, 2, 120, 51, 102, 130, 114, 81, 118, 118, 17, 195, 159, 18, 15, 158, 127, 87, 206, 11, 178, 157, 26, 120, 42, 36]
y=[0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
assert len(y)==81 and sum(y)==17 and len(y)-sum(y)==64
assert min(ages)==1 and max(ages)==206
p=sum(y)/len(y)
eta=log(p/(1-p))
assert abs(p-.20987654320987653)<1e-14
assert abs(eta+1.3256697393034558)<1e-14
assert abs(exp(eta)-.265625)<1e-14
assert abs(exp(eta)/(1+exp(eta))-p)<1e-14
assert abs(17/p-64/(1-p))<1e-12
for number in ['17','64','0.209877','-1.325670','206','0.265625']:
    assert number in body


# Refit the chapter's smooth with R, mgcv and rpart. STATWIKI_R_HOME can point
# to a portable R tree; the shared source cache supplies one in this workspace.
import os
import shutil
import subprocess
r_home = os.environ.get('STATWIKI_R_HOME')
portable = root.parent / 'statwiki-sources/r-runtime/extracted/usr/lib/R'
r_bin = shutil.which('R')
r_env = os.environ.copy()
if r_home or (not r_bin and portable.is_dir()):
    r_home = Path(r_home) if r_home else portable
    r_bin = str(r_home / 'bin/exec/R')
    r_env['R_HOME'] = str(r_home)
    r_env['R_LIBS_SITE'] = str(r_home / 'library')
    r_env['LD_LIBRARY_PATH'] = str(r_home / 'lib') + ':' + r_env.get('LD_LIBRARY_PATH', '')
for number in ['2.223', '6.356', '0.0762', '-1.509193', '2.805577']:
    assert number in body, number

def _r_ready() -> bool:
    if not r_bin:
        return False
    if not Path(r_bin).is_file() and shutil.which(str(r_bin)) is None:
        return False
    probe = subprocess.run(
        [r_bin, '--vanilla', '--slave'],
        input='suppressPackageStartupMessages(library(mgcv)); suppressPackageStartupMessages(library(rpart)); cat("ok\\n")',
        text=True, capture_output=True, env=r_env,
    )
    return probe.returncode == 0 and "ok" in probe.stdout

if not _r_ready():
    print("kyphosis-data: skipping the mgcv refit because R, mgcv, or rpart is unavailable. The arithmetic checks above still ran. CI installs R 4.5.0 with mgcv 1.9-3 and rpart 4.1.24.")
    raise SystemExit(0)
r_code = r'''
suppressPackageStartupMessages(library(mgcv))
suppressPackageStartupMessages(library(rpart))
data(kyphosis, package="rpart")
kyphosis$Kyphosis <- as.numeric(kyphosis$Kyphosis == "present")
fit <- gam(Kyphosis ~ s(Age), family=binomial, data=kyphosis)
s <- summary(fit)
cat(sprintf("%.12f", c(s$s.table[1,],s$p.table[1,1:3])), sep=",")
'''
r_result = subprocess.run([r_bin, '--vanilla', '--slave'], input=r_code,
                          text=True, capture_output=True, check=True, env=r_env)
actual = [float(x) for x in r_result.stdout.strip().split(',')]
expected = [2.22344180416414, 2.80557721914319, 6.35590636926641,
            .0762373466512047, -1.50919301706596, .315970050052515,
            -4.77637996644027]
assert len(actual) == len(expected)
for observed, target in zip(actual, expected):
    assert abs(observed-target) < 5e-6, (observed,target)

print("kyphosis-data checks passed")
print('kyphosis mgcv smooth-fit checks passed')
