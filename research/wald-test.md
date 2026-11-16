# Wald test

Type: Concept. Rank 289. Tier: lighter.

## Facts

- **Checked:** ESL 12th printing, p. 122, defines the logistic Z score as the coefficient divided by its standard error and calls it a Wald test. A Z score larger than about 2 is described as significant at 5%. Page 125 states the normal limit with covariance (X^T W X)^{-1} and identifies the Wald test as a test for dropping a term from the current weighted least-squares fit.
- **Checked by code:** z_{0.975} rounds to 1.960. Z=0.8/0.25=3.2 has two-sided p-value 0.0014. Z=3 has p-value 0.0027. Z=1 has p-value 0.3173. 2{1-Phi(1.96)} rounds to 0.0500.
- **Assumed:** The standard error is positive and finite. The normal tail is the reference distribution of the approximation, not an exact law.
- **Disputed:** Nothing numerical. The asymptotic expansion was not proved. ESL's printed South African heart-disease Z scores were not recomputed from the data, and they are not used.

## Sources opened

Hastie, Tibshirani and Friedman (2009), pp. 122 and 125. Key `hastie_esl2009`.

## Proofs

The normal tail probabilities of the worked statistics are computed. The asymptotic N(0,1) null limit is logged.
