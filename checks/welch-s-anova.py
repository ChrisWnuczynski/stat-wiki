"""Number check for welch-s-anova.md -- plain Python stdlib only.

Recomputes every number quoted in the article: group means and sample
variances, Welch weights, weighted mean, weighted between-group sum of
squares, correction term A, Welch F, numerator and denominator degrees
of freedom, p-values (via a regularised incomplete beta implemented here
with a continued fraction), the classic one-way ANOVA F on the same data,
Games-Howell pair-specific degrees of freedom, and the Your turn exercise.
Prints PASS and exits 0 when all quoted values agree within tolerance.
"""
import math
import sys

TOL = 5e-4  # quoted values are rounded to 3-4 decimal places


def betacf(a, b, x):
    maxit, eps, fpmin = 200, 3e-14, 1e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < fpmin:
        d = fpmin
    d = 1.0 / d
    h = d
    for m in range(1, maxit + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < fpmin:
            d = fpmin
        c = 1.0 + aa / c
        if abs(c) < fpmin:
            c = fpmin
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < fpmin:
            d = fpmin
        c = 1.0 + aa / c
        if abs(c) < fpmin:
            c = fpmin
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < eps:
            break
    return h


def betai(a, b, x):
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    bt = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
                  + a * math.log(x) + b * math.log(1.0 - x))
    if x < (a + 1.0) / (a + b + 2.0):
        return bt * betacf(a, b, x) / a
    return 1.0 - bt * betacf(b, a, 1.0 - x) / b


def f_sf(f, d1, d2):
    """Upper-tail probability P(F >= f) for F on (d1, d2) df."""
    return betai(d2 / 2.0, d1 / 2.0, d2 / (d2 + d1 * f))


failures = []


def check(label, computed, quoted):
    ok = abs(computed - quoted) <= TOL * max(1.0, abs(quoted)) + 5e-4
    print(f"{'ok  ' if ok else 'FAIL'} {label}: computed={computed:.6f} quoted={quoted}")
    if not ok:
        failures.append(label)


def analyse(groups, tag, quoted):
    k = len(groups)
    ns = [len(g) for g in groups]
    n_total = sum(ns)
    means = [sum(g) / len(g) for g in groups]
    ss_within = [sum((x - m) ** 2 for x in g) for g, m in zip(groups, means)]
    variances = [s / (n - 1) for s, n in zip(ss_within, ns)]
    for i in range(k):
        check(f"{tag} n[{i}]", ns[i], quoted["n"][i])
        check(f"{tag} mean[{i}]", means[i], quoted["means"][i])
        check(f"{tag} var[{i}]", variances[i], quoted["vars"][i])
    w = [n / v for n, v in zip(ns, variances)]
    total_w = sum(w)
    wmean = sum(wi * m for wi, m in zip(w, means)) / total_w
    wss = sum(wi * (m - wmean) ** 2 for wi, m in zip(w, means))
    a_term = sum((1.0 - wi / total_w) ** 2 / (n - 1) for wi, n in zip(w, ns))
    corr = 1.0 + 2.0 * (k - 2) / (k * k - 1) * a_term
    f_welch = (wss / (k - 1)) / corr
    df2 = (k * k - 1) / (3.0 * a_term)
    p_welch = f_sf(f_welch, k - 1, df2)
    for i in range(k):
        check(f"{tag} w[{i}]", w[i], quoted["w"][i])
    check(f"{tag} W", total_w, quoted["W"])
    check(f"{tag} weighted mean", wmean, quoted["wmean"])
    check(f"{tag} weighted SSB", wss, quoted["wss"])
    check(f"{tag} A", a_term, quoted["A"])
    check(f"{tag} correction", corr, quoted["corr"])
    check(f"{tag} Welch F", f_welch, quoted["F"])
    check(f"{tag} df1", k - 1, quoted["df1"])
    check(f"{tag} df2", df2, quoted["df2"])
    check(f"{tag} Welch p", p_welch, quoted["p"])
    # Classic one-way ANOVA on the same data.
    grand = sum(sum(g) for g in groups) / n_total
    ssb = sum(n * (m - grand) ** 2 for n, m in zip(ns, means))
    ssw = sum(ss_within)
    f_classic = (ssb / (k - 1)) / (ssw / (n_total - k))
    p_classic = f_sf(f_classic, k - 1, n_total - k)
    check(f"{tag} grand mean", grand, quoted["grand"])
    check(f"{tag} classic SSB", ssb, quoted["SSB"])
    check(f"{tag} classic SSW", ssw, quoted["SSW"])
    check(f"{tag} classic MSB", ssb / (k - 1), quoted["MSB"])
    check(f"{tag} classic MSW", ssw / (n_total - k), quoted["MSW"])
    check(f"{tag} classic F", f_classic, quoted["Fc"])
    check(f"{tag} classic p", p_classic, quoted["pc"])
    # Games-Howell pair-specific Welch-Satterthwaite degrees of freedom.
    gh = {}
    for i in range(k):
        for j in range(i + 1, k):
            a = variances[i] / ns[i]
            b = variances[j] / ns[j]
            gh[(i, j)] = (a + b) ** 2 / (a * a / (ns[i] - 1) + b * b / (ns[j] - 1))
    return gh


