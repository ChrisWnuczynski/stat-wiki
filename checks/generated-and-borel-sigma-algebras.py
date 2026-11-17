"""Recompute the mathematical examples and inspect the generated article."""
from pathlib import Path
import re
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT / "articles" / "generated-and-borel-sigma-algebras.qmd").read_text(encoding="utf-8")
assert "Your turn" in text
assert "## Check yourself {#check-yourself}" in text
assert len(re.findall('class="cite-ref"',text))>=5
assert len(set(re.findall('data-cite-key="([^\"]+)',text)))>=2

from itertools import combinations
omega=set(range(1,7));A={1,2,3};B={3,4}
def atoms(A,B):return [s for s in [A&B,A-B,B-A,omega-(A|B)] if s]
a=atoms(A,B);assert a==[{3},{1,2},{4},{5,6}]
family={frozenset().union(*(a[i] for i in range(len(a)) if mask>>i&1)) for mask in range(1<<len(a))}
assert len(family)==16 and frozenset({1}) not in family
assert len(atoms(A,{1,2}))==3 and 2**3==8
assert 2**2==4 and 2**4==16
for token in ['16','2^3=8','four events']:assert token in text,token

print("generated-and-borel-sigma-algebras: exact calculations and generated-article assertions passed")
