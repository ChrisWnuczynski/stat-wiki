"""Independent numerical and algebraic checks for clotting-time-data."""
import math
from pathlib import Path
import numpy as np


c = np.array([5,10,15,20,30,40,60,80,100.])
y1=np.array([118,58,42,35,27,25,21,19,18.]);y2=np.array([69,35,26,21,18,16,13,12,12.])
X=np.c_[np.ones(9),np.log(c)]
from scipy.optimize import root as solve_root
fits=[solve_root(lambda b:X.T@(1/(X@b)-y),[-.016,.015]) for y in (y1,y2)]
assert all(f.success for f in fits)
assert np.allclose(fits[0].x,[-.01655438,.01534311],atol=5e-9)
assert np.allclose(fits[1].x,[-.02390847,.02359921],atol=5e-9)
assert np.allclose([1/(np.array([1,math.log(10)])@f.x) for f in fits],[53.26388874,32.86152119])
assert abs(1/(-.01655+.01534*math.log(10))-53.27180702)<1e-7
assert abs(1/(-.0239+.0236*math.log(10))-32.85042314)<1e-7
assert .00213*50**2==5.325
assert abs(math.exp(-.08)-.9231163464)<1e-10
assert np.all(X@fits[0].x > 0) and np.all(X@fits[1].x > 0)


# Recompute the displayed joint Gamma fit and the three likelihood scores.
from scipy.stats import t as student_t, gamma as gamma_law
Y=np.r_[y1,y2]
means=np.r_[*[1/(X@f.x) for f in fits]]
assert np.all(means[:9]>means[9:])
phi=float(np.sum(((Y-means)/means)**2)/14)
assert abs(phi-.002129691536505264)<1e-13
fullX=np.vstack([np.c_[np.ones(9),np.zeros(9),np.log(c),np.zeros(9)],
                 np.c_[np.ones(9),np.ones(9),np.log(c),np.log(c)]])
beta=np.array([fits[0].x[0],fits[1].x[0]-fits[0].x[0],fits[0].x[1],fits[1].x[1]-fits[0].x[1]])
se=np.sqrt(np.diag(phi*np.linalg.inv(fullX.T@(means[:,None]**2*fullX))))
ratios=beta/se
pvalues=2*student_t.sf(abs(ratios),14)
assert np.allclose(ratios,[-19.12710008,-4.38278051,39.62604861,11.22848333],atol=1e-8)
assert np.allclose(pvalues,[1.96739824e-11,6.25203161e-4,8.85102903e-16,2.18429429e-8],rtol=1e-8,atol=0)
dev=2*np.sum(-np.log(Y/means)+(Y-means)/means)
disp=dev/18
gamma_aic=-2*gamma_law.logpdf(Y,a=1/disp,scale=means*disp).sum()+10
assert round(float(gamma_aic),1)==63.2
ig_aics=[]
for power in (1,2):
    fitted=[]
    for yy in (y1,y2):
        if power==1:
            bb=np.linalg.solve(X.T@(yy[:,None]*X),X.sum(axis=0))
            mu=1/(X@bb)
        else:
            # Convex canonical objective with line search to keep every predictor positive.
            bb=np.array([.0001,.0001])
            def objective(v):
                eta=X@v
                return np.sum(yy*eta-2*np.sqrt(eta)) if np.min(eta)>0 else np.inf
            for iteration in range(50):
                eta=X@bb; mu=eta**-.5
                grad=X.T@(yy-mu)
                hess=.5*X.T@(eta[:,None]**(-1.5)*X)
                step=np.linalg.solve(hess,grad); step_size=1.
                while objective(bb-step_size*step)>objective(bb):
                    step_size/=2
                    assert step_size>1e-12
                bb=bb-step_size*step
                if np.max(abs(grad))<1e-7:
                    break
            mu=(X@bb)**-.5
            assert np.max(abs(X.T@(yy-mu)))<1e-6
        fitted.extend(mu)
    mm=np.array(fitted)
    ig_phi=np.mean((Y-mm)**2/(Y*mm*mm))
    ll=np.sum(-.5*np.log(2*np.pi*ig_phi*Y**3)-(Y-mm)**2/(2*ig_phi*Y*mm*mm))
    ig_aics.append(-2*ll+10)
assert round(float(ig_aics[0]),1)==60.7
assert round(float(ig_aics[1]),1)==110.5

root=Path(__file__).resolve().parents[1]
body=(root / "articles" / "clotting-time-data.qmd").read_text()
source=(root / "research/content" / "clotting-time-data.md").read_text()
assert "**Your turn.**" in body
assert len(__import__("re").findall(r"\{\{cite:",source)) >= 5
for token in ['53.2718', '32.8504', '53.2639', '5.325']:
    assert token in body, (token, "clotting-time-data")
print("clotting-time-data: numerical and algebraic checks passed")