# ---- Worked example (article) -------------------------------------------
main_groups = [
    [8, 9, 10, 11, 12],
    [13, 15, 17, 15],
    [10, 14, 18, 22, 26, 14, 18, 22],
]
main_quoted = {
    "n": [5, 4, 8], "means": [10.0, 15.0, 18.0],
    "vars": [2.5, 2.6667, 27.4286],
    "w": [2.0, 1.5, 0.2917], "W": 3.7917, "wmean": 12.5934,
    "wss": 30.6648, "A": 0.2993, "corr": 1.0748,
    "F": 14.2650, "df1": 2, "df2": 8.9094, "p": 0.0017,
    "grand": 14.9412, "SSB": 196.9412, "SSW": 210.0,
    "MSB": 98.4706, "MSW": 15.0, "Fc": 6.5647, "pc": 0.0097,
}
gh = analyse(main_groups, "main", main_quoted)
# Article wording check (review fix): w3/w1 = (8/(192/7)) / (5/2.5) = 7/48
# = 0.145833..., which is slightly MORE than 1/7 = 0.142857..., not less.
_w3 = 8 / (192 / 7)
_w1 = 5 / 2.5
check("main w3/w1 ratio", _w3 / _w1, 7 / 48)
assert _w3 / _w1 > 1 / 7, "w3/w1 must exceed 1/7"
print("ok   main w3/w1 = 7/48 = 0.14583 > 1/7 (slightly more than one seventh)")
check("main GH df pair 1-2", gh[(0, 1)], 6.4615)
check("main GH df pair 1-3", gh[(0, 2)], 8.8608)
check("main GH df pair 2-3", gh[(1, 2)], 9.1773)

# ---- Your turn exercise (article, hidden answer) ------------------------
yt_groups = [
    [5, 7, 9, 7],
    [9, 10, 11, 12, 13],
    [12, 16, 20, 24, 16, 20],
]
yt_quoted = {
    "n": [4, 5, 6], "means": [7.0, 11.0, 18.0],
    "vars": [2.6667, 2.5, 17.6],
    "w": [1.5, 2.0, 0.3409], "W": 3.8409, "wmean": 10.0592,
    "wss": 37.3047, "A": 0.3473, "corr": 1.0868,
    "F": 17.1622, "df1": 2, "df2": 7.6779, "p": 0.0015,
    "grand": 12.7333, "SSB": 312.9333, "SSW": 106.0,
    "MSB": 156.4667, "MSW": 8.8333, "Fc": 17.7132, "pc": 0.0003,
}
analyse(yt_groups, "yourturn", yt_quoted)

# ---- Check yourself 1: k = 2 reduction ----------------------------------
# Groups 1 and 2 of the worked example: Welch F must equal t^2 and the
# denominator df from (k^2-1)/(3A) must equal the Welch-Satterthwaite df.
g1, g2 = main_groups[0], main_groups[1]
n1, n2 = len(g1), len(g2)
m1, m2 = sum(g1) / n1, sum(g2) / n2
v1 = sum((x - m1) ** 2 for x in g1) / (n1 - 1)
v2 = sum((x - m2) ** 2 for x in g2) / (n2 - 1)
t_stat = (m1 - m2) / math.sqrt(v1 / n1 + v2 / n2)
w1, w2 = n1 / v1, n2 / v2
wtot = w1 + w2
a2 = (1 - w1 / wtot) ** 2 / (n1 - 1) + (1 - w2 / wtot) ** 2 / (n2 - 1)
df_formula = (2 * 2 - 1) / (3 * a2)
df_ws = (v1 / n1 + v2 / n2) ** 2 / ((v1 / n1) ** 2 / (n1 - 1) + (v2 / n2) ** 2 / (n2 - 1))
wm2 = (w1 * m1 + w2 * m2) / wtot
f_k2 = (w1 * (m1 - wm2) ** 2 + w2 * (m2 - wm2) ** 2) / 1  # k-1 = 1, correction = 1
check("k=2 Welch F equals t^2", f_k2, round(t_stat ** 2, 4))
check("k=2 t^2 quoted", t_stat ** 2, 21.4286)
check("k=2 df from (k^2-1)/(3A)", df_formula, round(df_ws, 4))
check("k=2 df quoted", df_ws, 6.4615)

# ---- Check yourself 3: A and df2 from given weights ---------------------
# w = (1, 2, 3), n = (6, 6, 6), k = 3: W = 6, A and df2 as quoted in article.
w_q = [1.0, 2.0, 3.0]
n_q = [6, 6, 6]
wq = sum(w_q)
a_q = sum((1 - wi / wq) ** 2 / (n - 1) for wi, n in zip(w_q, n_q))
check("check3 A", a_q, 0.2778)
check("check3 df2", (9 - 1) / (3 * a_q), 9.6)
check("check3 correction", 1 + 2 * (3 - 2) / (9 - 1) * a_q, 1.0694)

if failures:
    print("FAIL:", failures)
    sys.exit(1)
print("PASS")
