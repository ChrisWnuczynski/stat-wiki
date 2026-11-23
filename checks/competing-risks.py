#!/usr/bin/env python3
"""Number check for the stat-wiki 'competing-risks' draft.

Recomputes, with exact rational arithmetic (fractions.Fraction),
every number quoted in the Worked example and in the Your turn
answer of ~/workspace/stat-wiki-s1/drafts/competing-risks.md.

Method (no repo code, no imports beyond the standard library):
  * Subjects are (time, outcome) with outcome 0 = right-censored,
    1 = event of interest (cause 1), 2 = competing event (cause 2).
    No tied event times occur in either data set, so the risk set
    just before an event time u is simply the subjects with
    observed time >= u.
  * Kaplan-Meier for cause 1 alone (the naive calculation):
    at each cause-1 event time u, multiply by (1 - d1(u)/n(u));
    cause-2 events and censorings only remove subjects from later
    risk sets.  The naive risk is 1 - S_KM1(t).
  * Overall survival S_all(t): Kaplan-Meier with ANY event
    (cause 1 or cause 2) as the event; only censoring removes
    subjects without an event.
  * Aalen-Johansen CIF for cause k:
        F_k(t) = sum over event times u <= t of
                 S_all(u-) * d_k(u) / n(u),
    where S_all(u-) is overall survival just before u.
  * Checks: at each evaluation time, F_1(t) + F_2(t) == 1 - S_all(t),
    and the naive 1 - S_KM1(t) exceeds F_1(t).

Run:  python3 competing-risks.py   (exit code 0 iff all checks pass)
"""

from fractions import Fraction as F

# ---------------------------------------------------------------- worked example
# 10 patients after bone-marrow transplant; time in months.
# cause 1 = relapse (event of interest), cause 2 = death without relapse.
WORKED = [
    ("A", 2, 1),
    ("B", 3, 2),
    ("C", 4, 1),
    ("D", 5, 0),
    ("E", 6, 2),
    ("F", 7, 1),
    ("G", 8, 0),
    ("H", 9, 1),
    ("I", 10, 2),
    ("J", 12, 0),
]

# ---------------------------------------------------------------- your turn
# 8 patients; cause 1 = event of interest, cause 2 = competing event.
YOUR_TURN = [
    ("A", 1, 1),
    ("B", 2, 2),
    ("C", 3, 0),
    ("D", 4, 1),
    ("E", 5, 2),
    ("F", 6, 1),
    ("G", 7, 0),
    ("H", 8, 2),
]


def risk_set(data, u):
    """Number at risk just before time u (observed time >= u)."""
    return sum(1 for _, t, _ in data if t >= u)


def km_cause1(data, t_eval):
    """Kaplan-Meier survival for cause 1 only, at t_eval.

    Cause-2 events are treated as censoring, as in the naive analysis.
    """
    s = F(1)
    for _, u, outcome in sorted(data, key=lambda r: r[1]):
        if u > t_eval or outcome != 1:
            continue
        n = risk_set(data, u)
        s *= F(n - 1, n)
    return s


def overall_survival(data, t_eval):
    """Kaplan-Meier survival for ANY event (cause 1 or 2), at t_eval."""
    s = F(1)
    for _, u, outcome in sorted(data, key=lambda r: r[1]):
        if u > t_eval or outcome == 0:
            continue
        n = risk_set(data, u)
        s *= F(n - 1, n)
    return s


def cif(data, cause, t_eval):
    """Aalen-Johansen cumulative incidence for `cause` at t_eval."""
    total = F(0)
    for _, u, outcome in sorted(data, key=lambda r: r[1]):
        if u > t_eval:
            continue
        n = risk_set(data, u)
        # Overall survival just before u: evaluate at the previous
        # event time, i.e. recompute the product over event times < u.
        s_before = F(1)
        for _, v, out2 in sorted(data, key=lambda r: r[1]):
            if v >= u or out2 == 0:
                continue
            s_before *= F(risk_set(data, v) - 1, risk_set(data, v))
        if outcome == cause:
            total += s_before * F(1, n)
    return total


def report(data, label, times):
    print(f"--- {label} ---")
    for t in times:
        s_km1 = km_cause1(data, t)
        naive = 1 - s_km1
        s_all = overall_survival(data, t)
        f1 = cif(data, 1, t)
        f2 = cif(data, 2, t)
        print(
            f"t={t}: KM1 S={s_km1} ({float(s_km1):.4f})  "
            f"naive 1-KM={naive} ({float(naive):.4f})  "
            f"S_all={s_all} ({float(s_all):.4f})  "
            f"CIF1={f1} ({float(f1):.4f})  CIF2={f2} ({float(f2):.4f})  "
            f"CIF1+CIF2={f1 + f2}  1-S_all={1 - s_all}"
        )
        assert f1 + f2 == 1 - s_all, "CIFs must sum to 1 - S_all(t)"
        assert naive >= f1, "naive 1-KM must not be below the CIF"
    print()


def main():
    report(WORKED, "Worked example (10 subjects)", [2, 4, 7, 9])
    report(YOUR_TURN, "Your turn (8 subjects)", [4, 6])

    # Exact values quoted in the draft.
    assert km_cause1(WORKED, 7) == F(63, 100)      # S_KM1(7) = 0.63
    assert 1 - km_cause1(WORKED, 7) == F(37, 100)  # naive risk at 7 = 0.37
    assert cif(WORKED, 1, 7) == F(19, 60)          # AJ CIF1(7) = 0.3167
    assert km_cause1(WORKED, 9) == F(42, 100)      # S_KM1(9) = 0.42
    assert 1 - km_cause1(WORKED, 9) == F(29, 50)   # naive risk at 9 = 0.58
    assert cif(WORKED, 1, 9) == F(17, 36)          # AJ CIF1(9) = 0.4722
    assert cif(WORKED, 2, 9) == F(13, 60)          # AJ CIF2(9) = 0.2167
    assert overall_survival(WORKED, 9) == F(14, 45)

    assert km_cause1(YOUR_TURN, 4) == F(7, 10)     # S_KM1(4) = 0.70
    assert 1 - km_cause1(YOUR_TURN, 4) == F(3, 10)  # naive risk at 4 = 0.30
    assert cif(YOUR_TURN, 1, 4) == F(11, 40)       # AJ CIF1(4) = 0.275
    assert km_cause1(YOUR_TURN, 6) == F(7, 15)     # S_KM1(6) = 0.4667
    assert 1 - km_cause1(YOUR_TURN, 6) == F(8, 15)  # naive risk at 6 = 0.5333
    assert cif(YOUR_TURN, 1, 6) == F(17, 40)       # AJ CIF1(6) = 0.425
    assert cif(YOUR_TURN, 2, 6) == F(11, 40)       # AJ CIF2(6) = 0.275

    print("All checks passed: every number quoted in the draft is exact.")


if __name__ == "__main__":
    main()
