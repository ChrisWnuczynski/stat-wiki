"""Recompute the numerical claims and inspect the generated article."""
from pathlib import Path
import math
from fractions import Fraction
from itertools import combinations
import numpy as np
from scipy import stats
import sympy as sp
ROOT = Path(__file__).resolve().parents[1]
X=np.array([[0,0,0,0],[1,0,1,0],[0,1,0,1]],dtype=float);C=X-X.mean(axis=0);S=C.T@C/2
assert np.linalg.matrix_rank(C)==2 and np.linalg.matrix_rank(S)==2
assert np.allclose(np.linalg.eigvalsh(S),[0,0,1/3,1])
assert np.allclose(np.linalg.eigvalsh(S+.5*np.eye(4)),[.5,.5,5/6,1.5])
assert np.allclose(X@np.array([1,2,0,0]),[0,1,2])
assert np.allclose(X@np.array([0,0,1,2]),[0,1,2])
xnew=np.array([1,0,0,0])
assert xnew@np.array([1,2,0,0])==1 and xnew@np.array([0,0,1,2])==0
assert np.allclose(S@np.array([1,0,-1,0]),0)
assert min(4-1,10)==3 and 10-3==7
assert min(5-1,12)==4 and 12-4==8
assert np.allclose(np.array([3,1,0])+.2,[3.2,1.2,.2])
assert 100-1==99 and 100-2==98
assert 40+22==62 and 2000>62 and 2000*62==124000
assert 5-(3-1)==3

# Deepened research calculations.
assert [v+0.5 for v in (4, 2, 0)] == [4.5, 2.5, 0.5]
assert [v+0.2 for v in (3, 1, 0)] == [3.2, 1.2, 0.2]
assert min(5, 15) == 5 and 15-5 == 10
assert min(4, 12) == 4 and 12-4 == 8

text = (ROOT / "articles" / "high-dimensional-data.qmd").read_text(encoding="utf-8")
assert "## Check yourself {#check-yourself}" in text
assert "Your turn" in text
assert text.count('class="cite-ref"') >= 5
print("high-dimensional-data: all recomputed claims and generated-text checks passed")
