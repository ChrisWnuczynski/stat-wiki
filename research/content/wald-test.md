## Lead context
A Wald test compares an estimate with a hypothesised value by dividing the difference by the estimate’s standard error.

## Motivating example
Suppose $\hat\beta=0.8$ and $\mathrm{se}(\hat\beta)=0.25$, and the null value is $0$. Then

$$
Z=0.8/0.25=3.2.
$$

The two-sided standard-normal $p$-value is $2\{1-\Phi(3.2)\}=0.0014$ to four decimals. Because $3.2>1.960$, the level $0.05$ test rejects. The $p$-value uses the normal approximation. It is not an exact tail probability for a finite sample.

## Intuition — How many standard errors from the null
If an estimator is approximately normal, centred at the true value, then the standardised difference between the estimate and a null value is approximately standard normal. The Wald statistic is that ratio, using a standard error computed at the fitted model. A large absolute value is evidence against the null because the estimate sits many estimated standard errors away from it. The approximation is a large-sample statement. It is not an exact finite-sample law.{{cite:hastie_esl2009}} (Ch. 4, §4.4.2, p. 122; §4.4.3, p. 125)

## Definition — Estimate over standard error
For a scalar coefficient estimate $\hat\beta$ with standard error $\mathrm{se}(\hat\beta)$, the Wald statistic for $H_0:\beta=\beta_0$ is

$$
Z=\frac{\hat\beta-\beta_0}{\mathrm{se}(\hat\beta)}.
$$

In a logistic regression this is the coefficient divided by its standard error when $\beta_0=0$, and Hastie, Tibshirani and Friedman call that ratio a $Z$ score and a Wald test of the hypothesis that the coefficient is zero while the other coefficients stay in the model.{{cite:hastie_esl2009}} (Ch. 4, §4.4.2, p. 122) A two-sided level $0.05$ comparison with the standard normal uses the quantile $z_{0.975}=1.960$: reject when $|Z|\ge 1.960$. Their remark that a $Z$ score larger than about $2$ is significant at $5\%$ is that quantile, rounded.{{cite:hastie_esl2009}} (p. 122)

## Worked example — A coefficient and its standard error

**Your turn.** An estimate is $1.2$ and its standard error is $0.4$. Give the Wald statistic for a zero null, and the two-sided normal $p$-value to four decimals.

::: {.callout-tip collapse="true" title="Answer"}
$Z=1.2/0.4=3$. The $p$-value is $2\{1-\Phi(3)\}=0.0027$. The test rejects at level $0.05$, because $3>1.960$.
:::

The normal limit itself, $\hat\beta$ approximately $\mathrm{N}(\beta,(X^\top WX)^{-1})$ for a logistic fit, is the large-sample result used to justify the standard error.{{cite:hastie_esl2009}} (Ch. 4, §4.4.3, p. 125) Under complete separation a logistic coefficient diverges and the printed standard error does not support this ratio.

## Connections — Intervals, likelihood ratios and scores
The [Wald interval](wald-interval.qmd) inverts the same ratio: the values $\beta_0$ that are not rejected are $\hat\beta\pm z\,\mathrm{se}(\hat\beta)$. [Maximum likelihood](maximum-likelihood.qmd) supplies $\hat\beta$ in a regular model, and the [standard error](standard-error.qmd) is the square root of an estimated variance. A likelihood-ratio test compares two maximised log-likelihoods and refits the smaller model. A Wald test does not. ESL notes that the Wald test of a coefficient, and the Rao score test of an omitted term, can both be read off the weighted least-squares fit at the current maximum.{{cite:hastie_esl2009}} (p. 125)
