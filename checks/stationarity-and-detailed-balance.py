"""Detailed-balance and stationary-flow numeric checks."""
from math import isclose
from pathlib import Path
root=Path(__file__).resolve().parents[1]
page=(root/"articles/stationarity-and-detailed-balance.qmd").read_text()
content=(root/"research/content/stationarity-and-detailed-balance.md").read_text()
def near(x,y): assert isclose(x,y,abs_tol=1e-10),(x,y)
P=[[.2,.8,0],[0,.2,.8],[.8,0,.2]]
pi=[1/3]*3
for j in range(3): near(sum(pi[i]*P[i][j] for i in range(3)),pi[j])
near(pi[0]*P[0][1],4/15)
near(pi[1]*P[1][0],0)
near(.4*.3,.12)
near(.6*.2,.12)
Q=[[.5,.25,0,0],[.5,.5,.25,0],[0,.25,.5,.5],[0,0,.25,.5]]
v=[1/6,2/6,2/6,1/6]
for j in range(4): near(sum(Q[j][i]*v[i] for i in range(4)),v[j])
assert sum([1,2,2,1])==6
assert '::: {.callout-note collapse="true" title="Proof"}' in page
assert '::: {.callout-tip collapse="true" title="Answer"}' in page
assert '## Worked example {#worked-example}' in page
assert 'Lead context' not in content
print("stationarity and detailed balance checks passed")
