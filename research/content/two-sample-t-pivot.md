## Motivating example
Two independent groups may have different mean measurements but share a common population variance. Their mean difference has a normal sampling law under normal sampling, yet its scale contains that unknown variance. Pooling the within-group sums of squares estimates the scale without using the between-group difference. Dividing the centred difference by this independent estimate produces an exact Student pivot.{{cite:nist_two_sample_t2002}} (§1.3.5.3, equal-variance test statistic)

## Statement
Assume each sample is iid normal, the samples are independent, their common variance is positive, and both sample sizes exceed one. With $\nu=n_1+n_2-2$, define the Bessel-corrected sample variances and their pooled estimate $S_p^2$. Then
$$T=\frac{\bar X_1-\bar X_2-(\mu_1-\mu_2)}{S_p\sqrt{1/n_1+1/n_2}}\sim t_\nu.$$
A pivot has a distribution free of the unknown model parameters. Here $T$ contains the unknown mean contrast in its definition, but its reference distribution contains neither that contrast nor the variance. Evaluating it at a proposed contrast gives a test statistic; inverting its quantiles gives a confidence interval.

## Intuition — Two fitted means spend two degrees of freedom
A within-group sum of squares removes one fitted mean in each group. Thus the two residual sums contribute $n_1-1$ and $n_2-1$ independent normal directions. Pooling adds those counts. The weight on each sample variance is its residual degrees of freedom, rather than its group size alone. An unweighted average agrees with the pooled estimate for every pair of sample variances only when the sample sizes are equal, though at unequal sample sizes both still equal the shared observed value when the sample variances tie, and such a tie does not imply equal population variances.{{cite:nist_two_sample_t2002}} (§1.3.5.3, pooled-variance formula)

## Proof
Within each normal sample, the sample mean is independent of the sample variance, and $(n_j-1)S_j^2/\sigma^2$ is chi-squared with $n_j-1$ degrees of freedom. Independence between samples makes their sum $U=\nu S_p^2/\sigma^2$ chi-squared with $\nu$ degrees of freedom. The normal variable $Z=[\bar X_1-\bar X_2-(\mu_1-\mu_2)]/[\sigma\sqrt{1/n_1+1/n_2}]$ is standard normal and independent of both residual sums. Consequently $Z/\sqrt{U/\nu}$ has the Student distribution in the statement. The normal-sample independence is the ingredient that turns a standard-error formula into an exact finite-sample law.

## Worked example
### Unequal sample sizes with a common scale
Suppose $n_1=6,n_2=10$, group means are $12$ and $9$, and sample variances are $4$ and $9$. The pooled variance is $(5\times4+9\times9)/14=101/14\approx7.214286$. The estimated variance of the mean difference is $(101/14)(1/6+1/10)=202/105\approx1.923810$, giving standard error $1.387015$. At a hypothesised difference of zero the statistic is $3/1.387015\approx2.162919$, with fourteen degrees of freedom. The reference law is exact under the common-variance normal model, regardless of the unequal sample sizes.

**Your turn.** Keep those samples but test a difference of one. What changes?

::: {.callout-tip collapse="true" title="Answer"}
The numerator becomes $3-1=2$. The pooled variance and degrees of freedom stay the same, giving $T\approx1.441946$.
:::

## Generalizations — Separate variances lead to a different calibration
When population variances differ, the variance of the difference is $\sigma_1^2/n_1+\sigma_2^2/n_2$. A common pooled estimate does not generally estimate that expression correctly. Welch's statistic substitutes the two sample variances separately and uses an approximate degrees-of-freedom calculation. Equal observed sample variances do not prove equal population variances, and a preliminary variance test is not part of the derivation of this pivot.{{cite:nist_two_sample_t2002}} (§1.3.5.3, Welch–Satterthwaite formulation)

