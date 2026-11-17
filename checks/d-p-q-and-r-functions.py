"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

assert round(stats.binom.pmf(3,10,.4),5)==.21499
assert round(stats.binom.cdf(3,10,.4),5)==.38228
assert stats.binom.ppf(.9,10,.4)==6
assert round(stats.binom.cdf(5,10,.4),5)==.83376 and round(stats.binom.cdf(6,10,.4),5)==.94524
assert round(stats.norm.pdf(0),3)==.399 and round(stats.norm.cdf(1.96)-stats.norm.cdf(-1.96),2)==.95
assert round(stats.norm.ppf(.975),2)==1.96
assert 4/6<.75<=5/6
# Execute the displayed R calls, including a reproducible seeded draw.
import os,subprocess,shutil
configured_home = os.environ.get("STATWIKI_R_HOME")
configured_r = Path(configured_home) / "bin" / "exec" / "R" if configured_home else None
r = str(configured_r) if configured_r is not None and configured_r.is_file() and os.access(configured_r, os.X_OK) else shutil.which("R")
if r is None:
 raise RuntimeError("R is required to reproduce the displayed R calculations; configure STATWIKI_R_HOME or put R on PATH")
s='set.seed(1); x<-rbinom(6,10,.4); stopifnot(identical(x,c(3L,3L,4L,6L,3L,6L))); stopifnot(qbinom(.9,10,.4)==6); print(x)'
s += '; stopifnot(abs(dbinom(3,10,.4)-.214990848)<1e-12,abs(pbinom(3,10,.4)-.3822806016)<1e-12); stopifnot(all.equal(dgamma(1,shape=2,rate=3),dgamma(1,shape=2,scale=1/3))); stopifnot(abs(dnorm(0)-1/sqrt(2*pi))<1e-12)'
subprocess.run([str(r),'--slave','-e',s],check=True)
assert math.isclose(stats.binom.cdf(5,10,.4)-stats.binom.cdf(2,10,.4),sum(stats.binom.pmf(np.arange(3,6),10,.4)))

# Compare recomputed results with the generated worked example and practice answer.
ROOT = Path(__file__).resolve().parents[1]
SLUG = 'd-p-q-and-r-functions'
article = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked_section = article.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
worked_example, your_turn = worked_section.split("**Your turn.**", 1)

for value in (stats.binom.pmf(3,10,.4),stats.binom.cdf(3,10,.4),stats.binom.cdf(5,10,.4),stats.binom.cdf(6,10,.4)):
 assert f"{value:.5f}" in worked_example
assert f"90th percentile is {stats.binom.ppf(.9,10,.4):.0f}" in worked_example
practice_mass=Fraction(1,6);practice_cdf=4*practice_mass
assert f"mass is ${practice_mass}$" in your_turn
assert f"4/6={practice_cdf}" in your_turn
assert f"75th percentile is {math.ceil(.75*6)}" in your_turn

print("d-p-q-and-r-functions: numerical checks passed")
