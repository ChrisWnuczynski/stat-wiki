## Motivating example
Two independent groups may have different mean measurements but share a common population variance. Their mean difference has a normal sampling law under normal sampling, yet its scale contains that unknown variance. Pooling the within-group sums of squares estimates the scale without using the between-group difference. Dividing the centred difference by this independent estimate produces an exact Student pivot.{{cite:nist_two_sample_t2002}} (§1.3.5.3, equal-variance test statistic)

## Statement
Assume each sample is iid normal, the samples are independent, their common variance is positive, and both sample sizes exceed one. With $\nu=n_1+n_2-2$, define the Bessel-corrected sample variances and their pooled estimate $S_p^2$. Then
$$T=\frac{\bar X_1-\bar X_2-(\mu_1-\mu_2)}{S_p\sqrt{1/n_1+1/n_2}}\sim t_\nu.$$
A pivot has a distribution free of the unknown model parameters. Here $T$ contains the unknown mean contrast in its definition, but its reference distribution contains neither that contrast nor the variance. Evaluating it at a proposed contrast gives a test statistic; inverting its quantiles gives a confidence interval.{{cite:siegrist2022_normals}} (§6.8, “The Two Sample Model”)

## Intuition — Two fitted means spend two degrees of freedom
A within-group sum of squares removes one fitted mean in each group. Thus the two residual sums contribute $n_1-1$ and $n_2-1$ independent normal directions. Pooling adds those counts. The weight on each sample variance is its residual degrees of freedom, rather than its group size alone. An unweighted average is equivalent only when the sample sizes are equal.{{cite:nist_two_sample_t2002}} (§1.3.5.3, pooled-variance formula)

## Proof
Within each normal sample, the sample mean is independent of the sample variance, and $(n_j-1)S_j^2/\sigma^2$ is chi-squared with $n_j-1$ degrees of freedom. Independence between samples makes their sum $U=\nu S_p^2/\sigma^2$ chi-squared with $\nu$ degrees of freedom. The normal variable $Z=[\bar X_1-\bar X_2-(\mu_1-\mu_2)]/[\sigma\sqrt{1/n_1+1/n_2}]$ is standard normal and independent of both residual sums. Consequently $Z/\sqrt{U/\nu}$ has the Student distribution in the statement. The normal-sample independence is the ingredient that turns a standard-error formula into an exact finite-sample law.{{cite:siegrist2022_normals}} (§6.8, normal sample mean/variance and “The Two Sample Model”)

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

To see the inversion explicitly, let $c$ be the upper $1-\alpha/2$ quantile of $t_\nu$. The event $-c\le T\le c$ has probability $1-\alpha$ under the model. Multiplying by the positive estimated standard error and rearranging produces an interval centred at $\bar X_1-\bar X_2$, with half-width $cS_p\sqrt{1/n_1+1/n_2}$. The unknown contrast appears inside the event being covered; the random endpoints depend only on the observations. This is why a confidence procedure can be constructed from a pivot even though evaluating the pivot requires a proposed parameter value. Its exactness concerns repeated sampling under the stated normal common-variance model.{{cite:siegrist2022_normals}} (§6.8, “The Two Sample Model”)
