"""Recompute article examples independently; public lidar data are from SemiPar."""
from pathlib import Path
import re
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT / "articles" / "mixture-discriminant-analysis.qmd").read_text(encoding="utf-8")
assert "Your turn" in text
assert "## Check yourself {#check-yourself}" in text
assert len(re.findall('class="cite-ref"',text))>=5
assert len(set(re.findall('data-cite-key="([^\"]+)',text)))>=2

import math
phi=lambda x,m:math.exp(-(x-m)**2/2)/math.sqrt(2*math.pi)
fA=lambda x:(phi(x,-2)+phi(x,2))/2
fB=lambda x:phi(x,0)
for val,digits,s in [(fA(0)/(fA(0)+fB(0)),6,'0.119203'),(fA(2),9,'0.199538055'),(fB(2),9,'0.053990967'),(fA(2)/(fA(2)+fB(2)),6,'0.787042'),(math.acosh(math.exp(2))/2,6,'1.344268'),(3*math.exp(-2),6,'0.406006'),(3/(math.exp(2)+3),6,'0.288765')]:assert f'{val:.{digits}f}'==s and s in text
x=sp.symbols('x',real=True)
assert sp.simplify((sp.exp(-(x+2)**2/2)+sp.exp(-(x-2)**2/2))/(2*sp.exp(-x**2/2))-sp.exp(-2)*(sp.exp(2*x)+sp.exp(-2*x))/2)==0
assert abs(fA(math.acosh(math.exp(2))/2)-fB(math.acosh(math.exp(2))/2))<1e-14

print("mixture-discriminant-analysis: numerical examples and generated-article assertions passed")
