"""Independent numerical and algebraic checks for cycle."""
import math
from pathlib import Path
import numpy as np


t=np.arange(-24,49); seasonal=np.cos(2*np.pi*t/12); other=np.cos(2*np.pi*t/8)
assert np.allclose(seasonal-np.cos(2*np.pi*(t-12)/12),0,atol=1e-13)
assert np.allclose(other-np.cos(2*np.pi*(t-12)/8),2*other,atol=1e-13)
assert abs(1-np.exp(-2j*np.pi*12/8))==2
assert math.lcm(12,8)==24
assert abs(9/(1-.4**2)-75/7)<1e-12
assert .4**2==.16000000000000003

assert .8*10+.2*30==14
assert math.lcm(12,8)==24

root=Path(__file__).resolve().parents[1]
body=(root / "articles" / "cycle.qmd").read_text()
source=(root / "research/content" / "cycle.md").read_text()
assert "**Your turn.**" in body
assert len(__import__("re").findall(r"\{\{cite:",source)) >= 5
for token in ['24', '14']:
    assert token in body, (token, "cycle")
print("cycle: numerical and algebraic checks passed")
