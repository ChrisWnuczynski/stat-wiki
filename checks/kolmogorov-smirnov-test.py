#!/usr/bin/env python3
"""Number checks for kolmogorov-smirnov-test.md (stdlib only).

Recomputes every number in the worked example and in the 'Your turn'
exercise: ECDF values, D+ / D- / D, the scaled statistic sqrt(n) D,
asymptotic p-values from the Kolmogorov limiting series, and the
critical-value comparisons quoted in the text (Massey 1951, Table 1).
Prints PASS and exits 0 when all checks agree.
"""
import math
import sys

FAILURES = []


def check(name, got, want, tol=1e-9):
    if abs(got - want) > tol:
        FAILURES.append(f"{name}: got {got!r}, want {want!r}")


def check_true(name, cond):
    if not cond:
        FAILURES.append(f"{name}: condition failed")


def kolmogorov_cdf(x):
    """Limiting CDF K(x) = 1 - 2 * sum_{k>=1} (-1)^(k-1) exp(-2 k^2 x^2)."""
    if x <= 0:
        return 0.0
    total = 0.0
    for k in range(1, 200):
        term = 2.0 * ((-1) ** (k - 1)) * math.exp(-2.0 * k * k * x * x)
        total += term
        if abs(term) < 1e-16:
            break
    return min(1.0, max(0.0, 1.0 - total))


def asym_p_one_sample(d, n):
    return 1.0 - kolmogorov_cdf(math.sqrt(n) * d)


# ---------------------------------------------------------------- worked example
# One sample, n = 5, tested against F0(x) = x on [0, 1] (Uniform(0, 1)).
sample = [0.05, 0.12, 0.18, 0.25, 0.90]
n = len(sample)
check("worked n", n, 5, tol=0)

# rows: (x_(i), F_n just after = i/n, F_n just before = (i-1)/n,
#        i/n - F0(x_(i)), F0(x_(i)) - (i-1)/n)
expected_rows = [
    (0.05, 0.2, 0.0, 0.15, 0.05),
    (0.12, 0.4, 0.2, 0.28, -0.08),
    (0.18, 0.6, 0.4, 0.42, -0.22),
    (0.25, 0.8, 0.6, 0.55, -0.35),
    (0.90, 1.0, 0.8, 0.10, 0.10),
]
d_plus_terms, d_minus_terms = [], []
for i, x in enumerate(sample, start=1):
    row = expected_rows[i - 1]
    check(f"worked x[{i}]", x, row[0])
    check(f"worked F_n after [{i}]", i / n, row[1])
    check(f"worked F_n before [{i}]", (i - 1) / n, row[2])
    # F0(x) = x for Uniform(0, 1)
    d_plus_terms.append(i / n - x)
    d_minus_terms.append(x - (i - 1) / n)
    check(f"worked D+ term [{i}]", d_plus_terms[-1], row[3])
    check(f"worked D- term [{i}]", d_minus_terms[-1], row[4])

d_plus = max(d_plus_terms)
d_minus = max(d_minus_terms)
d = max(d_plus, d_minus)
check("worked D+", d_plus, 0.55)
check("worked D-", d_minus, 0.10)
check("worked D", d, 0.55)
check("worked sqrt(n) D", math.sqrt(n) * d, 1.2298373876248845)
p_worked = asym_p_one_sample(d, n)
check("worked asymptotic p", p_worked, 0.0971, tol=5e-5)

# Massey (1951) Table 1 exact critical values for n = 5 (p. 70 of the paper):
# alpha = 0.10 -> 0.510 ; alpha = 0.05 -> 0.565 ; alpha = 0.20 -> 0.446.
check_true("worked D exceeds 10% exact critical value 0.510", d > 0.510)
check_true("worked D below 5% exact critical value 0.565", d < 0.565)
check_true("worked D exceeds 20% exact critical value 0.446", d > 0.446)
# Asymptotic 5% critical value 1.36/sqrt(n):
check("asymptotic 5% critical value, n=5", 1.36 / math.sqrt(5), 0.6082, tol=5e-5)
check_true("worked D below asymptotic 5% critical value", d < 1.36 / math.sqrt(5))

# ------------------------------------------------------------------- your turn
# Two samples of size 4 each.
xs = [1.2, 1.5, 2.1, 2.8]
ys = [1.8, 2.4, 3.0, 3.6]
nx, ny = len(xs), len(ys)
pooled = sorted(xs + ys)
expected_diffs = [0.25, 0.50, 0.25, 0.50, 0.25, 0.50, 0.25, 0.0]
diffs = []
for j, t in enumerate(pooled):
    fx = sum(1 for v in xs if v <= t) / nx
    fy = sum(1 for v in ys if v <= t) / ny
    diffs.append(fx - fy)
    check(f"your-turn diff [{j}] at {t}", fx - fy, expected_diffs[j])
d2 = max(abs(v) for v in diffs)
d2_plus = max(diffs)
d2_minus = max(-v for v in diffs)
check("your-turn two-sample D", d2, 0.50)
check("your-turn two-sample D+", d2_plus, 0.50)
check("your-turn two-sample D-", d2_minus, 0.0)
# Asymptotic 5% critical value: 1.36 * sqrt((nx + ny) / (nx * ny)).
crit2 = 1.36 * math.sqrt((nx + ny) / (nx * ny))
check("your-turn asymptotic 5% critical value", crit2, 0.9617, tol=5e-5)
check_true("your-turn D below asymptotic 5% critical value", d2 < crit2)
# Asymptotic p-value from the Kolmogorov series with effective size
# n_e = nx * ny / (nx + ny) = 2, lambda = sqrt(n_e) * D.
n_eff = nx * ny / (nx + ny)
check("your-turn effective n", n_eff, 2.0)
lam2 = math.sqrt(n_eff) * d2
check("your-turn lambda", lam2, 0.7071067811865476)
p2 = 1.0 - kolmogorov_cdf(lam2)
check("your-turn asymptotic p", p2, 0.6994, tol=5e-5)

# ---------------------------------------------------------------------- report
if FAILURES:
    print("FAIL")
    for f in FAILURES:
        print(" -", f)
    sys.exit(1)
print(f"worked example: D+ = {d_plus:.2f}, D- = {d_minus:.2f}, D = {d:.2f}, "
      f"sqrt(n) D = {math.sqrt(n) * d:.4f}, asymptotic p = {p_worked:.4f}")
print(f"your turn: D = {d2:.2f}, asymptotic 5% critical value = {crit2:.4f}, "
      f"asymptotic p = {p2:.4f}")
print("PASS")
