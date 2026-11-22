"""68-95-99.7 rule checks (gap batch 3).
Reproduces: OpenIntro 4e §4.1.5 Guided Practice 4.20 footnote (0.6827, 0.9545, 0.9973; 4 sd about 1 in 15,000,
5 sd about 1 in 2 million, 6 sd 1 in 500 million); McNemar (1955) pp. 26, 34 (68.26, 95.45, 99.73, 99.9936 %);
de Moivre (1756) pp. 246-248 (0.682688 for +-sqrt(n)/2; 0.95428 for +-sqrt(n); 0.99874 for +-3sqrt(n)/2;
n = 3600: 1770..1830 has probability 0.682688; Odds 28 to 13; 21 to 1; 369 to 1);
Grinstead & Snell p. 215 (within 2 sd: .9544) and p. 359 (within 3 sd .997)."""
from math import erf, sqrt, exp
from scipy.stats import norm, binom, expon, uniform

for k in [1, 2, 3, 4, 5, 6]:
    p = 2*norm.cdf(k) - 1
    print(f"k={k}: within {p:.6f}  outside {1-p:.3e}  (1 in {1/(1-p):,.0f})  Chebyshev lower bound {max(0,1-1/k**2):.4f}")
print("de Moivre printed: 0.682688 / 0.95428 / 0.99874; odds 28:13 =", round(28/41, 4), " 21:1 =", round(21/22, 4), " 369:1 =", round(369/370, 5))
print("de Moivre 3-sigma error vs true: ", round(0.99874 - (2*norm.cdf(3)-1), 5))
n = 3600; mu, sd = 1800, 30
for k in [1, 2, 3]:
    lo, hi = mu - k*sd, mu + k*sd
    exact = binom.cdf(hi, n, .5) - binom.cdf(lo-1, n, .5)
    plain = 2*norm.cdf(k) - 1
    cc = norm.cdf((hi+.5-mu)/sd) - norm.cdf((lo-.5-mu)/sd)
    print(f"n=3600, {lo}..{hi}: exact binomial {exact:.6f}  normal {plain:.6f}  with continuity correction {cc:.6f}")
# skewed counterexample: Exponential(1), mean 1, sd 1
for k in [1, 2, 3]:
    p = expon.cdf(1+k) - expon.cdf(max(0, 1-k)); print(f"Exponential(1) within {k} sd: {p:.4f}")
# Your turn: Uniform(0,1)
s = 1/sqrt(12)
for k in [1, 2, 3]:
    p = min(1, 2*k*s); print(f"Uniform(0,1) within {k} sd (sd={s:.4f}): {p:.4f}")
# Normal notation throughout: N(mean, variance), with SDs stated explicitly.
print("N(1100,200^2), SD 200: rule says 700..1500 ~ 95%, 1100..1500 ~ 47.5%; exact",
      round(norm.cdf(2) - norm.cdf(-2), 4), round(norm.cdf(2) - norm.cdf(0), 4))
# Check yourself: heights N(170, 10^2), SD 10: above 190
print("N(170,10^2), SD 10: rule says above 190 ~ 2.5%; exact", round(norm.sf(2), 4))
# Check yourself: Chebyshev's 2-sd bound is attained: X = -2, 0, 2 with probs 1/8, 3/4, 1/8
import numpy as np
v = np.array([-2, 0, 2.]); pr = np.array([1/8, 3/4, 1/8]); m = (v*pr).sum(); sd = np.sqrt(((v-m)**2*pr).sum())
print("three-point: mean", m, "sd", sd, "P(|X-mu| < 2sd) =", pr[np.abs(v-m) < 2*sd].sum())
assert m == 0 and sd == 1
assert pr[np.abs(v-m) < 2*sd].sum() == 0.75
inclusive = pr[np.abs(v-m) <= 2*sd].sum()
assert inclusive == 1
print("three-point: P(|X-mu| <= 2sd) =", inclusive)
# Fitted sample band: nine observations near 0 and one near 10.
# At the limiting configuration all inclusion/exclusion inequalities are strict.
# Continuity preserves the count in an open neighborhood; every nondegenerate
# Gaussian product density is positive there. No binomial model for this count.
sample = np.array([0.] * 9 + [10.])
sample_mean = sample.mean(); sample_sd = sample.std(ddof=1)
distance = np.abs(sample - sample_mean)
assert sample_mean == 1 and np.isclose(sample_sd, sqrt(10))
assert np.count_nonzero(distance < sample_sd) == 9
margin = np.min(np.abs(distance - sample_sd))
assert margin > 0
print("fitted one-sample-SD band (n=10, ddof=1): mean", sample_mean,
      "SD", sample_sd, "inside", np.count_nonzero(distance < sample_sd),
      "strict margin", margin)
# A deterministic nearby sample also has exactly nine inside its refitted band.
nearby = sample + np.linspace(-0.01, 0.01, len(sample))
assert np.count_nonzero(np.abs(nearby - nearby.mean()) < nearby.std(ddof=1)) == 9
print("1.96 vs 2:", round(2*norm.cdf(1.96)-1, 4), round(norm.ppf(0.975), 4))
