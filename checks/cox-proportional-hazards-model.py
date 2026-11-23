"""Number check for the Cox proportional hazards model draft.

Recomputes, with plain Python arithmetic only (no repo imports):
  * the worked example (5 subjects, 1 binary covariate, 3 event times),
  * the Your-turn exercise (4 subjects, 2 event times; exact root log(sqrt(2))),
  * the hazard-ratio illustration (constant hazards 0.20 vs 0.14 per year),
  * the tied-event Breslow vs Efron denominators used in Check yourself Q2,
  * the Nelson-Aalen vs Kaplan-Meier contrast (exp(-1/2) vs 1 - 1/2),
  * the Breslow information at beta = 0 for the tied-event contrast.

Run:  python3 cox-proportional-hazards-model.py
Exit 0 means every asserted draft number agrees with recomputation
to the stated tolerance.
"""

import math

TOL = 1e-3


def close(name, got, want, tol=TOL):
    ok = abs(got - want) <= tol
    print(f"{'OK  ' if ok else 'FAIL'} {name}: got {got:.6f}, draft says {want:.6f}")
    return ok


def bisect_score(score, lo, hi):
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if score(lo) * score(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2.0


def main():
    ok = True

    # ------------------------------------------------------------------
    # Worked example.
    # Subjects (time, event indicator delta, binary x):
    #   1: (2, 1, 1)   2: (4, 1, 0)   3: (5, 0, 1)
    #   4: (7, 1, 1)   5: (9, 0, 0)
    # Risk sets: t=2: all 5; t=4: subjects 2,3,4,5; t=7: subjects 4,5.
    # L(beta) = [e^b/(3e^b+2)] * [1/(2e^b+2)] * [e^b/(e^b+1)]
    # ------------------------------------------------------------------
    def we_contribs(b):
        e = math.exp(b)
        return (e / (3 * e + 2), 1.0 / (2 * e + 2), e / (e + 1))

    def we_loglik(b):
        e = math.exp(b)
        return 2 * b - math.log(3 * e + 2) - math.log(2 * e + 2) - math.log(e + 1)

    def we_score(b):
        e = math.exp(b)
        return 2 - (3 * e / (3 * e + 2) + 2 * e / (2 * e + 2) + e / (e + 1))

    b_hat = bisect_score(we_score, 0.0, 1.0)
    e_hat = math.exp(b_hat)
    print(f"Worked example: beta_hat = {b_hat:.6f}, exp(beta_hat) = {e_hat:.6f}")
    ok &= close("beta_hat", b_hat, 0.564, tol=0.001)
    ok &= close("hazard ratio exp(beta_hat)", e_hat, 1.758, tol=0.002)

    for b, want_ll in [(0.0, -3.689), (0.25, -3.612), (0.5, -3.579),
                       (0.564, -3.578), (0.75, -3.589), (1.0, -3.638)]:
        ok &= close(f"log-likelihood at beta={b}", we_loglik(b), want_ll, tol=0.001)
    ok &= close("score at beta=0", we_score(0.0), 0.400)
    ok &= close("score at beta=0.5", we_score(0.5), 0.043)
    ok &= close("score at beta_hat", we_score(b_hat), 0.0, tol=1e-6)

    c1, c2, c3 = we_contribs(b_hat)
    ok &= close("contribution t=2 at beta_hat", c1, 0.242)
    ok &= close("contribution t=4 at beta_hat", c2, 0.181)
    ok &= close("contribution t=7 at beta_hat", c3, 0.637)
    ok &= close("partial likelihood at beta_hat", c1 * c2 * c3, 0.0279, tol=0.0002)
    ok &= close("partial likelihood at beta=0", 0.2 * 0.25 * 0.5, 0.025)

    # Schoenfeld residuals at beta_hat: observed x minus risk-set mean of x.
    r2 = 1 - 3 * e_hat / (3 * e_hat + 2)
    r4 = 0 - 2 * e_hat / (2 * e_hat + 2)
    r7 = 1 - e_hat / (e_hat + 1)
    ok &= close("Schoenfeld residual t=2", r2, 0.275)
    ok &= close("Schoenfeld residual t=4", r4, -0.637)
    ok &= close("Schoenfeld residual t=7", r7, 0.363)
    ok &= close("Schoenfeld residuals sum to score (0)", r2 + r4 + r7, 0.0, tol=1e-9)

    # Observed information at beta_hat, for a binary x: sum over event
    # times of p(1-p), where p is the risk-set mean of x. Its inverse
    # square root is the approximate standard error of beta_hat.
    ps = [3 * e_hat / (3 * e_hat + 2), 2 * e_hat / (2 * e_hat + 2),
          e_hat / (e_hat + 1)]
    info = sum(p * (1 - p) for p in ps)
    ok &= close("observed information at beta_hat", info, 0.662)
    ok &= close("approx. SE of beta_hat", 1 / math.sqrt(info), 1.229)

    # Breslow estimator of cumulative baseline hazard at beta_hat.
    h2, h4, h7 = 1 / (3 * e_hat + 2), 1 / (2 * e_hat + 2), 1 / (e_hat + 1)
    ok &= close("Breslow increment t=2", h2, 0.137)
    ok &= close("Breslow increment t=4", h4, 0.181)
    ok &= close("Breslow increment t=7", h7, 0.363)
    h0_7 = h2 + h4 + h7
    ok &= close("Breslow H0(7)", h0_7, 0.681)
    ok &= close("S0(7) = exp(-H0(7))", math.exp(-h0_7), 0.506)
    ok &= close("S(7|x=1) = exp(-H0(7) exp(beta_hat))",
                math.exp(-h0_7 * e_hat), 0.302)

    # ------------------------------------------------------------------
    # Your turn. Subjects: A (1,1,1), B (2,1,0), C (3,0,1), D (4,0,0).
    # L(beta) = [e^b/(2e^b+2)] * [1/(e^b+2)]; exact root e^b = sqrt(2).
    # ------------------------------------------------------------------
    def yt_contribs(b):
        e = math.exp(b)
        return (e / (2 * e + 2), 1.0 / (e + 2))

    def yt_score(b):
        e = math.exp(b)
        return 1 - (2 * e / (2 * e + 2) + e / (e + 2))

    b_yt = bisect_score(yt_score, 0.0, 1.0)
    e_yt = math.exp(b_yt)
    print(f"Your turn: beta_hat = {b_yt:.6f}, exp(beta_hat) = {e_yt:.6f}")
    ok &= close("Your-turn beta_hat vs log(sqrt(2))", b_yt, math.log(math.sqrt(2)), tol=1e-9)
    ok &= close("Your-turn exp(beta_hat) vs sqrt(2)", e_yt, math.sqrt(2), tol=1e-9)
    d1, d2 = yt_contribs(b_yt)
    ok &= close("Your-turn contribution t=1", d1, 0.293)
    ok &= close("Your-turn contribution t=2", d2, 0.293)
    ok &= close("Your-turn partial likelihood", d1 * d2, 0.0858, tol=0.0002)
    ok &= close("Your-turn Breslow H0(2)",
                1 / (2 * e_yt + 2) + 1 / (e_yt + 2), 0.500, tol=1e-9)
    ok &= close("Your-turn Schoenfeld residual t=1",
                1 - 2 * e_yt / (2 * e_yt + 2), 0.414)

    # ------------------------------------------------------------------
    # Hazard-ratio illustration (Common misconceptions):
    # constant hazards 0.20/yr (control) vs 0.14/yr (treated), HR = 0.70.
    # Risk by time t is 1 - exp(-hazard * t); median is log(2)/hazard.
    # ------------------------------------------------------------------
    for t, want_rr in [(1, 0.721), (5, 0.796), (10, 0.871)]:
        risk0 = 1 - math.exp(-0.20 * t)
        risk1 = 1 - math.exp(-0.14 * t)
        ok &= close(f"risk ratio at {t} year(s)", risk1 / risk0, want_rr)
    med0, med1 = math.log(2) / 0.20, math.log(2) / 0.14
    ok &= close("median survival, control", med0, 3.466)
    ok &= close("median survival, treated", med1, 4.951)
    ok &= close("median-survival ratio", med1 / med0, 1.429)

    # ------------------------------------------------------------------
    # Check yourself Q2: one tied time, d = 2, risk-set sum S = 10,
    # event-set sum E = 4. Breslow denominator S^2; Efron denominator
    # S * (S - E/2). Numerator is the same in both, so only the
    # denominators are compared here.
    # ------------------------------------------------------------------
    ok &= close("Breslow tied denominator", 10.0 ** 2, 100.0)
    ok &= close("Efron tied denominator", 10.0 * (10.0 - 4.0 / 2), 80.0)

    # ------------------------------------------------------------------
    # Nelson-Aalen vs Kaplan-Meier contrast (Baseline hazard section):
    # one event, two subjects at risk. Nelson-Aalen increment is 1/2,
    # so exp(-1/2) ~= 0.6065 (to 4 dp), whereas the Kaplan-Meier factor
    # for the same event is 1 - 1/2 = 0.5.
    # ------------------------------------------------------------------
    ok &= close("exp(-1/2) to 4 dp", round(math.exp(-0.5), 4), 0.6065, tol=1e-9)
    ok &= close("Kaplan-Meier factor 1 - 1/2", 1 - 1 / 2, 0.5, tol=1e-9)

    # ------------------------------------------------------------------
    # Breslow information at beta = 0 for the ties contrast
    # (Motivating example / Estimation): risk-set covariate values
    # {1, 1, 0, 0} (2 at risk in each group) with d = 2 tied events.
    # At beta = 0 all weights are 1, so the risk-set variance of x is
    # the plain variance 1/4, and I = d * Var(x) = 2 * 1/4 = 1/2.
    # (The log-rank hypergeometric variance in this case is 1/3.)
    # ------------------------------------------------------------------
    xs = [1, 1, 0, 0]
    mean_x = sum(xs) / len(xs)
    var_x = sum((x - mean_x) ** 2 for x in xs) / len(xs)
    ok &= close("risk-set Var(x) for {1,1,0,0}", var_x, 0.25, tol=1e-9)
    ok &= close("Breslow information at beta=0, d=2", 2 * var_x, 0.5, tol=1e-9)

    print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
