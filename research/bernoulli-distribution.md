# Bernoulli distribution — research record

Page type: distribution, rank 84. Baseline 862 words and two figures; preserve PMF/CDF plots, infobox, existing binary-check example, source proof, binomial relationship and history.

## Sources opened

- Kyle Siegrist, *Probability, Mathematical Statistics, and Stochastic Processes*, §11.1 “Introduction to Bernoulli Trials,” at the author-hosted Random Services site and Statistics LibreTexts: https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/11:_Bernoulli_Trials/11.01:_Introduction_to_Bernoulli_Trials . Read definition, moments, simulation, examples and reliability subsections. New bibliography entry requested in pending JSON.
- Same book, §11.2 “The Binomial Distribution,” at https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/11:_Bernoulli_Trials/11.02:_The_Binomial_Distribution . Read distribution, moments and sampling without replacement subsections. Existing key `siegrist2022_binomial_distribution`.
- Dodge, *Concise Encyclopedia of Statistics* (2008), “Bernoulli Distribution” pp. 36–37 and “Bernoulli, Jakob” p. 37. Authorized user PDF, `/workspace/statwiki-sources/dodge2008/pages/pdf-0043.txt` and `pdf-0044.txt`. Existing key `dodge2008`.
- Question bank `ex-sp-bernoulli-pairs` and `ex-sp-proportion-bound`: both have worked answers and exercise respectively independence versus identical Bernoulli margins and Bernoulli sample-proportion variance. They differ from the page's worked example.

## Fact audit

- **Checked**: PMF, CDF, mean, variance, variance maximum at $p=1/2$, generating function, and uniform simulation: Siegrist §11.1, Basic Theory.
- **Checked**: independent common-$p$ Bernoulli sums are binomial, with mean $np$ and variance $np(1-p)$: Siegrist §11.2, Distribution Functions and Moments.
- **Checked**: sampling without replacement creates dependent indicators and hypergeometric counts: Siegrist §11.2, finite-population sampling.
- **Checked**: Jakob Bernoulli's *Ars Conjectandi* appeared posthumously in 1713: Dodge p. 37. We do not claim the modern PMF notation appears in that book.
- **Checked**: all new numeric examples by exact arithmetic in `checks/bernoulli-distribution.py`.
- **Assumed**: “success” is an analyst-chosen binary event; repeated-trial calculations require independence and a common $p$.
- **Disputed/limited**: a Bernoulli model for a dichotomized continuous response loses magnitude; Bernoulli margins alone do not identify dependence.
