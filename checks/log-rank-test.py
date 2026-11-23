#!/usr/bin/env python3
"""Number check for the stat-wiki log-rank-test draft article.

Recomputes, with plain Python arithmetic only (fractions for exactness,
math.erfc for the chi-squared(1 df) tail probability), every number in the
Worked example and the Your turn exercise of
research/content/log-rank-test.md.

No repo code is imported. No external data. Run: python3 log-rank-test.py

Conventions (matching the article):
  - Each observation is (time, event) with event = 1 for an observed event,
    0 for right-censoring at that time.
  - At each distinct event time t_j, the risk set is everyone with
    observed time >= t_j (a person censored at t_j is at risk at t_j).
  - Focal group is group 1.  O_j = events in group 1 at t_j,
    E_j = d_j * n_1j / n_j,  V_j = d_j * (n_1j/n_j) * (1 - n_1j/n_j)
           * (n_j - d_j) / (n_j - 1)   [hypergeometric variance;
           V_j = 0 when n_j = 1, by the (n_j - d_j) factor]
    Z = sum(O_j - E_j) / sqrt(sum V_j);  chi2 = Z^2 ~ chi2_1 approx.
  - For chi2 on 1 df, p = erfc(sqrt(chi2 / 2)).
"""

import math
from itertools import combinations
from fractions import Fraction as F

# ---------------------------------------------------------------- worked example
# Group A (focal): events at 1, 2, 3, 5; censored at 4.
# Group B:        events at 6, 7, 8, 9; censored at 10.  Times in months.
A = [(1, 1), (2, 1), (3, 1), (4, 0), (5, 1)]
B = [(6, 1), (7, 1), (8, 1), (9, 1), (10, 0)]

# ------------------------------------------------------------------- your turn
# Group C (focal): events at 2, 3, 5, 8; censored at 7.
# Group D:        events at 4, 6, 9, 10; censored at 12.  Times in months.
C = [(2, 1), (3, 1), (5, 1), (7, 0), (8, 1)]
D = [(4, 1), (6, 1), (9, 1), (10, 1), (12, 0)]


def logrank(g1, g2, label):
    """Return per-event-time rows and totals for focal group g1."""
    times = sorted({t for t, e in g1 + g2 if e == 1})
    rows = []
    for t in times:
        n1 = sum(1 for y, _ in g1 if y >= t)
        n2 = sum(1 for y, _ in g2 if y >= t)
        n = n1 + n2
        d1 = sum(1 for y, e in g1 if y == t and e == 1)
        d2 = sum(1 for y, e in g2 if y == t and e == 1)
        d = d1 + d2
        E = F(d * n1, n) if n else F(0)
        if n > 1:
            V = F(d, 1) * F(n1, n) * F(n - n1, n) * F(n - d, n - 1)
        else:
            V = F(0)
        rows.append((t, n1, n2, n, d1, d, E, V))
    O = sum(r[4] for r in rows)
    Etot = sum((r[6] for r in rows), F(0))
    Vtot = sum((r[7] for r in rows), F(0))
    diff = F(O) - Etot
    Z = float(diff) / math.sqrt(float(Vtot))
    chi2 = Z * Z
    p = math.erfc(math.sqrt(chi2 / 2.0))
    print(f"--- {label} ---")
    print(f"{'t':>3} {'n1':>3} {'n2':>3} {'n':>3} {'d1':>3} {'d':>3} "
          f"{'E':>9} {'V':>9} {'O-E':>9}")
    for t, n1, n2, n, d1, d, E, V in rows:
        print(f"{t:>3} {n1:>3} {n2:>3} {n:>3} {d1:>3} {d:>3} "
              f"{float(E):9.4f} {float(V):9.4f} {float(F(d1) - E):9.4f}"
              f"   E={E}  V={V}")
    print(f"O = {O},  E = {Etot} = {float(Etot):.4f},  "
          f"V = {Vtot} = {float(Vtot):.4f}")
    print(f"O - E = {diff} = {float(diff):.4f}")
    print(f"Z = {Z:.4f},  chi2 = Z^2 = {chi2:.4f},  p = {p:.4f}")
    print(f"exact: Z = {diff}/sqrt({Vtot}), "
          f"chi2 = {(diff * diff) / Vtot} = {float((diff * diff) / Vtot):.4f}")
    print()
    return {"rows": rows, "O": O, "E": Etot, "V": Vtot,
            "diff": diff, "Z": Z, "chi2": chi2, "p": p}


