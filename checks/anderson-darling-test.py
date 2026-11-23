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
# Case 0 (fully specified) asymptotic percentage points (Stephens 1974, Table 1):
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
# Stephens' illustration: A^2 = 0.947 at n = 11, adjustment factor
# 1 + 0.75/11 + 2.25/121 = 1.0868, giving A^{2*} = 1.029.
factor = 1.0 + 0.75 / 11 + 2.25 / 121
check("normal-case adjustment factor (n=11)", factor, 1.0868)
check("normal-case A^{2*} (0.947 adjusted)", 0.947 * factor, 1.029, tol=5e-4)
# Normal case (both parameters estimated) percentage points for A^{2*}:
# 15% 0.576, 10% 0.656, 5% 0.787, 2.5% 0.918, 1% 1.092.
assert 0.947 * factor < 1.092, "adjusted value must fall below the 1% point"
print("ok   adjusted A^{2*} = 1.029 < 1.092 (significant at about the 1% level)")

if FAILURES:
    print(f"FAIL: {len(FAILURES)} check(s) failed")
    sys.exit(1)
print("PASS")
