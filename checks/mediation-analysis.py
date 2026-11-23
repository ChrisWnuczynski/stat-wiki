"""Recompute every number in mediation-analysis.md (worked example + Your turn).

Exact arithmetic uses fractions.Fraction. Exit 0 only if all assertions pass.
"""
from fractions import Fraction as F

failures = []

def check(name, got, want):
    ok = got == want
    print(f"{'PASS' if ok else 'FAIL'}: {name}: got {got}, expected {want}")
    if not ok:
        failures.append(name)

# ---- Worked example: linear system -------------------------------------
# M = 2 + 0.5 A + e_M ; Y = 1 + 0.3 A + 0.8 M + e_Y  (no interaction)
a = F(1, 2)          # 0.5
b = F(4, 5)          # 0.8
c_prime = F(3, 10)   # 0.3
m_intercept = F(2)
y_intercept = F(1)

indirect = a * b
check("worked indirect ab", indirect, F(2, 5))            # 0.4
total = c_prime + indirect
check("worked total c'+ab", total, F(7, 10))              # 0.7
prop = indirect / total
check("worked proportion mediated", prop, F(4, 7))        # ~0.571
print(f"      proportion mediated decimal = {float(prop):.4f} (~57.1%)")
check("worked CDE(m) = c' (no interaction)", c_prime, F(3, 10))

# Counterfactual means
EM0 = m_intercept                     # E[M^0] = 2
EM1 = m_intercept + a                 # E[M^1] = 5/2
check("E[M^0]", EM0, F(2))
check("E[M^1]", EM1, F(5, 2))

def nested_mean(a_exp, mean_m):
    return y_intercept + c_prime * a_exp + b * mean_m

EY00 = nested_mean(0, EM0)            # E[Y^{0,M^0}] = 13/5 = 2.6
EY10 = nested_mean(1, EM0)            # E[Y^{1,M^0}] = 29/10 = 2.9
EY11 = nested_mean(1, EM1)            # E[Y^{1,M^1}] = 33/10 = 3.3
check("E[Y^{0,M^0}]", EY00, F(13, 5))
check("E[Y^{1,M^0}]", EY10, F(29, 10))
check("E[Y^{1,M^1}]", EY11, F(33, 10))

NDE = EY10 - EY00
NIE = EY11 - EY10
check("worked NDE", NDE, F(3, 10))
check("worked NIE", NIE, F(2, 5))
check("NDE + NIE = total", NDE + NIE, F(7, 10))
check("NDE = c'", NDE, c_prime)
check("NIE = ab", NIE, indirect)
check("E[Y^1]-E[Y^0] = total", EY11 - EY00, total)

# ---- Inconsistent-mediation illustration (proportion mediated section) --
d_eff, i_eff = F(1, 2), F(-3, 10)     # direct 0.5, indirect -0.3
check("inconsistent total", d_eff + i_eff, F(1, 5))       # 0.2
check("inconsistent ratio", i_eff / (d_eff + i_eff), F(-3, 2))  # -1.5

# ---- Your turn ----------------------------------------------------------
a2, b2, cp2 = F(4, 5), F(1, 2), F(1, 10)   # 0.8, 0.5, 0.1
ind2 = a2 * b2
check("your-turn indirect", ind2, F(2, 5))                # 0.4
tot2 = cp2 + ind2
check("your-turn total", tot2, F(1, 2))                   # 0.5
check("your-turn proportion", ind2 / tot2, F(4, 5))       # 0.8 = 80%
# Nested means stated in the article: 1.0, 1.1, 1.5
y00, y10, y11 = F(1), F(11, 10), F(3, 2)
check("your-turn NDE", y10 - y00, cp2)                    # 0.1
check("your-turn NIE", y11 - y10, ind2)                   # 0.4
check("your-turn NDE+NIE = total", (y10 - y00) + (y11 - y10), tot2)

# ---- Check-yourself Q3 numbers ------------------------------------------
check("Q3 total", F(1, 2) + F(-3, 10), F(1, 5))
check("Q3 ratio", F(-3, 10) / F(1, 5), F(-3, 2))

print()
if failures:
    print(f"FAIL ({len(failures)} checks failed)")
    raise SystemExit(1)
print("PASS: all numbers in mediation-analysis.md verified")

# ---- Review-fix additions (2026-11-23) -------------------------------
# M = A counterexample: A randomised, M identical to A, so only (0,0) and
# (1,1) occur. Model 1, Y = M: Y^{a,m} = m.
nde1 = F(0) - F(0)          # E[Y^{1,M0}] - E[Y^{0,M0}] with M0 = 0
nie1 = F(1) - F(0)          # E[Y^{1,M1}] - E[Y^{1,M0}]
check("M=A model Y=M: (NDE, NIE)", (nde1, nie1), (F(0), F(1)))
# Model 2, Y = A: Y^{a,m} = a.
nde2 = F(1) - F(0)
nie2 = F(1) - F(1)
check("M=A model Y=A: (NDE, NIE)", (nde2, nie2), (F(1), F(0)))
# Both models give the same observed Y (= A = M) yet opposite decompositions.
print()
if failures:
    print(f"FAIL ({len(failures)} checks failed)")
    raise SystemExit(1)
print("PASS: review-fix M=A counterexample verified: (NDE, NIE) = (0,1) under Y=M and (1,0) under Y=A, same observed data.")