def main():
    w = logrank(A, B, "Worked example (focal group A)")
    y = logrank(C, D, "Your turn (focal group C)")

    # Article's stated values, as exact fractions / rounded decimals.
    assert w["O"] == 4 and w["E"] == F(107, 72) and w["V"] == F(4511, 5184)
    assert w["diff"] == F(181, 72)
    assert abs(w["Z"] - 2.6949) < 0.0005, w["Z"]
    assert abs(w["chi2"] - 7.2625) < 0.0005, w["chi2"]
    assert abs(w["p"] - 0.0070) < 0.0005, w["p"]

    assert y["O"] == 4 and y["E"] == F(1175, 504)
    assert y["diff"] == F(841, 504)
    assert abs(y["Z"] - 1.4174) < 0.0005, y["Z"]
    assert abs(y["chi2"] - 2.0091) < 0.0005, y["chi2"]
    assert abs(y["p"] - 0.1564) < 0.0005, y["p"]

    # Cross-check of the Bland & Altman (2004) glioma figures quoted in the
    # article (their simpler sum (O-E)^2/E form, not the (O-E)^2/V form):
    # O = 14 vs E = 22.48 and O = 28 vs E = 19.52, chi2 = 6.88.
    ba = (14 - 22.48) ** 2 / 22.48 + (28 - 19.52) ** 2 / 19.52
    print(f"Bland & Altman (2004) check: sum (O-E)^2/E = {ba:.4f} "
          f"(article states 6.88)")
    assert abs(ba - 6.88) < 0.005, ba

    # Check yourself Q3: O - E = 6, V = 9  =>  Z = 2, chi2 = 4,
    # two-sided p = 2 * (1 - Phi(2)) = erfc(sqrt(2)).
    z3 = 6 / math.sqrt(9)
    p3 = math.erfc(math.sqrt(4 / 2.0))
    print(f"Check yourself Q3: Z = {z3:.4f}, chi2 = {z3 ** 2:.4f}, "
          f"p = {p3:.4f} (article states 2, 4, 0.0455)")
    assert z3 == 2.0 and abs(p3 - 0.0455) < 0.0005, p3

    # Ties contrast quoted in the article (Properties, "Relation to the Cox
    # model"): one event time with n = 4 at risk, n1 = 2 of them in group 1,
    # and d = 2 tied events, both in group 1.
    # (a) Hypergeometric (log-rank) variance, exact rational arithmetic:
    #     V = d * (n1/n) * (1 - n1/n) * (n - d)/(n - 1)
    #       = 2 * (1/2) * (1/2) * (2/3) = 1/3.
    n_t, n1_t, d_t = 4, 2, 2
    v_hyp = F(d_t) * F(n1_t, n_t) * F(n_t - n1_t, n_t) * F(n_t - d_t, n_t - 1)
    print(f"Ties contrast: hypergeometric variance V = {v_hyp} "
          f"(article states 1/3)")
    assert v_hyp == F(1, 3), v_hyp

    # (b) Breslow partial-likelihood information at beta = 0 for the same
    #     configuration: risk-set group indicators {1, 1, 0, 0},
    #     I = d * Var(indicator) = 2 * 1/4 = 1/2.
    risk = [F(1), F(1), F(0), F(0)]
    mean_r = sum(risk) / len(risk)
    var_r = sum((x - mean_r) ** 2 for x in risk) / len(risk)
    info_breslow = F(d_t) * var_r
    print(f"Ties contrast: Breslow information at beta = 0: "
          f"Var = {var_r}, I = d * Var = {info_breslow} "
          f"(article states 1/2)")
    assert var_r == F(1, 4) and info_breslow == F(1, 2), info_breslow
    assert v_hyp != info_breslow  # the two variances genuinely differ

    # Enumerate the exact conditional null failing subsets, independently
    # of the closed-form hypergeometric moments, including all-fail/empty
    # groups and no-tie configurations. This checks the claimed equality
    # rather than merely repeating the variance formula.
    for n in range(2, 9):
        for n1 in range(n + 1):
            for d in range(1, n + 1):
                totals = [sum(i < n1 for i in subset)
                          for subset in combinations(range(n), d)]
                mean = F(sum(totals), len(totals))
                variance = sum((F(z) - mean) ** 2 for z in totals) / len(totals)
                assert mean == F(d * n1, n)
                assert variance == F(d) * F(n1, n) * F(n - n1, n) * F(n - d, n - 1)
    exact_counts = [sum(i < 2 for i in pair) for pair in combinations(range(4), 2)]
    exact_mean = F(sum(exact_counts), len(exact_counts))
    exact_info = sum((F(z) - exact_mean) ** 2 for z in exact_counts) / len(exact_counts)
    assert exact_info == v_hyp == F(1, 3)
    score = F(2) - exact_mean
    assert score == 1 and score ** 2 / exact_info == 3
    assert score ** 2 / info_breslow == 2

    # Three groups, but the third is absent from the informative risk set:
    # enumerated covariance has rank one, not g-1=2.
    groups = [0, 0, 1, 1]
    counts = [[sum(groups[i] == g for i in pair) for g in range(3)]
              for pair in combinations(range(4), 2)]
    means = [F(sum(row[g] for row in counts), len(counts)) for g in range(3)]
    cov = [[sum((F(row[g]) - means[g]) * (F(row[h]) - means[h])
                for row in counts) / len(counts) for h in range(3)] for g in range(3)]
    assert cov == [[F(1, 3), -F(1, 3), F(0)],
                   [-F(1, 3), F(1, 3), F(0)], [F(0), F(0), F(0)]]
    assert all(sum(row) == 0 for row in cov)
    # The second row is minus the nonzero first row and the third is zero.
    assert cov[0][0] > 0 and cov[1] == [-x for x in cov[0]] and not any(cov[2])
    print("Exact conditional moments and degenerate three-group rank passed.")

    print("All checks passed.")


if __name__ == "__main__":
    main()
