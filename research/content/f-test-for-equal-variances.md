## Motivating example

Two production processes can have similar mean output but different variability. Comparing their sample variances addresses that difference directly. The classical F test obtains an exact reference distribution when the two samples are independent and each population is normal.{{cite:siegrist2022_normals}} (§6.8, “The Two Sample Model”)

## Definition — The variance-ratio pivot

For independent normal samples of sizes $n_1,n_2\ge2$, put $\nu_i=n_i-1$ and use sample variances with denominator $\nu_i$. Then
$$\frac{S_1^2/\sigma_1^2}{S_2^2/\sigma_2^2}\sim F_{\nu_1,\nu_2}.$$
Under $H_0:\sigma_1^2=\sigma_2^2$, the observed ratio is compared with this F distribution. Its numerator and denominator degrees of freedom follow the order of the two sample variances.{{cite:siegrist2022_normals}} (§6.8, “Ratios of Sample Variances”)

The pivot follows because $\nu_iS_i^2/\sigma_i^2$ are independent chi-square variables with $\nu_i$ degrees of freedom. Dividing each chi-square variable by its own degrees of freedom gives the F ratio. The construction requires more than unbiased sample variances: it requires their normal-sample chi-square distributions.{{cite:dodge2008}} (p.205)

## Properties — Two tails and a confidence interval

Let $q_p$ denote the lower-tail $p$ quantile of $F_{\nu_1,\nu_2}$. A two-sided level-$\alpha$ test rejects for a ratio below $q_{\alpha/2}$ or above $q_{1-\alpha/2}$. Inverting the same pivot gives a confidence interval for the population variance ratio:
$$\left[\frac{S_1^2/S_2^2}{q_{1-\alpha/2}},
\frac{S_1^2/S_2^2}{q_{\alpha/2}}\right].$$
Reciprocating the observed ratio requires swapping the degrees of freedom; it is not sufficient to invert the statistic while leaving the reference distribution unchanged.{{cite:siegrist2022_normals}} (§6.8, “Ratios of Sample Variances”)

## Worked example

For $n_1=15,n_2=10$ and sample standard deviations $15,12$, the ratio is $225/144=1.5625$. With degrees of freedom $(14,9)$, the lower and upper $2.5\%$ critical values are $0.311594$ and $3.797952$. The ratio lies between them. The equal-tail two-sided p-value is approximately $0.506589$, and the $95\%$ interval for $\sigma_1^2/\sigma_2^2$ is $(0.411406,5.014532)$. The wide interval permits substantial variation in either direction; failure to reject equality does not establish equality.{{cite:siegrist2022_normals}} (§6.8, “Ratios of Sample Variances”)

**Your turn.** If the two samples in the worked example are exchanged, what statistic and degrees of freedom must be used?

::: {.callout-tip collapse="true" title="Answer"}
The ratio becomes $144/225=0.64$, with numerator and denominator degrees of freedom $(9,14)$. The reciprocal transformation gives the same two-sided decision.
:::

## Assumptions and limits

The exact F calibration is a normal-population result. For a general population, unbiasedness of $S^2$ remains valid with finite variance, but its sampling distribution need not be a scaled chi-square. Outliers or heavy tails can change the behaviour of the ratio. Independence between the samples is also necessary for the independent chi-square construction.{{cite:siegrist2022_normals}} (§6.8, “The Sample Variance”; “Ratios of Sample Variances”)


## Check yourself

### [Checking equal variances](../questions/ex-inf-variance-ratio-interval.qmd) {#self-check-ex-inf-variance-ratio-interval}

::: {.callout-tip collapse="true" title="Answer"}
For two independent normal samples of size fifty with standard deviations $14.1$ and $14.3$, the observed ratio is about $0.97222$. Using the supplied critical value $1.762$ gives the interval $(0.55177,1.71306)$ approximately. It contains one, indicating compatibility with equality at that confidence level, rather than proving it.
:::

### [Expectation of sample variance](../questions/ex-inf-expected-sample-variance.qmd) {#self-check-ex-inf-expected-sample-variance}

::: {.callout-tip collapse="true" title="Answer"}
Expand about the population mean to obtain $\sum(X_i-\bar X)^2=\sum(X_i-\mu)^2-n(\bar X-\mu)^2$. Expectations give $n\sigma^2-\sigma^2=(n-1)\sigma^2$, hence the sample variance with divisor $n-1$ is unbiased.
:::
