# Link function

Type: Concept. Rank 288. Tier: lighter.

## Facts

- **Checked:** ESL 12th printing, p. 296, lists the identity, logit, probit and log links, and writes the logit equation (9.2).
- **Checked by code:** At eta=1.5 the log mean rounds to 4.4817 and the logit mean to 0.8176. At eta=-1 they round to 0.3679 and 0.2689. exp(0.2) rounds to 1.2214.
- **Assumed:** The mean is the conditional mean of the response given the covariates.
- **Disputed:** Nothing numerical. Complementary log-log is not on this ESL page; it is treated on its own article.

## Sources opened

Hastie, Tibshirani and Friedman (2009), p. 296. Key `hastie_esl2009`.

## Proofs

Positivity of the exponential and the unit-interval range of the logistic are proved.
