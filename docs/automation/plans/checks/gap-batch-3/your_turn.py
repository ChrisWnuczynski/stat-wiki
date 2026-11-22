"""'Your turn' answers for gap batch 3 (numbers differ from each worked example)."""
import numpy as np
from scipy import stats
from math import sqrt
from mcnemar import tests

print("== McNemar, Your turn: Cavo et al. via Fagerland (2013) Table 2: CR before 65/161, after 75/161; discordant 6 (CR->no CR), 16 (no CR->CR)")
r = tests(6, 16); print({k: round(float(v), 4) for k, v in r.items()}, "| diff in proportions", round(75/161 - 65/161, 4))

print("== Regression diagnostics, Your turn: x = 1,2,3,4,5,10 ; y = 1.2,1.9,3.2,3.8,5.1,7.0")
x = np.array([1,2,3,4,5,10.]); y = np.array([1.2,1.9,3.2,3.8,5.1,7.0])
X = np.column_stack([np.ones(6), x]); XtXi = np.linalg.inv(X.T@X); b = XtXi@X.T@y; h = np.diag(X@XtXi@X.T)
e = y - X@b; n, p = X.shape; s2 = e@e/(n-p); r = e/np.sqrt(s2*(1-h)); D = r**2*h/(p*(1-h))
print(" fit b0=%.4f b1=%.4f s2=%.5f" % (b[0], b[1], s2)); print(" h", np.round(h, 4), " sum", h.sum()); print(" r", np.round(r, 3)); print(" D", np.round(D, 3))
print(" h_66 by formula 1/n + (x-xbar)^2/Sxx =", 1/6 + (10-x.mean())**2/((x-x.mean())**2).sum())
bm = np.polyfit(x[:5], y[:5], 1); print(" without case 6: slope %.4f intercept %.4f; prediction at x=10: %.3f" % (bm[0], bm[1], bm[1]+10*bm[0]))
print(" F(0.5; 2, 4) =", round(stats.f.ppf(.5, 2, 4), 3))

print("== ANCOVA, Your turn: two teaching methods, pre-test x and post-test y (constructed)")
xa = np.array([10,12,14,16.]); ya = np.array([20,23,25,29.]); xb = np.array([14,16,18,20.]); yb = np.array([21,24,26,29.])
x = np.r_[xa, xb]; y = np.r_[ya, yb]; gB = np.r_[np.zeros(4), np.ones(4)]
Exx = ((xa-xa.mean())**2).sum() + ((xb-xb.mean())**2).sum(); Exy = ((xa-xa.mean())*(ya-ya.mean())).sum() + ((xb-xb.mean())*(yb-yb.mean())).sum()
beta = Exy/Exx; xbar = x.mean()
adjA = ya.mean() - beta*(xa.mean()-xbar); adjB = yb.mean() - beta*(xb.mean()-xbar)
print(" raw means A %.3f B %.3f (B-A %.3f); pooled slope %.4f; adjusted A %.3f B %.3f (B-A %.3f)" % (ya.mean(), yb.mean(), yb.mean()-ya.mean(), beta, adjA, adjB, adjB-adjA))
Xf = np.column_stack([np.ones(8), gB, x]); bf, *_ = np.linalg.lstsq(Xf, y, rcond=None); ef = y - Xf@bf; sse = ef@ef; mse = sse/5
se = np.sqrt(np.linalg.inv(Xf.T@Xf)[1,1]*mse); tB = bf[1]/se
print(" regression check: group coef %.4f SE %.4f t %.3f p %.4f; SSE %.4f on 5 df" % (bf[1], se, tB, 2*stats.t.sf(abs(tB), 5), sse))
t0 = stats.ttest_ind(yb, ya); print(" ignoring x: two-sample t %.3f p %.3f" % (t0.statistic, t0.pvalue))
print(" covariate means A %.1f B %.1f" % (xa.mean(), xb.mean()))
