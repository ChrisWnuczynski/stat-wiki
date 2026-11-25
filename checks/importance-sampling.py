"""Check script for the importance-sampling article (stat-wiki Batch B1).

Recomputes EVERY number stated in ~/workspace/stat-wiki-b1/drafts/importance-sampling.md
using only math and fractions, and asserts each one. Run: python3 importance-sampling.py
Exits 0 only if all assertions pass.
"""
import math
from fractions import Fraction as F

TOL = 5e-7  # numbers in the article are stated to at most 6 significant figures


def close(a, b, tol=TOL):
    assert abs(a - b) <= tol, (a, b)


def Phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


# ---------------------------------------------------------------------------
# Worked example 1: P(Z > 3), Z ~ N(0,1), proposal q = N(3,1)
# ---------------------------------------------------------------------------
mu = 1.0 - Phi(3.0)
close(mu, 0.001349898, 1e-9)          # article: 0.001349898 (and 0.0013499)
close(mu, 0.0013499, 5e-8)

# weight function w(x) = exp(9/2 - 3x); values stated in the article
close(math.exp(4.5 - 3 * 3), 0.011109, 1e-6)   # w(3) = exp(-9/2)
close(math.exp(-4.5), 0.011109, 1e-6)
close(math.exp(4.5 - 3 * 4), 0.000553, 1e-6)   # w(4)

# Exact per-draw second moment: E_q[w(X)^2 1(X>3)] = e^9 * (1 - Phi(6))
second = math.exp(9.0) * (1.0 - Phi(6.0))
close(second, 7.994402e-6, 1e-9)      # article: 7.994402 x 10^-6 (exact 7.99440249e-6)
close(1.0 - Phi(6.0), 9.865876e-10, 1e-15)

# Per-draw variance of the importance-sampling contribution
var_is = second - mu ** 2
close(var_is, 6.172178e-6, 1e-9)      # article: 6.1722 x 10^-6

# Crude Monte Carlo per-draw variance p(1-p)
var_crude = mu * (1.0 - mu)
close(var_crude, 1.348076e-3, 1e-9)   # article: 1.3481 x 10^-3
close(var_crude / var_is, 218.4, 0.05)  # article: about 218 times smaller

# Draws needed for a 10% relative standard error: N = (var/mu^2) / 0.1^2
n_crude = (var_crude / mu ** 2) / 0.01
n_is = (var_is / mu ** 2) / 0.01
assert math.ceil(n_crude) == 73980, n_crude   # article: 73,980
assert math.ceil(n_is) == 339, n_is           # article: 339

# Chi-squared divergence ingredient: E_q[w(X)^2] = e^9 for this pair (p, q),
# so D = e^9 - 1 (article: e^9 = 8103.08, D = 8102.08)
close(math.exp(9.0), 8103.08, 0.005)
close(math.exp(9.0) - 1.0, 8102.08, 0.005)

# ---------------------------------------------------------------------------
# Worked example 2 (self-normalised): posterior Beta(4,2) for a coin,
# unnormalised target t(theta) = theta^3 (1 - theta) on (0,1),
# proposal q = Uniform(0,1) (density 1), draws 0.2, 0.4, 0.5, 0.6, 0.8
# ---------------------------------------------------------------------------
ths = [F(1, 5), F(2, 5), F(1, 2), F(3, 5), F(4, 5)]
ws = [t ** 3 * (1 - t) for t in ths]
assert ws == [F(4, 625), F(24, 625), F(1, 16), F(54, 625), F(64, 625)]
assert [float(w) for w in ws] == [0.0064, 0.0384, 0.0625, 0.0864, 0.1024]

S = sum(ws)
assert S == F(2961, 10000) and float(S) == 0.2961

norm = [w / S for w in ws]
assert norm == [F(64, 2961), F(128, 987), F(625, 2961), F(96, 329), F(1024, 2961)]
for got, stated in zip(norm, [0.021614, 0.129686, 0.211077, 0.291793, 0.345829]):
    close(float(got), stated, 1e-6)
assert sum(norm) == 1

num = sum(w * t for w, t in zip(ws, ths))
assert num == F(3633, 20000) and float(num) == 0.18165
est = num / S
assert est == F(173, 282)
close(float(est), 0.613475, 1e-6)     # article: 0.6135 (0.613475)
close(float(F(4, 6)), 0.666667, 1e-6)  # true posterior mean Beta(4,2) = 2/3

# Normalising-constant (marginal-likelihood style) estimate: mean unnormalised weight
z_est = S / 5
assert z_est == F(2961, 50000) and float(z_est) == 0.05922
z_true = F(math.factorial(3) * math.factorial(1), math.factorial(5))  # B(4,2)
assert z_true == F(1, 20) and float(z_true) == 0.05

# Effective sample size (sum w)^2 / sum w^2
sumsq = sum(w * w for w in ws)
assert sumsq == F(2337249, 100000000) and float(sumsq) == 0.02337249
assert S * S == F(8767521, 100000000)  # 0.2961^2 = 0.08767521
close(float(S * S), 0.08767521, 1e-9)
ess = S * S / sumsq
assert ess == F(2922507, 779083)
close(float(ess), 3.7512, 1e-4)       # article: ESS = 3.7512 (about 3.75 of 5)

# ---------------------------------------------------------------------------
# Check yourself, question 2: weights 1, 1, 2, 6 and h-values 0, 1, 2, 3
# ---------------------------------------------------------------------------
wq = [F(1), F(1), F(2), F(6)]
hq = [F(0), F(1), F(2), F(3)]
assert sum(wq) == 10 and sum(w * w for w in wq) == 42
ess_q = sum(wq) ** 2 / sum(w * w for w in wq)
assert ess_q == F(50, 21)
close(float(ess_q), 2.381, 1e-3)      # article answer: 50/21, about 2.381
sn_q = sum(w * h for w, h in zip(wq, hq)) / sum(wq)
assert sn_q == F(23, 10) and float(sn_q) == 2.3
assert max(wq) / sum(wq) == F(3, 5)   # largest normalised weight 0.6

# Check yourself, question 1 (support failure), exact discrete arithmetic:
# p(1) = p(2) = 1/2, h(x) = x, true mean 3/2; q(1) = 1, q(2) = 0.
# Every draw is 1, w(1) = 1/2, so the estimator is identically 1/2.
assert F(1, 2) * 1 + F(1, 2) * 2 == F(3, 2)
assert F(1, 2) / F(1, 1) == F(1, 2)   # the constant value the estimator takes

# Check yourself, question 3 (infinite variance threshold):
# p = N(0,1), q = N(0, s^2): E_q[w^2] finite iff s^2 > 1/2.
# Exponent coefficient of p^2/q is -1 + 1/(2 s^2); check the boundary cases
# stated in the answer: s = 0.6 gives variance infinite, s = 0.8 finite.
for s, finite in [(0.6, False), (0.8, True)]:
    coeff = -1.0 + 1.0 / (2.0 * s * s)
    assert (coeff < 0) == finite, (s, coeff)

print("importance-sampling: all checks passed")
