"""Regression diagnostics checks (gap batch 3).
Reproduces Cook & Weisberg (1982) rat data (Table 3.5.2): Table 3.5.3(b) coefficients/t-values,
D_3 = 0.93, v_33 = 0.85, other D_i < 0.27 (p. 120); Example 3.5.1 (p. 118) D_i = 3.0 for four (r_i, v_ii) pairs;
Anscombe (1973, p. 19) printed summary for all four data sets and the set-3 line y = 4 + 0.346x."""
import numpy as np
from scipy import stats

def fit(X, y):
    X = np.column_stack([np.ones(len(y)), X])
    n, p = X.shape
    XtXi = np.linalg.inv(X.T @ X)
    b = XtXi @ X.T @ y
    H = X @ XtXi @ X.T
    h = np.diag(H)
    e = y - X @ b
    s2 = e @ e / (n - p)
    se = np.sqrt(np.diag(XtXi) * s2)
    with np.errstate(divide='ignore', invalid='ignore'):
        r = e / np.sqrt(s2 * (1 - h))
        D = r**2 * h / (p * (1 - h))
        s2i = ((n - p) * s2 - e**2 / (1 - h)) / (n - p - 1)
        t = e / np.sqrt(s2i * (1 - h))
    return dict(b=b, se=se, tval=b/se, h=h, e=e, s2=s2, r=r, D=D, t=t, n=n, p=p)

rat = np.array([
 [176,6.5,0.88,0.42],[176,9.5,0.88,0.25],[190,9.0,1.00,0.56],[176,8.9,0.88,0.23],[200,7.2,1.00,0.23],
 [167,8.9,0.83,0.32],[188,8.0,0.94,0.37],[195,10.0,0.98,0.41],[176,8.0,0.88,0.33],[165,7.9,0.84,0.38],
 [158,6.9,0.80,0.27],[148,7.3,0.74,0.36],[149,5.2,0.75,0.21],[163,8.4,0.81,0.28],[170,7.2,0.85,0.34],
 [186,6.8,0.94,0.28],[146,7.3,0.73,0.30],[181,9.0,0.90,0.37],[149,6.4,0.75,0.46]])
X, y = rat[:, :3], rat[:, 3]
print("== Rat data, Y on X1,X2,X3 (CW1982 Table 3.5.3(b), last column: 0.266(1.37), -0.0212(-2.67), 0.0143(0.83), 4.178(2.74))")
f = fit(X, y)
print(" coef", np.round(f['b'], 4), " t", np.round(f['tval'], 2))
print(" D_3 =", round(f['D'][2], 2), " v_33 =", round(f['h'][2], 2), " max other D =", round(np.delete(f['D'], 2).max(), 3))
print(" r_i range", np.round(f['r'].min(), 2), np.round(f['r'].max(), 2), " r_3 =", round(f['r'][2], 3), " t_3 =", round(f['t'][2], 3))
print(" sum h = p' =", round(f['h'].sum(), 6), " mean h =", round(f['h'].mean(), 4), " 2p'/n =", round(2*4/19, 3))
F50 = stats.f.ppf(0.5, 4, 15); print(" F(0.5; 4, 15) =", round(F50, 3), "; D_3 percentile of F(4,15):", round(stats.f.cdf(f['D'][2], 4, 15), 3))
for j, name in enumerate(["X1", "X2", "X3"]):
    g = fit(X[:, j], y); print(f" simple regression on {name}: t = {g['tval'][1]:.2f}")
keep = np.arange(19) != 2
g = fit(X[keep], y[keep]); print(" case 3 deleted: coef", np.round(g['b'], 4), " t", np.round(g['tval'], 2))
print(" body weight vs dose correlation:", round(np.corrcoef(X[:,0], X[:,2])[0,1], 3), "(printed 0.990)")

print("== CW1982 Example 3.5.1 (p'=3, n=100): D = r^2 v /(p'(1-v))")
for e_, v, r_ in [(0.6325,0.9,1.0),(1.732,0.75,1.732),(9.0,0.25,5.196),(19.087,0.1,9.0)]:
    print("  v=%.2f r=%.3f D=%.3f" % (v, r_, r_**2 * v / (3*(1-v))))

ax = np.array([10,8,13,9,11,14,6,4,12,7,5], float)
Y = {1:[8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68],
     2:[9.14,8.14,8.74,8.77,9.26,8.10,6.13,3.10,9.13,7.26,4.74],
     3:[7.46,6.77,12.74,7.11,7.81,8.84,6.08,5.39,8.15,6.42,5.73]}
x4 = np.array([8,8,8,8,8,8,8,19,8,8,8], float); y4 = np.array([6.58,5.76,7.71,8.84,8.47,7.04,5.25,12.50,5.56,7.91,6.89])
print("== Anscombe 1973 p.19 printed: n=11, xbar 9.0, ybar 7.5, y=3+0.5x, Sxx 110, SSreg 27.50, RSS 13.75, SE(b1) .118, R2 .667")
for k in [1,2,3,4]:
    x = ax if k < 4 else x4; yy = np.array(Y[k]) if k < 4 else y4
    f = fit(x, yy); sxx = ((x-x.mean())**2).sum(); rss = (f['e']**2).sum(); tss = ((yy-yy.mean())**2).sum()
    with np.errstate(invalid='ignore'):
        print(f" set {k}: b0={f['b'][0]:.3f} b1={f['b'][1]:.4f} ybar={yy.mean():.3f} Sxx={sxx:.1f} SSreg={tss-rss:.3f} RSS={rss:.3f} SE={f['se'][1]:.4f} R2={1-rss/tss:.3f}")
        i = np.nanargmax(np.where(np.isfinite(f['D']), f['D'], -1)); print(f"   max h={f['h'].max():.3f} (case {f['h'].argmax()+1}); max finite D={f['D'][i]:.3f} (case {i+1}); r={f['r'][i]:.3f}; t={f['t'][i]:.3f}")
# Set 3 line through the 10 non-outlying points
m = np.arange(11) != 2
b = np.polyfit(ax[m], np.array(Y[3])[m], 1); print(" set 3 without obs 3: y = %.4f + %.4f x (printed 4 + 0.346x)" % (b[1], b[0]))
