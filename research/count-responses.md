# Count responses

Type: Concept. Rank 292. Tier: lighter.

## Facts

- **Checked:** ESL 12th printing, p. 296, lists g(mu)=log(mu) for Poisson count data.
- **Checked by code:** exp(-1.5) rounds to 0.2231, exp(-0.2) to 0.8187, exp(-1.7) to 0.1827, exp(0.5) to 1.6487, exp(0.3) to 1.3499, and exp(-0.4) to 0.6703. The exact ratio exp(0.3)/exp(0.5) equals exp(-0.2). The identity 2-0.5x is zero at x=4.
- **Assumed:** The mean is the conditional mean of a nonnegative integer response. Poisson variance equal to the mean is the usual starting component and was not re-derived from the Poisson pmf in this note.
- **Disputed:** Nothing numerical. The product of the four-decimal rounds is not claimed to equal the exact exponential; both the exact mean and the rounded product are described separately.

## Sources opened

Hastie, Tibshirani and Friedman (2009), p. 296. Key `hastie_esl2009`.

## Proofs

The multiplicative effect of a log-link coefficient is proved.
