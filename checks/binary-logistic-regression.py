"""Binary logistic examples and inherited printed numbers."""
from math import exp, isclose
from pathlib import Path

root = Path(__file__).resolve().parents[1]
page = (root / "articles/binary-logistic-regression.qmd").read_text()
content = (root / "research/content/binary-logistic-regression.md").read_text()
def near(a,b,tol=5e-4):
    assert isclose(a,b,abs_tol=tol),(a,b)
def logistic(t): return 1/(1+exp(-t))
near(logistic(-.6),.3543)
near(logistic(.2),.5498)
near(logistic(.2)-logistic(-.6),.1955)
near(exp(.8),2.2255)
near(exp(.5),1.649,.0006)
near(2/11,.182)
near(2/3,.667)
near(-3+.8*4-.4*2,-.6)
near(-3+.8*5-.4*2,.2)
assert '::: {.callout-note collapse="true" title="Proof"}' in page
assert '::: {.callout-tip collapse="true" title="Answer"}' in page
assert '## Worked example {#worked-example}' in page
assert 'Lead context' not in content
print("binary logistic regression checks passed")
