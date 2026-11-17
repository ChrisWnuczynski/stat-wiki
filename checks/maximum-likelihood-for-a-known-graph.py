"""Recompute article examples independently; public lidar data are from SemiPar."""
from pathlib import Path
import re
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT / "articles" / "maximum-likelihood-for-a-known-graph.qmd").read_text(encoding="utf-8")
assert "Your turn" in text
assert "## Check yourself {#check-yourself}" in text
assert len(re.findall('class="cite-ref"',text))>=5
assert len(set(re.findall('data-cite-key="([^\"]+)',text)))>=2

S=sp.Matrix([[1,sp.Rational(2,5),sp.Rational(3,10)],[sp.Rational(2,5),1,sp.Rational(1,2)],[sp.Rational(3,10),sp.Rational(1,2),1]])
W=S.copy();W[0,2]=W[2,0]=sp.Rational(1,5)
T=sp.Matrix([[sp.Rational(25,21),-sp.Rational(10,21),0],[-sp.Rational(10,21),sp.Rational(32,21),-sp.Rational(2,3)],[0,-sp.Rational(2,3),sp.Rational(4,3)]])
assert W*T==sp.eye(3)
assert [W[:i,:i].det() for i in range(1,4)]==[1,sp.Rational(21,25),sp.Rational(63,100)]
assert sp.Rational(1,5)*sp.Rational(3,5)==sp.Rational(3,25)
# The copied sweep uses the same three-variable sample matrix.
assert S[0,1]/W[1,1]==sp.Rational(2,5) and S[0,1]*S[1,2]/S[1,1]==sp.Rational(1,5)
# Independently recompute the four-variable chain example if present.
S4=sp.Matrix([[sp.Rational(v) for v in row] for row in [['.8088','.3166','.2911','.1228'],['.3166','.5490','.4638','.2318'],['.2911','.4638','.9569','.5472'],['.1228','.2318','.5472','.8223']]])
W4=S4.copy()
for i,j in [(0,2),(1,3),(0,3)]:
 W4[i,j]=W4[j,i]=sp.prod(S4[k,k+1] for k in range(i,j))/sp.prod(S4[k,k] for k in range(i+1,j))
assert [f'{float(W4[i,j]):.4f}' for i,j in [(0,2),(0,3),(1,3)]]==['0.2675','0.1529','0.2652']
assert all(W4.inv()[i,j]==0 for i in range(4) for j in range(4) if abs(i-j)>1)
assert f'{float(S4[0,1]/S4[1,1]):.3f}'=='0.577'
for token in ['25/21','32/21','63/100','3/25']:assert token in text,token

print("maximum-likelihood-for-a-known-graph: numerical examples and generated-article assertions passed")
