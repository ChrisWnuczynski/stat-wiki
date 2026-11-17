"""Verify primal-dual values, stationarity and two-point classifier bounds."""
from pathlib import Path
import sympy as s
import re
root=Path(__file__).resolve().parents[1]
x,lam=s.symbols("x lam",real=True)
for bound,optlam,optx,value in [(1,2,1,1),(2,4,2,4)]:
    L=x*x+lam*(bound-x)
    xmin=s.solve(s.diff(L,x),x)[0]
    g=s.simplify(L.subs(x,xmin))
    assert xmin==lam/2 and s.diff(g,lam).subs(lam,optlam)==0
    assert g.subs(lam,optlam)==value and xmin.subs(lam,optlam)==optx
assert (lam-lam**2/4).subs(lam,1)==s.Rational(3,4)
a=s.symbols("a",nonnegative=True);dual=2*a-2*a*a
assert s.solve(s.diff(dual,a),a)==[s.Rational(1,2)]
for C,alpha,w,expected in [(1,s.Rational(1,2),1,s.Rational(1,2)),(s.Rational(1,4),s.Rational(1,4),s.Rational(1,2),s.Rational(3,8))]:
    slack=1-w
    primal=s.Rational(w)**2/2+C*2*slack
    assert alpha<=C and w==2*alpha
    assert primal==dual.subs(a,alpha)==expected
X=s.Matrix([[1,1],[1,1]]);y=s.Matrix([1,3]);G=X.T*X
assert set(G.eigenvals())=={0,4}
assert (G+s.eye(2)).inv()*X.T*y==s.Matrix([s.Rational(4,5),s.Rational(4,5)])
body=(root/"articles/dual-problem.qmd").read_text().split("## See also",1)[0]
for text in ["3/4","3/8","4/5","Your turn","## Check yourself {#check-yourself}"]:
    assert text in body,text
assert len(re.findall('class="cite-ref"',body))>=5
for q in ["depth-dual-hard-margin","depth-dual-support-weight"]:assert f"../questions/{q}.qmd" in body
print("dual-problem: exact primal-dual optima, classifier constraints and article checks passed")
