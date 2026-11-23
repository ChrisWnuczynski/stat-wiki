"""Recompute every number in causal-diagram.md (fork, collider, Your turn).

Plain Python, fractions only for the exact claims. Exit 0 only on PASS.
"""
from fractions import Fraction as F

failures = []

def check(label, got, want):
    ok = got == want
    print(f"{'ok  ' if ok else 'FAIL'} {label}: got {got}, want {want}")
    if not ok:
        failures.append(label)

# ---- Worked example (a): fork A <- X -> Y, A -> Y, no effect of A ----
# X=0: n=200, A1=50 (Y=10), A0=150 (Y=30); X=1: n=200, A1=150 (Y=120), A0=50 (Y=40)
x0 = {"n": 200, "a1": 50, "a1_y": 10, "a0": 150, "a0_y": 30}
x1 = {"n": 200, "a1": 150, "a1_y": 120, "a0": 50, "a0_y": 40}
check("X=0 total", x0["a1"] + x0["a0"], x0["n"])
check("X=1 total", x1["a1"] + x1["a0"], x1["n"])
r_x0_a1 = F(x0["a1_y"], x0["a1"]); r_x0_a0 = F(x0["a0_y"], x0["a0"])
r_x1_a1 = F(x1["a1_y"], x1["a1"]); r_x1_a0 = F(x1["a0_y"], x1["a0"])
check("X=0 risk A=1", r_x0_a1, F(1, 5))
check("X=0 risk A=0", r_x0_a0, F(1, 5))
check("X=1 risk A=1", r_x1_a1, F(4, 5))
check("X=1 risk A=0", r_x1_a0, F(4, 5))
check("X=0 risk difference", r_x0_a1 - r_x0_a0, F(0))
check("X=1 risk difference", r_x1_a1 - r_x1_a0, F(0))

a1_n = x0["a1"] + x1["a1"]; a1_y = x0["a1_y"] + x1["a1_y"]
a0_n = x0["a0"] + x1["a0"]; a0_y = x0["a0_y"] + x1["a0_y"]
check("crude A=1 n", a1_n, 200); check("crude A=1 events", a1_y, 130)
check("crude A=0 n", a0_n, 200); check("crude A=0 events", a0_y, 70)
crude1, crude0 = F(a1_y, a1_n), F(a0_y, a0_n)
check("crude risk A=1", crude1, F(13, 20))
check("crude risk A=0", crude0, F(7, 20))
check("crude risk difference", crude1 - crude0, F(3, 10))
std1 = F(1, 2) * r_x0_a1 + F(1, 2) * r_x1_a1
std0 = F(1, 2) * r_x0_a0 + F(1, 2) * r_x1_a0
check("standardised risk A=1", std1, F(1, 2))
check("standardised risk A=0", std0, F(1, 2))
check("standardised risk difference", std1 - std0, F(0))
check("X=1 share of exposed", F(x1["a1"], a1_n), F(3, 4))
check("X=0 share of unexposed", F(x0["a0"], a0_n), F(3, 4))

# ---- Worked example (b): collider, A,B independent, C = A OR B ----
cells = {(0, 0): 100, (1, 0): 100, (0, 1): 100, (1, 1): 100}
check("collider population", sum(cells.values()), 400)
def risk_b_given_a(a, restrict_c1=False):
    num = den = 0
    for (av, bv), n in cells.items():
        if restrict_c1 and not (av or bv):
            continue
        if av == a:
            den += n
            if bv == 1:
                num += n
    return F(num, den), num, den
