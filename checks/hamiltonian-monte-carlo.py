"""Check script for the Hamiltonian Monte Carlo article's worked example.

Target: standard normal in one dimension, so U(q) = q^2 / 2 and
K(p) = p^2 / 2, with mass 1. Leapfrog with epsilon = 0.5, L = 4 steps,
starting from q0 = 0.5, p0 = 1.0. Every number printed in the article's
worked example is recomputed here with plain Python (math only) and
asserted. Run: python3 hamiltonian-monte-carlo.py  (exits 0 on success)
"""
import math

TOL = 5e-7  # article prints 6 decimal places


def close(a, b):
    return abs(a - b) < TOL


def H(q, p):
    return q * q / 2 + p * p / 2


q0, p0, eps, L = 0.5, 1.0, 0.5, 4

H0 = H(q0, p0)
assert H0 == 0.625, H0  # exact: (0.25 + 1) / 2

# Expected trajectory: (p_half, q, p, H) after each leapfrog step.
expected = [
    (0.875000, 0.937500, 0.640625, 0.644653),
    (0.406250, 1.140625, 0.121094, 0.657845),
    (-0.164062, 1.058594, -0.428711, 0.652207),
    (-0.693359, 0.711914, -0.871338, 0.633026),
]

q, p = q0, p0
for i in range(L):
    p_half = p - (eps / 2) * q          # half step for momentum; dU/dq = q
    q = q + eps * p_half                # full step for position
    p = p_half - (eps / 2) * q          # half step for momentum
    e_half, e_q, e_p, e_H = expected[i]
    assert close(p_half, e_half), (i + 1, p_half, e_half)
    assert close(q, e_q), (i + 1, q, e_q)
    assert close(p, e_p), (i + 1, p, e_p)
    assert close(H(q, p), e_H), (i + 1, H(q, p), e_H)

H_new = H(q, p)
dH = H_new - H0
assert close(dH, 0.008026), dH
accept = min(1.0, math.exp(H0 - H_new))
assert close(accept, 0.992006), accept

# Exact (non-leapfrog) trajectory at the same time t = L * eps = 2:
# q(t) = q0 cos t + p0 sin t,  p(t) = -q0 sin t + p0 cos t  (rotation).
t = L * eps
assert t == 2.0
q_exact = q0 * math.cos(t) + p0 * math.sin(t)
p_exact = -q0 * math.sin(t) + p0 * math.cos(t)
assert close(q_exact, 0.701224), q_exact
assert close(p_exact, -0.870796), p_exact
assert close(H(q_exact, p_exact), 0.625)  # exact dynamics conserves H

# Leapfrog endpoint errors against the exact trajectory.
assert close(q - q_exact, 0.010690), q - q_exact
assert close(p - p_exact, -0.000542), p - p_exact

# Misconception passage: at H = 0.625 the energetically allowed interval is
# |q| <= sqrt(2H) = sqrt(1.25), which carries about 0.7364 of the standard
# normal target: P(|Z| <= sqrt(1.25)) = erf(sqrt(1.25) / sqrt(2)).
allowed_mass = math.erf(math.sqrt(1.25) / math.sqrt(2))
assert round(allowed_mass, 4) == 0.7364, allowed_mass

# Reversibility check used in the article's Check yourself, question 1:
# negate p, run the same 4 steps, negate p again -> back to the start.
q2, p2 = q, -p
for _ in range(L):
    p_half = p2 - (eps / 2) * q2
    q2 = q2 + eps * p_half
    p2 = p_half - (eps / 2) * q2
p2 = -p2
assert close(q2, q0) and close(p2, p0), (q2, p2)

print("All worked-example numbers verified.")
print(f"H0 = {H0}, H_new = {H_new:.6f}, dH = {dH:+.6f}, accept = {accept:.6f}")
print(f"Leapfrog endpoint: q = {q:.6f}, p = {p:.6f}")
print(f"Exact endpoint:    q = {q_exact:.6f}, p = {p_exact:.6f}")
