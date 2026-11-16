"""Quasi-Poisson numeric and structure checks."""
from math import log,sqrt,isclose
from pathlib import Path
root=Path(__file__).resolve().parents[1]
page=(root/"articles/quasi-poisson.qmd").read_text()
source=(root/"research/content/quasi-poisson.md").read_text()
def near(x,y,tol=5e-5): assert isclose(x,y,abs_tol=tol),(x,y)
near(sum((0,0,6))/3,2)
near(sum((0,0,12))/3,4)
near(4/2,2)
near(log(2),.69315)
near(sum((0-2)**2/2 for _ in range(2))+(6-2)**2/2,12)
near(sum((0-4)**2/4 for _ in range(2))+(12-4)**2/4,24)
near((12+24)/(6-2),9)
near(sqrt(9)*.20,.60)
near(sqrt(4)*.15,.30)
assert all(x in page for x in ('\\phi>1','\\phi<1','\\phi=1'))
assert '::: {.callout-note collapse="true" title="Proof"}' in page
assert '::: {.callout-tip collapse="true" title="Answer"}' in page
assert '## Worked example {#worked-example}' in page
assert 'Lead context' not in source
print("quasi-Poisson checks passed")
