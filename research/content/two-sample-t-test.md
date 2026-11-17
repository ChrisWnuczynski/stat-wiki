## Motivating example
A comparison of two sample means needs both a contrast and an estimate of its sampling variability. A difference of three units can be precise in a large stable experiment or uninformative in a small noisy one. A two-sample t procedure standardises the difference using the design and the within-group variation. Its reference distribution depends on whether a common population variance is assumed.{{cite:nist_two_sample_t2002}} (§1.3.5.3)

## Definition — State the target contrast before selecting a tail
Write $\Delta=\mu_1-\mu_2$ and specify a null value $\Delta_0$. The alternatives $\Delta>\Delta_0$, $\Delta<\Delta_0$ and $\Delta\ne\Delta_0$ require upper, lower and two-sided tail calculations. A one-sided alternative must follow the scientific question rather than the observed sign. The null value can be a nonzero practical threshold, so equality of the two means is only one application.{{cite:nist_two_sample_t2002}} (§1.3.5.3, purpose, null difference and critical region)

## Properties — The denominator distinguishes pooled and Welch tests
For independent samples, Welch's statistic divides $\bar X_1-\bar X_2-\Delta_0$ by $\sqrt{S_1^2/n_1+S_2^2/n_2}$. Its approximate degrees of freedom are
$$\nu_W=\frac{(S_1^2/n_1+S_2^2/n_2)^2}{(S_1^2/n_1)^2/(n_1-1)+(S_2^2/n_2)^2/(n_2-1)}.$$
The pooled statistic uses the common-variance estimate and has an exact Student law for independent normal samples with equal population variances. Welch permits unequal population variances, with an approximate Student calibration. These are different assumptions about sampling variation, rather than two labels for the same degrees of freedom.{{cite:nist_two_sample_t2002}} (§1.3.5.3)

Under normality, the pooled law follows by dividing an independent standard normal contrast by the square root of an independent scaled chi-square residual sum. This is why the equal-variance pivot has $n_1+n_2-2$ degrees of freedom. If the observations are paired, the covariance between measurements changes the standard error, and the appropriate elementary analysis uses within-pair differences.{{cite:siegrist2022_normals}} (§6.8, “The Two Sample Model”)

## Interpretation — A p-value does not measure an effect's size
For a two-sided test, the p-value is twice the relevant Student upper tail at the absolute observed statistic. A small p-value indicates that the contrast is large relative to the standard error under the null model. The confidence interval gives the corresponding range of contrast values that the same two-sided procedure does not reject. Changing sample size can change the p-value substantially while leaving a scientifically relevant mean difference unchanged.{{cite:nist_two_sample_t2002}} (§1.3.5.3, critical regions)

## Worked example — A pooled comparison with a threshold
Take independent normal samples with common variance, $n_1=6,n_2=10$, means $12,9$, and sample variances $4,9$. The pooled variance is $101/14$ and the standard error of the difference is $\sqrt{202/105}\approx1.387015$. At $\Delta_0=0$ the statistic is approximately $2.162919$ on fourteen degrees of freedom. Testing a practical threshold of one instead gives $1.441946$ on the same reference law. The contrast has not changed; the null claim has.

The caffeine example uses the actual two observed groups to illustrate pooled and Welch calculations. Its unequal sample variances produce different reference degrees of freedom even though the group sizes match. Equal group sizes make the two estimated standard errors coincide, but they do not make the reference distributions identical.

**Your turn.** With the same estimated standard error, what is the statistic at a null difference of three?

::: {.callout-tip collapse="true" title="Answer"}
The observed difference is three, so the centred numerator is zero and the statistic is zero.
:::

## Assumptions and limits — Design and distribution both matter
Independent observations within each sample and independent groups are separate requirements. Clustered, serial or matched data need the corresponding covariance accounted for. Normality gives finite-sample t calibration; for nonnormal populations large-sample approximations depend on moment and sample-size conditions. Severe skewness, influential outliers or a very small group can make those approximations unreliable. The ordinary WMW rank-sum null addresses a different comparison and cannot be chosen merely by replacing the word *mean* with *median*.{{cite:fay_proschan2010}} (§§5.1–5.3, pp. 10–25)