r, n_, d_ = risk_b_given_a(1); check("marginal P(B=1|A=1)", r, F(1, 2))
r, n_, d_ = risk_b_given_a(0); check("marginal P(B=1|A=0)", r, F(1, 2))
# marginal odds ratio = 1
or_marg = F(cells[(1, 1)] * cells[(0, 0)], cells[(1, 0)] * cells[(0, 1)])
check("marginal odds ratio", or_marg, F(1))
c1 = {k: v for k, v in cells.items() if k != (0, 0)}
check("C=1 total", sum(c1.values()), 300)
check("C=1 table A=1,B=1", c1[(1, 1)], 100)
check("C=1 table A=1,B=0", c1[(1, 0)], 100)
check("C=1 table A=0,B=1", c1[(0, 1)], 100)
check("C=1 table A=0,B=0", c1.get((0, 0), 0), 0)
r1, n1, d1 = risk_b_given_a(1, restrict_c1=True)
r0, n0, d0 = risk_b_given_a(0, restrict_c1=True)
check("within C=1 P(B=1|A=1)", r1, F(1, 2))
check("within C=1 P(B=1|A=0)", r0, F(1))
check("within C=1 risk difference", r1 - r0, F(-1, 2))
or_c1 = F(c1[(1, 1)] * c1.get((0, 0), 0), c1[(1, 0)] * c1[(0, 1)])
check("within C=1 odds ratio", or_c1, F(0))

# ---- Your turn: fork with effect 1/4 ----
y0 = {"a1": 40, "a1_y": 20, "a0": 160, "a0_y": 40}
y1 = {"a1": 160, "a1_y": 120, "a0": 40, "a0_y": 20}
check("Your turn X=0 total", y0["a1"] + y0["a0"], 200)
check("Your turn X=1 total", y1["a1"] + y1["a0"], 200)
s0a1, s0a0 = F(y0["a1_y"], y0["a1"]), F(y0["a0_y"], y0["a0"])
s1a1, s1a0 = F(y1["a1_y"], y1["a1"]), F(y1["a0_y"], y1["a0"])
check("Your turn X=0 risk A=1", s0a1, F(1, 2))
check("Your turn X=0 risk A=0", s0a0, F(1, 4))
check("Your turn X=0 RD", s0a1 - s0a0, F(1, 4))
check("Your turn X=1 risk A=1", s1a1, F(3, 4))
check("Your turn X=1 risk A=0", s1a0, F(1, 2))
check("Your turn X=1 RD", s1a1 - s1a0, F(1, 4))
ta1_n, ta1_y = y0["a1"] + y1["a1"], y0["a1_y"] + y1["a1_y"]
ta0_n, ta0_y = y0["a0"] + y1["a0"], y0["a0_y"] + y1["a0_y"]
check("Your turn crude A=1", F(ta1_y, ta1_n), F(7, 10))
check("Your turn crude A=0", F(ta0_y, ta0_n), F(3, 10))
check("Your turn crude RD", F(ta1_y, ta1_n) - F(ta0_y, ta0_n), F(2, 5))
tstd1 = F(1, 2) * s0a1 + F(1, 2) * s1a1
tstd0 = F(1, 2) * s0a0 + F(1, 2) * s1a0
check("Your turn standardised A=1", tstd1, F(5, 8))
check("Your turn standardised A=0", tstd0, F(3, 8))
check("Your turn standardised RD", tstd1 - tstd0, F(1, 4))
check("Your turn crude overstatement", F(2, 5) - F(1, 4), F(3, 20))

print()
if failures:
    print(f"FAIL: {len(failures)} check(s) failed: {failures}")
    raise SystemExit(1)
print("PASS: all numbers in causal-diagram.md verified")

# ---------- Review-fix additions (2026-11-23) ----------
# Collider example: marginal conditional proportions are 100/200, not 200/400.
assert F(100, 200) == F(1, 2)
# Within C=1: risks 100/200 (A=1) and 100/100 (A=0); RD=-1/2, RR=1/2, OR=0.
r_a1, r_a0 = F(100, 200), F(100, 100)
assert r_a1 - r_a0 == F(-1, 2)
assert r_a1 / r_a0 == F(1, 2)
assert F(100 * 0, 100 * 100) == 0
print("Review-fix: collider marginal proportions 100/200; within C=1 RD=-1/2, RR=1/2, OR=0 (maximal only on the odds-ratio scale).")
print("PASS: review-fix numbers verified.")
