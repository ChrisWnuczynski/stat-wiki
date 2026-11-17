"""Recompute the displayed examples and practice answers."""
import math
from fractions import Fraction
import numpy as np
from scipy import stats, optimize
from pathlib import Path

Q=np.array([[.5,.25,0,0],[.5,.5,.25,0],[0,.25,.5,.5],[0,0,.25,.5]])
pi=np.array([1,2,2,1])/6
assert np.allclose(Q.sum(0),1) and np.allclose(Q@pi,pi)
assert np.allclose(Q*pi[None,:],(Q*pi[None,:]).T)
assert np.allclose(np.sort(np.linalg.eigvals(Q)),[0,.25,.75,1])
assert np.allclose(Q@Q@np.array([1,0,0,0]),[3/8,1/2,1/8,0]) and (Q@Q)[0,1]==.25
h=np.linalg.solve(np.eye(3)-Q[:3,:3].T,np.ones(3));assert np.allclose(h,[18,16,10])
assert np.allclose(np.linalg.matrix_power(Q,100)[:,0],pi,atol=1e-12)
A=Q.copy();A[:,3]=[0,0,0,1]
assert np.all(np.linalg.matrix_power(A,3)[3,:3]>=1/32)
assert 3/(1/32)==96 and max(h)<96

# Compare recomputed results with the generated worked example and practice answer.
ROOT = Path(__file__).resolve().parents[1]
SLUG = 'four-state-random-walk'
article = (ROOT / "articles" / (SLUG + ".qmd")).read_text(encoding="utf-8")
worked_section = article.split("{#worked-example}", 1)[1].split("\n## ", 1)[0]
worked_example, your_turn = worked_section.split("**Your turn.**", 1)

first=Q@np.array([1,0,0,0]);second=Q@first
render_vector=lambda values: '('+','.join(str(Fraction(float(value)).limit_denominator()) for value in values)+')'
assert 'v_1='+render_vector(first) in worked_example
assert 'v_2='+render_vector(second) in worked_example
practice_probability=Fraction(float((Q@Q)[0,1])).limit_denominator()
assert f"totaling ${practice_probability}$" in your_turn
assert '(h_1,h_2,h_3)=('+','.join(f'{value:.0f}' for value in h)+')' in article

print("four-state-random-walk: numerical checks passed")
