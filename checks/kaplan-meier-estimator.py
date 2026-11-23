#!/usr/bin/env python3
"""Number check for the Kaplan-Meier estimator draft article.

Recomputes, from scratch with plain arithmetic (fractions for exactness,
math for the log-log intervals), every number quoted in
research/content/kaplan-meier-estimator.md: the worked example (8 patients) and the
"Your turn" exercise (6 patients). No repo code is imported.

Run:  python3 checks/kaplan-meier-estimator.py
Exit status is 0 only if every asserted value matches the draft.
"""

import math
from fractions import Fraction as F

Z = 1.96  # 97.5% standard normal quantile, for 95% intervals


def km_table(data):
    """Return one row per distinct event time.

    data: list of (time, event) with event 1 = event, 0 = censored.
    Each row is (t_j, n_j, d_j, S_hat, Greenwood_sum_or_None).
    The Greenwood term d / (n (n - d)) is undefined when n == d, so the
    running sum is None from that event time onward.
    """
    event_times = sorted({t for t, e in data if e == 1})
    rows = []
    s = F(1)
    g = F(0)
    g_defined = True
    for tj in event_times:
        n = sum(1 for t, _e in data if t >= tj)  # at risk just before tj
        d = sum(1 for t, e in data if t == tj and e == 1)
        s *= F(n - d, n)
        if g_defined:
            if n == d:
                g_defined = False
                g = None
            else:
                g += F(d, n * (n - d))
        rows.append((tj, n, d, s, g))
    return rows


def loglog_ci(s_float, g_float, z=Z):
    """95% log-log CI for S(t) given S_hat and Greenwood sum G."""
    theta = math.log(-math.log(s_float))
    se_theta = math.sqrt(g_float) / abs(math.log(s_float))
    lo = math.exp(-math.exp(theta + z * se_theta))
    hi = math.exp(-math.exp(theta - z * se_theta))
    return theta, se_theta, lo, hi


def median_time(rows):
    """Smallest event time with S_hat <= 1/2, or None if never reached."""
    for tj, _n, _d, s, _g in rows:
        if s <= F(1, 2):
            return tj
    return None


def rmst(rows, tau):
    """Area under the KM step function from 0 to tau (exact Fraction)."""
    area = F(0)
    prev_t = 0
    prev_s = F(1)
    for tj, _n, _d, s, _g in rows:
        if tj > tau:
            break
        area += prev_s * (tj - prev_t)
        prev_t, prev_s = tj, s
    area += prev_s * (tau - prev_t)
    return area


def approx(a, b, tol=1e-9):
    return abs(a - b) <= tol


# ---------------------------------------------------------------- worked example
# (time in months, 1 = event, 0 = censored)
worked = [(2, 1), (3, 1), (4, 0), (6, 1), (6, 1), (7, 0), (9, 1), (12, 0)]
assert sum(e for _t, e in worked) == 5, "worked example has exactly 5 events"
assert len({t for t, e in worked if e == 1}) == 4, (
    "worked example has exactly 4 distinct event times"
)
w = km_table(worked)
assert [(r[0], r[1], r[2]) for r in w] == [(2, 8, 1), (3, 7, 1), (6, 5, 2), (9, 2, 1)]
assert [r[3] for r in w] == [F(7, 8), F(3, 4), F(9, 20), F(9, 40)], "KM curve"
assert w[2][4] == F(7, 40), "Greenwood sum at 6 months"
assert w[3][4] == F(27, 40), "Greenwood sum at 9 months"
assert median_time(w) == 6, "median"
assert rmst(w, 9) == F(259, 40), "RMST(9) = 6.475"

s6 = float(F(9, 20))
g6 = float(F(7, 40))
var6 = s6 ** 2 * g6
se6 = s6 * math.sqrt(g6)
assert approx(var6, 0.0354375) and approx(var6, 567 / 16000)
assert approx(se6, 0.1882485, tol=1e-6)
theta6, se_th6, lo6, hi6 = loglog_ci(s6, g6)
assert approx(theta6, -0.2250107, tol=1e-6)
assert approx(se_th6, 0.5238898, tol=1e-6)
assert approx(lo6, 0.1075736, tol=1e-6) and approx(hi6, 0.7512779, tol=1e-6)
plain6 = (s6 - Z * se6, s6 + Z * se6)
assert approx(plain6[0], 0.0810329, tol=1e-6) and approx(plain6[1], 0.8189671, tol=1e-6)

# ---------------------------------------------------------------- "Your turn"
yours = [(1, 1), (2, 0), (4, 1), (4, 1), (5, 0), (8, 1)]
y = km_table(yours)
assert [(r[0], r[1], r[2]) for r in y] == [(1, 6, 1), (4, 4, 2), (8, 1, 1)]
assert [r[3] for r in y] == [F(5, 6), F(5, 12), F(0)], "KM curve"
assert y[1][4] == F(17, 60), "Greenwood sum at 4 months"
assert y[2][4] is None, "Greenwood undefined at 8 months (n == d == 1)"
assert median_time(y) == 4, "median"

s4 = float(F(5, 12))
g4 = float(F(17, 60))
var4 = s4 ** 2 * g4
se4 = s4 * math.sqrt(g4)
assert approx(var4, 85 / 1728) and approx(var4, 0.0491898, tol=1e-6)
assert approx(se4, 0.2217878, tol=1e-6)
theta4, se_th4, lo4, hi4 = loglog_ci(s4, g4)
assert approx(theta4, -0.1329958, tol=1e-6)
assert approx(se_th4, 0.6080065, tol=1e-6)
assert approx(lo4, 0.0559883, tol=1e-6) and approx(hi4, 0.7665267, tol=1e-6)
plain4 = (s4 - Z * se4, s4 + Z * se4)
assert plain4[0] < 0, "plain interval crosses below zero, as stated in the answer"

# ------------------------------------------------------- "Check yourself" Q1
# New dataset, not used elsewhere: (3, event), (5, censored), (6, event),
# (9, event).
check1 = [(3, 1), (5, 0), (6, 1), (9, 1)]
c = km_table(check1)
assert [(r[0], r[1], r[2]) for r in c] == [(3, 4, 1), (6, 2, 1), (9, 1, 1)]
assert [r[3] for r in c] == [F(3, 4), F(3, 8), F(0)], (
    "Check yourself Q1: S(3) = 3/4, S(6) = 3/8, S(9) = 0"
)

print("Worked example: S = 7/8, 3/4, 9/20, 9/40; G(6) = 7/40 = 0.175;")
print(f"  Var = {var6}, SE = {se6:.6f}")
print(f"  log-log 95% CI at 6 months = ({lo6:.3f}, {hi6:.3f})")
print(f"  plain 95% CI at 6 months   = ({plain6[0]:.3f}, {plain6[1]:.3f})")
print(f"  median = 6 months; RMST(9) = {float(rmst(w, 9))} months")
print("Your turn: S = 5/6, 5/12, 0; G(4) = 17/60;")
print(f"  Var = {var4:.6f}, SE = {se4:.6f}")
print(f"  log-log 95% CI at 4 months = ({lo4:.3f}, {hi4:.3f})")
print(f"  plain 95% CI at 4 months   = ({plain4[0]:.3f}, {plain4[1]:.3f})")
print(f"  median = 4 months; Greenwood undefined at 8 months (n = d = 1)")
print("Check yourself Q1: S(3) = 3/4, S(6) = 3/8 = 0.375, S(9) = 0")
print("All checks passed.")