## Statistical use — Distinguish a paired contrast
If measurements are matched within people, independence of the two group means is usually inappropriate. The variance of their difference includes a covariance term. A paired analysis forms differences within people and applies a one-sample procedure to them. The pooled two-sample pivot applies when the sampling design supplies separate independent samples.{{cite:nist_two_sample_t2002}} (§1.3.5.3, paired and unpaired samples)

To see the inversion explicitly, let $c$ be the upper $1-\alpha/2$ quantile of $t_\nu$. The event $-c\le T\le c$ has probability $1-\alpha$ under the model. Multiplying by the positive estimated standard error and rearranging produces an interval centred at $\bar X_1-\bar X_2$, with half-width $cS_p\sqrt{1/n_1+1/n_2}$. The unknown contrast appears inside the event being covered; the random endpoints depend only on the observations. This is why a confidence procedure can be constructed from a pivot even though evaluating the pivot requires a proposed parameter value. Its exactness concerns repeated sampling under the stated normal common-variance model.

## Key results — Degrees of freedom add the two residual counts
Independent normal samples of sizes $8$ and $12$ have residual counts $7$ and $11$. The pooled pivot uses $8+12-2=18$ degrees of freedom. Equal sample sizes are not required for the addition: the worked samples of sizes $6$ and $10$ use $5+9=14$. The pooled variance weights the sample variances by those residual counts, $(5\times4+9\times9)/14=101/14\approx7.214286$. An unweighted average of $4$ and $9$ would be $6.5$, which overweights the smaller sample. The estimated variance of the mean difference is $202/105\approx1.923810$, and the standard error is $1.387015$. At a hypothesised difference of zero the statistic is $2.162919$. At a hypothesised difference of one it is $1.441946$. Only the numerator changes.{{cite:nist_two_sample_t2002}} (§1.3.5.3, pooled-variance formula)

If the common variance is known, the denominator uses that known standard deviation instead of $S_p$. The ratio is then standard normal, and the degrees of freedom disappear because no variance was estimated. The normal reference is narrower than the Student reference with $18$ degrees of freedom. For a numerical comparison that does estimate the variance, take an estimated standard error $2\sqrt{0.2}\approx0.894427$. The $0.975$ quantile of $t_{18}$ is $2.100922$, which equals $2.101$ to three decimals, and the half-width is $1.879122$. Around an estimated difference of $3$, the endpoints round to $(1.12,4.88)$. That interval uses an estimated scale. The known-variance interval at the same estimated standard error would replace $2.100922$ by a standard normal quantile.{{cite:nist_two_sample_t2002}} (§1.3.5.3, equal-variance test statistic)

### Statistical use — The pivot is evaluated at a proposed contrast
The random variable $T$ contains $\mu_1-\mu_2$. Substituting a candidate value $\Delta_0$ produces a number that can be compared with $t_\nu$. The interval collects the candidates that survive. For the worked standard error $1.387015$ and a critical value, the half-width is that critical value times $1.387015$. Shifting the null from $0$ to $1$ does not change the interval; it changes which point inside the interval is treated as the test's null. A one-sided test uses one tail of the same pivot and inverts to a one-sided bound. The two-sided interval $(1.12,4.88)$ in the eighteen-degree illustration is a different sample from the fourteen-degree worked example. The two calculations should not be spliced into one reported interval.{{cite:nist_two_sample_t2002}} (§1.3.5.3, equal-variance test statistic)

## Related concepts
The [two-sample $t$ test](two-sample-t-test.qmd) chooses a tail and a variance assumption for this pivot. Welch's statistic keeps the normal numerator and replaces the pooled scale by $S_1^2/n_1+S_2^2/n_2$, then approximates the degrees of freedom. The approximation is not the exact $t_\nu$ law proved here. A paired sample folds the covariance into within-pair differences and returns to a one-sample pivot, because the two group means are no longer independent.{{cite:nist_two_sample_t2002}} (§1.3.5.3, Welch–Satterthwaite formulation)
