"""Recompute worked examples and inspect generated mathematical claims."""
from pathlib import Path
import re
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT / "articles" / "linear-images-of-a-normal-vector.qmd").read_text(encoding="utf-8")
assert "Your turn" in text
assert "## Check yourself {#check-yourself}" in text
assert len(re.findall('class="cite-ref"',text))>=5
assert len(set(re.findall('data-cite-key="([^\"]+)',text)))>=2

mu=sp.Matrix([1,2]);S=sp.Matrix([[4,1],[1,9]]);A=sp.Matrix([[1,1],[1,-1]])
assert A*mu==sp.Matrix([3,-1])
assert A*S*A.T==sp.Matrix([[15,-5],[-5,11]])
assert f'{float(-5/sp.sqrt(165)):.6f}'=='-0.389249' and '-0.389249' in text
B=sp.Matrix([[1,0],[2,0]]);C=B*S*B.T
assert B*mu==sp.Matrix([1,2]) and C==sp.Matrix([[4,8],[8,16]]) and C.rank()==1
assert 3+4==7
assert '15&-5' in text and '-5&11' in text

print("linear-images-of-a-normal-vector: symbolic/numerical recomputation and article assertions passed")
