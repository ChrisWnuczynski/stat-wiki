"""Recompute every worked number in dirichlet-process.md.

Plain Python only: math and fractions. Run: python3 dirichlet-process.py
Exits 0 only if every assertion holds.
"""
from fractions import Fraction
import math

# ---------------------------------------------------------------------------
# Worked example 1: stick-breaking with V = (1/2, 1/3, 1/4, 1/5, 1/6)
# pi_k = V_k * prod_{j<k} (1 - V_j);  remaining mass R_5 = prod_{j<=5} (1-V_j)
# ---------------------------------------------------------------------------
V = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4), Fraction(1, 5), Fraction(1, 6)]
pi = []
remaining = Fraction(1)
for v in V:
    pi.append(v * remaining)
    remaining *= (1 - v)

expected_pi = [Fraction(1, 2), Fraction(1, 6), Fraction(1, 12),
               Fraction(1, 20), Fraction(1, 30)]
assert pi == expected_pi, pi
# each pi_k also equals 1 / (k * (k+1)) for k = 1..5 in this example
for k, p in enumerate(pi, start=1):
    assert p == Fraction(1, k * (k + 1)), (k, p)
assert remaining == Fraction(1, 6), remaining          # mass left after 5 breaks
assert sum(pi) == Fraction(5, 6)                        # mass assigned by 5 breaks
assert sum(pi) + remaining == 1
# decimal forms quoted in the article
assert abs(float(pi[0]) - 0.5) < 1e-12
assert abs(float(pi[1]) - 0.166667) < 1e-6
assert abs(float(pi[2]) - 0.083333) < 1e-6
assert abs(float(pi[3]) - 0.05) < 1e-12
assert abs(float(pi[4]) - 0.033333) < 1e-6
assert abs(float(remaining) - 0.166667) < 1e-6

# Expected stick-breaking weights under the prior, E[pi_k] for alpha = 2:
# E[V] = 1/(1+alpha), E[1-V] = alpha/(1+alpha), so E[pi_k] = (1/3)(2/3)^(k-1)
alpha_sb = Fraction(2)
for k in range(1, 6):
    e_pi = Fraction(1, 1 + alpha_sb) * Fraction(alpha_sb, 1 + alpha_sb) ** (k - 1)
    assert e_pi == Fraction(1, 3) * Fraction(2, 3) ** (k - 1)
assert Fraction(1, 3) * Fraction(2, 3) ** 0 == Fraction(1, 3)   # E[pi_1], alpha=2
assert Fraction(1, 3) * Fraction(2, 3) ** 1 == Fraction(2, 9)   # E[pi_2], alpha=2

# ---------------------------------------------------------------------------
# Worked example 2a: Chinese restaurant / Polya urn predictive probabilities.
# alpha = 2; first 5 customers occupy tables of sizes 3 and 2.
# Customer 6: P(join table with n_j customers) = n_j / (alpha + 5),
#             P(new table)                     = alpha / (alpha + 5).
# ---------------------------------------------------------------------------
alpha_crp = Fraction(2)
n_so_far = 5
denom = alpha_crp + n_so_far
assert denom == 7
p_table_big = Fraction(3) / denom
p_table_small = Fraction(2) / denom
p_new = alpha_crp / denom
assert p_table_big == Fraction(3, 7)
assert p_table_small == Fraction(2, 7)
assert p_new == Fraction(2, 7)
assert p_table_big + p_table_small + p_new == 1
assert abs(float(p_table_big) - 0.428571) < 1e-6
assert abs(float(p_table_small) - 0.285714) < 1e-6

# Probability the second draw repeats the first (Antoniak): 1 / (alpha + 1)
assert Fraction(1) / (alpha_crp + 1) == Fraction(1, 3)   # for alpha = 2
assert Fraction(1) / (Fraction(1) + 1) == Fraction(1, 2)  # for alpha = 1

# ---------------------------------------------------------------------------
# Worked example 2b: expected number of distinct values, Antoniak's formula
# E[K_n] = sum_{i=1}^n alpha / (alpha + i - 1).
# Case alpha = 1, n = 10: E[K_10] = H_10 = sum_{i=1}^{10} 1/i.
# ---------------------------------------------------------------------------
H10 = sum(Fraction(1, i) for i in range(1, 11))
assert H10 == Fraction(7381, 2520), H10
assert abs(float(H10) - 2.928968) < 1e-6
assert abs(float(H10) - sum(1.0 / i for i in range(1, 11))) < 1e-12
assert abs(float(H10) - 2.9289682539682538) < 1e-12

# Case alpha = 2, n = 5: E[K_5] = 2/2 + 2/3 + 2/4 + 2/5 + 2/6 = 29/10
EK5_a2 = sum(Fraction(2, 2 + i - 1) for i in range(1, 6))
assert EK5_a2 == Fraction(29, 10), EK5_a2
assert abs(float(EK5_a2) - 2.9) < 1e-12

# Antoniak/Escobar-West logarithmic approximation alpha * log((alpha + n)/alpha)
approx_a1_n10 = 1.0 * math.log((1 + 10) / 1)
assert abs(approx_a1_n10 - 2.397895) < 1e-6   # log(11); cruder than exact H_10
assert approx_a1_n10 < float(H10)

