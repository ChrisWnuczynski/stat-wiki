"""Verify printed spline-knot calculations and structure."""
from pathlib import Path
import sympy as sp


body = Path("articles/knot.qmd").read_text().split("## See also", 1)[0]
for token in ("6.375", "18", "-6", "24", "200", "M+4", "10", "30",
              'title="Proof"', 'title="Answer"'):
    assert token in body, token
assert body.count('title="Proof"') == 1

x = sp.symbols("x", real=True)
g_left, g_right = 1 + 2*x, 1 + 2*x + 3*(x-2)**3
for k, val in [(1,3), (2,5), (3,10)]:
    assert sp.simplify((g_left if k <= 2 else g_right).subs(x,k)-val) == 0
assert g_right.subs(x, sp.Rational(5,2)) == sp.Rational(51,8)
for n, val in [(0,5), (1,2), (2,0)]:
    assert sp.diff(g_left,x,n).subs(x,2) == sp.diff(g_right,x,n).subs(x,2) == val
assert sp.diff(g_right,x,3)-sp.diff(g_left,x,3) == 18

f_left, f_right = 2+3*x, 2+3*x-(x-1)**3
for k,val in [(0,2),(1,5),(2,7)]:
    assert (f_left if k <= 1 else f_right).subs(x,k) == val
for n,val in [(0,5),(1,3),(2,0)]:
    assert sp.diff(f_left,x,n).subs(x,1) == sp.diff(f_right,x,n).subs(x,1) == val
assert sp.diff(f_right,x,3)-sp.diff(f_left,x,3) == -6
assert (x+x**3).diff(x,2) == 6*x
print("knot spline arithmetic and structure passed")
