"""Analysis of covariance checks (gap batch 3).
Reproduces Oehlert (2010) Table 17.1 / Listing 17.1, pp. 456-459: covariate ANOVA F=1.45 p=.286;
ANCOVA type F=11.64 (2,8) p=.004; x F=24.79; slope 1.8199 (SE .3655); adjusted means 73.57, 54.50, 49.44
(SE 3.641, 3.722, 3.943); unadjusted MSE 187.2 vs 51.4 ("about 3.6 times"); Tukey 1-2 centre -19.07."""
import numpy as np
from scipy import stats

x = np.array([60,72,61,50, 54,68,66,59, 56,56,55,51], float)
y = np.array([85,95,69,58, 41,74,71,52, 41,34,50,40], float)
g = np.repeat([0,1,2], 4)

def ols(X, y):
    b, *_ = np.linalg.lstsq(X, y, rcond=None); e = y - X @ b
    return b, e @ e
one = np.ones(12); D = np.column_stack([(g == k).astype(float) for k in range(3)])
# covariate ANOVA
_, sse_x = ols(np.column_stack([one, D[:, 1:]]), x); sst_x = ((x - x.mean())**2).sum()
Fx = ((sst_x - sse_x)/2)/(sse_x/9); print("covariate ANOVA: SS type %.2f SSE %.2f F %.2f p %.3f" % (sst_x-sse_x, sse_x, Fx, stats.f.sf(Fx, 2, 9)))
print("covariate means", [x[g == k].mean() for k in range(3)])
# models
b_full, sse_full = ols(np.column_stack([D, x]), y)           # parallel lines
_, sse_line = ols(np.column_stack([one, x]), y)              # single line
_, sse_trt = ols(D, y)                                       # treatments only
mse = sse_full / 8
F_trt = ((sse_line - sse_full)/2)/mse; F_x = (sse_trt - sse_full)/mse
print("ANCOVA: SSE %.1f MSE %.1f | adj SS type %.1f F %.2f p %.4f | adj SS x %.1f F %.2f p %.4f" % (
    sse_full, mse, sse_line - sse_full, F_trt, stats.f.sf(F_trt, 2, 8), sse_trt - sse_full, F_x, stats.f.sf(F_x, 1, 8)))
beta = b_full[3]; xbar = x.mean()
adj = b_full[:3] + beta * xbar
X = np.column_stack([D, x]); XtXi = np.linalg.inv(X.T @ X)
se_beta = np.sqrt(XtXi[3, 3] * mse)
se_adj = [np.sqrt(np.r_[np.eye(3)[k], xbar] @ XtXi @ np.r_[np.eye(3)[k], xbar] * mse) for k in range(3)]
print("slope %.4f SE %.4f; xbar %.2f; adjusted means %s; SEs %s" % (beta, se_beta, xbar, np.round(adj, 3), np.round(se_adj, 3)))
# effects (sum-to-zero) as Minitab: mu + alpha_i ; alpha1 printed 14.399, alpha2 -4.671, constant -48.21
mu = b_full[:3].mean(); print("effects: constant %.2f alpha %s" % (mu, np.round(b_full[:3] - mu, 3)))
print("check: -48.21 + 14.399 + 1.8199*59 =", round(-48.21 + 14.399 + 1.8199*59, 2))
raw = [y[g == k].mean() for k in range(3)]; mse0 = sse_trt / 9
F0 = ((((y - y.mean())**2).sum() - sse_trt)/2)/mse0
print("no covariate: raw means %s MSE %.1f F %.2f p %.3f; ratio MSE %.2f" % (raw, mse0, F0, stats.f.sf(F0, 2, 9), mse0/mse))
# adjustment = beta*(xbar_i - xbar)
print("adjustment beta*(xbar_i - xbar):", np.round([beta*(x[g==k].mean()-xbar) for k in range(3)], 3), " raw - adj:", np.round(np.array(raw)-adj, 3))
# Tukey for adjusted difference 1-2 (Minitab-type: q * SE(diff)/sqrt2 with df 8)
from scipy.stats import studentized_range
q = studentized_range.ppf(0.95, 3, 8)
c = np.r_[1, -1, 0, 0]; se_d = np.sqrt(c @ XtXi @ c * mse)
print("adj diff 2-1 = %.2f, Tukey half-width %.2f -> (%.2f, %.2f) [printed -33.59, -19.07, -4.553]" % (adj[1]-adj[0], q/np.sqrt(2)*se_d, adj[1]-adj[0]-q/np.sqrt(2)*se_d, adj[1]-adj[0]+q/np.sqrt(2)*se_d))
# separate slopes check (homogeneity of slopes) - our own extension
Xs = np.column_stack([D, D * x[:, None]]); _, sse_sep = ols(Xs, y)
Fs = ((sse_full - sse_sep)/2)/(sse_sep/6); print("our extension, equal-slopes test: F %.3f on (2,6) p %.3f" % (Fs, stats.f.sf(Fs, 2, 6)))
# Fisher (DoE §57, pp. 173-174): adjustment = error sum of products / error sum of squares of x
Exy = sum(((x[g==k]-x[g==k].mean())*(y[g==k]-y[g==k].mean())).sum() for k in range(3))
Exx = sum(((x[g==k]-x[g==k].mean())**2).sum() for k in range(3)); Eyy = sum(((y[g==k]-y[g==k].mean())**2).sum() for k in range(3))
print("Fisher pooled within slope Exy/Exx = %.4f ; adjusted error SS Eyy - Exy^2/Exx = %.1f (= SSE 411.0)" % (Exy/Exx, Eyy - Exy**2/Exx))