# ---------------------------------------------------------------------------
# Prior mean and variance of G(A): G(A) ~ Beta(alpha*G0(A), alpha*(1-G0(A)))
# E[G(A)] = G0(A);  Var(G(A)) = G0(A)(1-G0(A)) / (alpha + 1).
# Article example: G0(A) = 1/2, alpha = 3  ->  Var = 1/16.
# ---------------------------------------------------------------------------
g0A = Fraction(1, 2)
alpha_prior = Fraction(3)
var_prior = g0A * (1 - g0A) / (alpha_prior + 1)
assert var_prior == Fraction(1, 16), var_prior
assert abs(float(var_prior) - 0.0625) < 1e-12
# alpha = 1 with the same G0(A): Var = 1/8; alpha = 9: Var = 1/40
assert g0A * (1 - g0A) / (1 + 1) == Fraction(1, 8)
assert g0A * (1 - g0A) / (9 + 1) == Fraction(1, 40)

# ---------------------------------------------------------------------------
# Worked example 3: posterior Dirichlet process.
# Prior DP(alpha=3, G0) with G0 = Uniform(0,1). Data (n=4): 0.2, 0.2, 0.7, 0.2.
# A = [0, 0.5], so G0(A) = 1/2 and A contains three observations (the 0.2s).
# Posterior: DP(alpha + n, (alpha*G0 + sum_i delta_{x_i}) / (alpha + n)).
# ---------------------------------------------------------------------------
alpha3 = Fraction(3)
n3 = 4
counts_in_A = 3                      # the three 0.2 values; 0.7 is outside A
post_alpha = alpha3 + n3
assert post_alpha == 7
post_mean_A = (alpha3 * g0A + counts_in_A) / post_alpha
assert post_mean_A == Fraction(9, 14), post_mean_A
assert abs(float(post_mean_A) - 0.642857) < 1e-6
# posterior base measure: weights on the atoms and on G0
w_atom_02 = Fraction(3, 7)           # three ties at 0.2
w_atom_07 = Fraction(1, 7)           # one observation at 0.7
w_base = Fraction(3, 7)              # alpha / (alpha + n) spread according to G0
assert w_atom_02 + w_atom_07 + w_base == 1
# predictive probabilities for a fifth draw, from the posterior mean measure
assert w_atom_02 == Fraction(3, 7)                       # P(X_5 = 0.2 | data)
assert w_atom_07 == Fraction(1, 7)                       # P(X_5 = 0.7 | data)
p_new_in_A = w_base * g0A                                # new value, falling in A
assert p_new_in_A == Fraction(3, 14)
assert w_atom_02 + p_new_in_A == post_mean_A             # P(X_5 in A | data) = 9/14
# posterior variance of G(A): G(A) | data ~ Beta(9/2, 5/2) marginally, so
# Var = p(1-p) / (alpha + n + 1) with p = 9/14
post_var_A = post_mean_A * (1 - post_mean_A) / (post_alpha + 1)
assert post_var_A == Fraction(45, 1568), post_var_A
assert abs(float(post_var_A) - 0.028699) < 1e-6
# prior predictive check (no data): P(X_1 in A) = G0(A) = 1/2
assert (alpha3 * g0A) / alpha3 == g0A

# ---------------------------------------------------------------------------
# Check-yourself answers
# Q1: V_1 = 1/4, V_2 = 1/2 -> pi_1 = 1/4, pi_2 = 3/8, remaining = 3/8.
# ---------------------------------------------------------------------------
q_pi1 = Fraction(1, 4)
q_pi2 = Fraction(1, 2) * (1 - Fraction(1, 4))
q_rem = (1 - Fraction(1, 4)) * (1 - Fraction(1, 2))
assert q_pi1 == Fraction(1, 4) and q_pi2 == Fraction(3, 8) and q_rem == Fraction(3, 8)
assert q_pi1 + q_pi2 + q_rem == 1

# Q2: alpha = 1; after 4 customers tables hold 3 and 1. Customer 5:
# P = 3/5, 1/5, 1/5 (denominator alpha + 4 = 5).
assert Fraction(3, 5) + Fraction(1, 5) + Fraction(1, 5) == 1
assert Fraction(1, 1 + 4) == Fraction(1, 5)   # new-table probability alpha/(alpha+4)

# Q3: alpha = 1, n = 2, both observations in A, G0(A) = 1/4.
# Posterior mean of G(A) = (1 * 1/4 + 2) / (1 + 2) = 3/4.
q3 = (Fraction(1) * Fraction(1, 4) + 2) / (1 + 2)
assert q3 == Fraction(3, 4), q3

print("dirichlet-process.py: all assertions passed")
print(f"  stick-breaking pi = {[str(p) for p in pi]}, remaining = {remaining}")
print(f"  CRP customer 6: {p_table_big}, {p_table_small}, new = {p_new}")
print(f"  E[K_10] (alpha=1) = H_10 = {H10} = {float(H10):.6f}")
print(f"  E[K_5] (alpha=2) = {EK5_a2} = {float(EK5_a2)}")
print(f"  posterior mean of G(A) = {post_mean_A} = {float(post_mean_A):.6f}")
print(f"  posterior var of G(A) = {post_var_A} = {float(post_var_A):.6f}")
