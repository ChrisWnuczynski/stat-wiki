"""Number check for the Anderson-Darling test article (Batch N1).

Plain Python standard library only. Recomputes, term by term:
  * the worked example (n = 8 against a fully specified Uniform(0, 1)),
  * the "Your turn" sample (n = 8 against the same distribution),
  * Stephens' normal-case adjustment arithmetic quoted in the article
    (A^2 = 0.947, n = 11 -> A^{2*} = 1.029), and
  * every critical-value comparison made in the article.
Prints PASS and exits 0 when all recomputed values match the article.
"""
import math
import sys

FAILURES = []


def check(label, got, want, tol=5e-4):
    ok = abs(got - want) <= tol
    print(f"{'ok  ' if ok else 'FAIL'} {label}: got {got:.4f}, article {want:.4f}")
    if not ok:
        FAILURES.append(label)


def ad_terms(u):
    """Term (2i-1)[ln F(x_i) + ln(1 - F(x_{n+1-i}))] for each i; F(x)=x here."""
    n = len(u)
    return [
        (2 * i - 1) * (math.log(u[i - 1]) + math.log(1.0 - u[n - i]))
        for i in range(1, n + 1)
    ]


def ad_statistic(u):
    terms = ad_terms(u)
    return -len(u) - sum(terms) / len(u), terms


# --- Worked example: n = 8 against fully specified Uniform(0, 1) -------------
worked = [0.03, 0.09, 0.16, 0.23, 0.30, 0.37, 0.43, 0.49]
a2, terms = ad_statistic(worked)
article_terms = [-4.1799, -8.9102, -11.4731, -12.7845,
                 -13.1880, -12.8547, -12.1976, -11.1571]
for i, (got, want) in enumerate(zip(terms, article_terms), start=1):
    check(f"worked term i={i}", got, want)
check("worked sum of terms", sum(terms), -86.7451)
check("worked A^2", a2, 2.8431)
# Case 0 (fully specified) asymptotic percentage points (Anderson & Darling 1954, p. 766):
# 15% 1.610, 10% 1.933, 5% 2.492, 2.5% 3.070, 1% 3.857.
assert 2.492 < a2 < 3.857, "worked example must reject at 5% but not at 1%"
print("ok   worked example: 2.492 < A^2 < 3.857 (reject at 5%, not at 1%)")

# --- Your turn: n = 8 against fully specified Uniform(0, 1) -------------------
your = [0.10, 0.19, 0.28, 0.37, 0.45, 0.54, 0.63, 0.72]
a2y, terms_y = ad_statistic(your)
article_terms_y = [-3.5756, -7.9650, -10.2475, -11.1446,
                   -11.3449, -10.3916, -8.7458, -6.5080]
for i, (got, want) in enumerate(zip(terms_y, article_terms_y), start=1):
    check(f"your-turn term i={i}", got, want)
check("your-turn sum of terms", sum(terms_y), -69.9229)
check("your-turn A^2", a2y, 0.7404)
assert a2y < 1.610, "your-turn sample must not reject even at the 15% level"
print("ok   your turn: A^2 < 1.610 (no rejection even at 15%)")

# --- Stephens' normal-case adjustment, as quoted in the article ---------------
# Stephens (1974), Case 3 (normal, both parameters estimated): sample variance
# with divisor n - 1 (pp. 730-731), adjustment factor 1 + 4/n - 25/n^2, and the
# Table 1.3 (p. 732) points 0.576 / 0.656 / 0.787 / 0.918 / 1.092.
# His sec. 3.3 Illustration 2 (n = 11 weights): recomputing the computing
# formula from the listed weights (mean 172, sample SD 24.95195) gives raw
# A^2 = 0.946772, which Stephens prints rounded as 0.947; the adjusted value
# is 0.946772 * 1.157025 = 1.09544, printed by Stephens as 1.095.
raw_stephens = 0.946772
check("Stephens raw A^2 rounds to his printed 0.947", round(raw_stephens, 3), 0.947, tol=0)
factor = 1.0 + 4.0 / 11 - 25.0 / 121
check("normal-case adjustment factor (n=11)", factor, 1.1570)
adjusted = raw_stephens * factor
check("normal-case A^{2*} (recomputed)", adjusted, 1.0954)
check("normal-case A^{2*} (article's 0.9468 chain)", 0.9468 * factor, 1.0954)
check("Stephens printed adjusted value", round(adjusted, 3), 1.095, tol=0)
# Normal case (both parameters estimated) percentage points for A^{2*}:
# 15% 0.576, 10% 0.656, 5% 0.787, 2.5% 0.918, 1% 1.092.
assert adjusted > 1.092, "adjusted value must exceed the 1% point"
print("ok   adjusted A^{2*} = 1.0954 > 1.092 (1% point) - rejects at 1%, narrowly")

# Factor properties quoted in the article and used in Check-yourself 3:
# f(5) = 0.8 is the minimum over n >= 5; f < 1 at n = 6; f > 1 for n >= 7;
# maximum about 1.16 near n = 12; f decreases towards 1 thereafter.
def adj_factor(n):
    return 1.0 + 4.0 / n - 25.0 / n ** 2

check("adjustment factor f(5)", adj_factor(5), 0.8, tol=1e-12)
check("adjustment factor f(6)", adj_factor(6), 0.9722)
check("adjustment factor f(7)", adj_factor(7), 1.0612)
check("adjustment factor f(12)", adj_factor(12), 1.1597)
check("adjustment factor f(13)", adj_factor(13), 1.1598)
check("adjustment factor f(100)", adj_factor(100), 1.0375)
assert min(adj_factor(n) for n in range(5, 2001)) == adj_factor(5), \
    "f(5) = 0.8 must be the minimum factor over n >= 5"
assert all(adj_factor(n) > 1.0 for n in range(7, 2001)), \
    "factor must exceed 1 for every n >= 7"
# Check-yourself 3: A^2 = 1.40, so A^{2*} >= 1.40 * 0.8 = 1.12 > 1.092 at
# every n >= 5 - the correct test rejects at the 1% level.
check("check3 lower bound 1.40 * 0.8", 1.40 * adj_factor(5), 1.12)
assert 1.40 * adj_factor(5) > 1.092
print("ok   factor: min 0.8 at n=5, >1 for n>=7, max ~1.16 near n=12; "
      "check3 bound 1.12 > 1.092")

if FAILURES:
    print(f"FAIL: {len(FAILURES)} check(s) failed")
    sys.exit(1)
print("PASS")
