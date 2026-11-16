"""Quasi-score examples, inherited question and structural checks."""
from math import log,isclose,sqrt
from pathlib import Path
root=Path(__file__).resolve().parents[1]
page=(root/"articles/quasi-score-and-quasi-likelihood.qmd").read_text()
source=(root/"research/content/quasi-score-and-quasi-likelihood.md").read_text()
def near(x,y,tol=5e-5): assert isclose(x,y,abs_tol=tol),(x,y)
near((1+2+3+4)/4,2.5)
near(log(2.5),.91629)
near(sqrt(2.25)*.12,.18)
near(sqrt(9)*.05,.15)
near(sqrt(4)*.10,.20)
near(.20/.10,2)
near(1/2,.5)
near(1/4,.25)
assert page.count('![')>=2
assert '::: {.callout-note collapse="true" title="Proof"}' in page
assert '::: {.callout-tip collapse="true" title="Answer"}' in page
assert '## Worked example {#worked-example}' in page
assert 'Lead context' not in source
print("quasi-score and quasi-likelihood checks passed")
