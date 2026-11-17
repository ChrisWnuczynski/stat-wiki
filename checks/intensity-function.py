"""Independent numerical and algebraic checks for intensity-function."""
import math
from pathlib import Path
import numpy as np


from scipy.integrate import quad
assert abs(quad(lambda u:2*u,0,2)[0]-4)<1e-14
assert abs(quad(lambda u:2*u,2,3)[0]-5)<1e-14
assert abs(math.exp(-4)-.01831563888873418)<1e-15
assert abs(4*math.exp(-4)-.07326255555493671)<1e-15
assert abs(math.exp(-5)-.006737946999085467)<1e-15
assert abs(math.sqrt(4+math.log(2))-2-.16636727739318147)<1e-14
assert abs(math.exp(-((2+.16636727739318147)**2-4))-.5)<1e-14

assert abs(math.exp(-1.5)*1.5**2/2-.25102143016698353)<1e-14

root=Path(__file__).resolve().parents[1]
body=(root / "articles" / "intensity-function.qmd").read_text()
source=(root / "research/content" / "intensity-function.md").read_text()
assert "**Your turn.**" in body
assert len(__import__("re").findall(r"\{\{cite:",source)) >= 5
for token in ['0.0183156', '0.0732626', '0.00673795', '0.166367']:
    assert token in body, (token, "intensity-function")
print("intensity-function: numerical and algebraic checks passed")
