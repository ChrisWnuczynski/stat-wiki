# Benjamini–Hochberg

Type: Concept. Rank 286. Tier: lighter.

## Facts

- **Checked:** ESL 12th printing, pp. 687–689. FDR is E(V/R). Algorithm 18.2 uses the strict cutoff p(j) < alpha j/M. Equation (18.45) states FDR <= (M0/M) alpha under independence. The proof is described as complicated and is not reproduced.
- **Checked by code:** For the five p-values at q*=0.05, both the closed and strict rules give k=4. At q*=0.02, k=1. The tie at 0.030 gives k=3 closed and k=2 strict. The set beginning 0.04 rejects nothing at q*=0.05.
- **Assumed:** The p-values are valid inputs to the procedure. Dependence conditions for the FDR bound were not re-derived.
- **Disputed:** The page definition uses a closed inequality. ESL's algorithm uses a strict inequality. The article states both and uses an example where they agree, plus one example where they do not.

## Sources opened

Hastie, Tibshirani and Friedman (2009), pp. 687–689. Key `hastie_esl2009`. Benjamini and Hochberg (1995) was not opened.

## Proofs

No FDR proof. Logged.
