"""McNemar's test checks for gap batch 3.
Reproduces: Fagerland, Lydersen & Laake (2013) Table 6 (Bentur and Cavo data) and
McNemar (1955, 2nd ed.) Table 28 / formula (87): chi2 = (29-10)^2/39 = 9.26, CR = 3.04."""
from math import comb, sqrt
from scipy.stats import norm, chi2, binom

def tests(b, c):
    n = b + c
    z = (b - c) / sqrt(n)
    p_asym = 2 * norm.sf(abs(z))
    zcc = (abs(b - c) - 1) / sqrt(n)
    p_cc = 2 * norm.sf(zcc)
    k = min(b, c)
    p_exact = min(1.0, 2 * binom.cdf(k, n, 0.5))
    p_mid = p_exact - binom.pmf(k, n, 0.5)  # Fagerland: exact minus half the point prob, two-sided => minus pmf
    return dict(n=n, z=z, chi2=z*z, p_asym=p_asym, chi2_cc=zcc**2, p_cc=p_cc, p_exact=p_exact, p_mid=p_mid)

def exact_unconditional(table):
    """Suissa-Shuster exact unconditional test (Fagerland 2013): maximise over nuisance p of
    P(|Z|>=|z_obs|) where (n12, n21, rest) ~ Multinomial(N; p/2, p/2, 1-p) under H0 (p = n12+n21 prob)."""
    import numpy as np
    n11, n12, n21, n22 = table
    N = sum(table)
    zobs = abs(n12 - n21) / sqrt(n12 + n21)
    best = 0
    for p in np.linspace(0.0001, 0.9999, 9999):
        tot = 0.0
        for m in range(1, N + 1):  # m discordant pairs
            pm = comb(N, m) * p**m * (1 - p)**(N - m)
            for x in range(m + 1):
                if abs(2 * x - m) / sqrt(m) >= zobs - 1e-12:
                    tot += pm * comb(m, x) * 0.5**m
        best = max(best, tot)
    return best

if __name__ == "__main__":
    print("Bentur (Fagerland Table 1): discordant 1 (AHR->no) vs 7 (no->AHR)")
    r = tests(1, 7); print({k: round(v, 4) for k, v in r.items()})
    print("  printed Table 6: asym 0.0339, CC 0.0771, exact 0.0703, mid-p 0.0391, uncond 0.0353")
    print("  exact unconditional:", round(exact_unconditional((1, 1, 7, 12)), 4))
    print("  marginal proportions before/after:", 2/21, 8/21, "diff", 8/21-2/21)
    print("Cavo (Fagerland Table 2): discordant 6 vs 16")
    r = tests(6, 16); print({k: round(v, 4) for k, v in r.items()})
    print("  printed Table 6: asym 0.0330, CC 0.0550, exact 0.0525, mid-p 0.0347, uncond 0.0342")
    print("McNemar 1955 Table 28 items 1 vs 2: A=10, D=29, N=100")
    r = tests(10, 29); print({k: round(v, 4) for k, v in r.items()})
    print("  printed p.230: chi2 9.26; CR (.68-.49)/sqrt(39)/10 =", round(0.19/ (sqrt(39)/100), 2), "(printed 3.04; .0624 rounded SE)")
    # SE of difference of correlated proportions (McNemar p.59): sqrt((a+d)/N) with a=A/N, d=D/N
    print("  SE_D =", sqrt((0.10+0.29)/100))
    # Contrast: wrongly treating the margins as independent samples
    from scipy.stats import chi2_contingency
    ct = [[49, 51], [68, 32]]
    print("  wrong independent-samples chi2 (no CC):", chi2_contingency(ct, correction=False)[:2])
    p1, p2 = .49, .68; pbar = (p1+p2)/2
    zind = (p2-p1)/sqrt(pbar*(1-pbar)*2/100)
    print("  wrong two-sample z:", round(zind, 3), "p", round(2*norm.sf(zind), 4))
