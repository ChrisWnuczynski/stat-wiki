"""Poisson-process example and inherited numeric checks."""
from math import exp, factorial, isclose
from pathlib import Path
root=Path(__file__).resolve().parents[1]
page=(root/"articles/homogeneous-poisson-process.qmd").read_text()
source=(root/"research/content/homogeneous-poisson-process.md").read_text()
def near(x,y,tol=5e-4): assert isclose(x,y,abs_tol=tol),(x,y)
near(exp(-2)*2**2/factorial(2),.27067)
near(exp(-.5),.60653)
near(exp(-1),.368)
near(1-2*exp(-1),.264)
near(3*(2/3),2)
near(3*(1/6),.5)
near(exp(-1.5)*1.5**2/2,exp(-1.5)*1.125)
assert '::: {.callout-note collapse="true" title="Proof"}' in page
assert '::: {.callout-tip collapse="true" title="Answer"}' in page
assert '## Worked example {#worked-example}' in page
assert 'Lead context' not in source
print("homogeneous Poisson process checks passed")
