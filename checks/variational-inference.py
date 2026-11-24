"""Number checks for variational-inference.md (plain Python, math/fractions only).

Example 1: mean-field for bivariate normal, rho = 0.8, unit marginal variances.
Example 2: normal-normal model where the variational family contains the posterior.
"""
import math
from fractions import Fraction as F

# ---------- Example 1 ----------
rho = F(4, 5)                      # 0.8 exactly
one_minus_rho2 = 1 - rho * rho     # 1 - rho^2
assert one_minus_rho2 == F(9, 25)  # 0.36
mf_var = one_minus_rho2            # optimal mean-field variance = 1 / (Sigma^{-1})_{ii}
mf_sd = math.sqrt(float(mf_var))
assert abs(mf_sd - 0.6) < 1e-15

# KL(q||p) for q = N(0, diag(v,v)), p = N(0, Sigma), Sigma = [[1,rho],[rho,1]]:
# KL = 0.5 * [ tr(Sigma^{-1} D) - 2 + log(det Sigma / det D) ],  D = diag(v, v)
# (Sigma^{-1})_{ii} = 1/(1-rho^2), so tr(Sigma^{-1} D) = 2v/(1-rho^2) = 2 at v = 1-rho^2.
v = float(mf_var)
tr = 2 * v / float(one_minus_rho2)
assert abs(tr - 2.0) < 1e-15
det_sigma = float(one_minus_rho2)          # det Sigma = 1 - rho^2 = 0.36
det_d = v * v                              # 0.1296
assert abs(det_sigma - 0.36) < 1e-15 and abs(det_d - 0.1296) < 1e-12
kl = 0.5 * (tr - 2 + math.log(det_sigma / det_d))
kl_closed = -0.5 * math.log(float(one_minus_rho2))   # -0.5 * log(1 - rho^2)
assert abs(kl - kl_closed) < 1e-12
print(f"Ex1: 1-rho^2 = {float(one_minus_rho2)}, mf var = {v}, mf sd = {mf_sd}")
print(f"Ex1: KL(q*||p) = {kl:.6f} nats  (= -0.5*log(0.36) = {kl_closed:.6f})")
assert abs(kl - 0.510826) < 1e-6

# Variance shortfall: mean-field variance is 36% of the true marginal variance.
assert abs(v / 1.0 - 0.36) < 1e-15
# Conditional variance of Z1 given Z2 under p is also 1 - rho^2 (sanity: distinct quantity, same number here)
# CAVI-style check: q1 variance from precision diagonal
prec_ii = 1.0 / float(one_minus_rho2)
assert abs(1.0 / prec_ii - v) < 1e-15

# ---------- Example 2 ----------
# Prior theta ~ N(0, tau^2), tau^2 = 4.  Data x_i | theta ~ N(theta, sigma^2), sigma^2 = 1, n = 5.
tau2, sig2, n = F(4), F(1), 5
data = [F(11, 10), F(8, 5), F(21, 10), F(13, 5), F(31, 10)]   # 1.1, 1.6, 2.1, 2.6, 3.1
S = sum(data)
assert S == F(21, 2)                       # sum = 10.5
ybar = S / n
assert ybar == F(21, 10)                   # 2.1
ss_dev = sum((x - ybar) ** 2 for x in data)
assert ss_dev == F(5, 2)                   # sum of squared deviations = 2.5
ss_tot = sum(x * x for x in data)
assert ss_tot == F(491, 20)                # 24.55

post_prec = 1 / tau2 + n / sig2            # 1/4 + 5 = 21/4
post_var = 1 / post_prec
assert post_var == F(4, 21)                # 0.190476...
post_mean = post_var * (S / sig2)          # prior mean 0
assert post_mean == F(2)                   # exactly 2
print(f"Ex2: posterior mean = {float(post_mean)}, posterior var = {float(post_var):.6f} "
      f"(4/21), posterior sd = {math.sqrt(float(post_var)):.6f}")
assert abs(math.sqrt(float(post_var)) - 0.436436) < 1e-6

# Log marginal likelihood log p(x): x ~ N(0, C), C = sig2 I + tau2 J.
# det C = sig2^(n-1) * (sig2 + n tau2) = 21 ;  x'C^{-1}x = ss_tot/sig2 - tau2*S^2/(sig2*(sig2+n tau2))
det_c = float(sig2 ** (n - 1) * (sig2 + n * tau2))
assert det_c == 21.0
quad = float(ss_tot / sig2) - float(tau2 * S * S / (sig2 * (sig2 + n * tau2)))
assert abs(quad - 3.55) < 1e-12            # 24.55 - 21.00
log_marg = -0.5 * n * math.log(2 * math.pi) - 0.5 * math.log(det_c) - 0.5 * quad
print(f"Ex2: log p(x) = {log_marg:.6f}")
assert abs(log_marg - (-7.891954)) < 1e-6

# ELBO at q = posterior, computed from its definition:
# ELBO = E_q[log p(x|theta)] + E_q[log p(theta)] - E_q[log q(theta)]
m, w = float(post_mean), float(post_var)
# E_q[log p(x|theta)] = -n/2 log(2 pi sig2) - (ss_dev + n (ybar - m)^2 + n w) / (2 sig2)
e_loglik = -0.5 * n * math.log(2 * math.pi * float(sig2)) \
    - (float(ss_dev) + n * (float(ybar) - m) ** 2 + n * w) / (2 * float(sig2))
# E_q[log p(theta)] = -0.5 log(2 pi tau2) - (m^2 + w) / (2 tau2)
e_logprior = -0.5 * math.log(2 * math.pi * float(tau2)) - (m * m + w) / (2 * float(tau2))
# -E_q[log q(theta)] = entropy of N(m, w) = 0.5 log(2 pi e w)
entropy = 0.5 * math.log(2 * math.pi * math.e * w)
elbo = e_loglik + e_logprior + entropy
print(f"Ex2: E loglik = {e_loglik:.6f}, E log prior = {e_logprior:.6f}, entropy = {entropy:.6f}")
print(f"Ex2: ELBO(q = posterior) = {elbo:.6f};  log p(x) - ELBO = {log_marg - elbo:.2e} (KL = 0)")
assert abs(elbo - log_marg) < 1e-9

# A suboptimal q for contrast: q = N(2, 1) (right mean, prior-scale variance).
w2 = 1.0
e_loglik2 = -0.5 * n * math.log(2 * math.pi) - (float(ss_dev) + n * (float(ybar) - m) ** 2 + n * w2) / 2
e_logprior2 = -0.5 * math.log(2 * math.pi * 4.0) - (m * m + w2) / 8.0
entropy2 = 0.5 * math.log(2 * math.pi * math.e * w2)
elbo2 = e_loglik2 + e_logprior2 + entropy2
kl2 = log_marg - elbo2
# KL(N(2,1) || N(2,4/21)) = 0.5*[ w2/post_var - 1 + log(post_var/w2) ] (equal means)
kl2_direct = 0.5 * (w2 / float(post_var) - 1 + math.log(float(post_var) / w2))
assert abs(kl2 - kl2_direct) < 1e-9
print(f"Ex2: ELBO(q = N(2,1)) = {elbo2:.6f};  KL = {kl2:.6f}")
assert abs(elbo2 - (-9.187840)) < 1e-6 and abs(kl2 - 1.295886) < 1e-6

print("All variational-inference checks passed.")
