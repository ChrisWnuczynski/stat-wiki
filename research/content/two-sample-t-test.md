## Motivating example
A comparison of two sample means needs both a contrast and an estimate of its sampling variability. A difference of three units can be precise in a large stable experiment or uninformative in a small noisy one. A two-sample t procedure standardises the difference using the design and the within-group variation. Its reference distribution depends on whether a common population variance is assumed.{{cite:nist_two_sample_t2002}} (§1.3.5.3)

## Definition — State the target contrast before selecting a tail
Write $\Delta=\mu_1-\mu_2$ and specify a null value $\Delta_0$. The alternatives $\Delta>\Delta_0$, $\Delta<\Delta_0$ and $\Delta\ne\Delta_0$ require upper, lower and two-sided tail calculations. A one-sided alternative must follow the scientific question rather than the observed sign. The null value can be a nonzero practical threshold, so equality of the two means is only one application.{{cite:nist_two_sample_t2002}} (§1.3.5.3, purpose, null difference and critical region)

## Properties — The denominator distinguishes pooled and Welch tests
For independent samples, Welch's statistic divides $\bar X_1-\bar X_2-\Delta_0$ by $\sqrt{S_1^2/n_1+S_2^2/n_2}$. Its approximate degrees of freedom are
$$\nu_W=\frac{(S_1^2/n_1+S_2^2/n_2)^2}{(S_1^2/n_1)^2/(n_1-1)+(S_2^2/n_2)^2/(n_2-1)}.$$
The pooled statistic uses the common-variance estimate and has an exact Student law for independent normal samples with equal population variances. Welch permits unequal population variances, with an approximate Student calibration. These are different assumptions about sampling variation, rather than two labels for the same degrees of freedom.{{cite:nist_two_sample_t2002}} (§1.3.5.3)

Under normality, the pooled law follows by dividing an independent standard normal contrast by the square root of an independent scaled chi-square residual sum. This is why the equal-variance pivot has $n_1+n_2-2$ degrees of freedom. If the observations are paired, the covariance between measurements changes the standard error, and the appropriate elementary analysis uses within-pair differences.

## Interpretation — A p-value does not measure an effect's size
For a two-sided test, the p-value is twice the relevant Student upper tail at the absolute observed statistic. A small p-value indicates that the contrast is large relative to the standard error under the null model. The confidence interval gives the corresponding range of contrast values that the same two-sided procedure does not reject. Changing sample size can change the p-value substantially while leaving a scientifically relevant mean difference unchanged.{{cite:nist_two_sample_t2002}} (§1.3.5.3, critical regions)

## Worked example — A pooled comparison with a threshold
Take independent normal samples with common variance, $n_1=6,n_2=10$, means $12,9$, and sample variances $4,9$. The pooled variance is $101/14$ and the standard error of the difference is $\sqrt{202/105}\approx1.387015$. At $\Delta_0=0$ the statistic is approximately $2.162919$ on fourteen degrees of freedom. Testing a practical threshold of one instead gives $1.441946$ on the same reference law. The contrast has not changed; the null claim has.

The caffeine example uses the actual two observed groups to illustrate pooled and Welch calculations. Its unequal sample variances produce different reference degrees of freedom even though the group sizes match. Equal group sizes make the two estimated standard errors coincide, but they do not make the reference distributions identical.

**Your turn.** Using the same pooled standard error, what is the statistic when the null difference is $0.5$, and what is its two-sided tail probability on fourteen degrees of freedom?

::: {.callout-tip collapse="true" title="Answer"}
The numerator is $3-0.5=2.5$. Dividing by $\sqrt{202/105}$ gives $1.802432$. The two-sided tail probability on fourteen degrees of freedom is $0.093041$.
:::

## Common misconceptions — Equal sample sizes do not equate the two reference laws
When both groups have size $n$, the Welch variance estimate is $(S_1^2+S_2^2)/n$ and the pooled variance is $(S_1^2+S_2^2)/2$, so the two standard errors agree. The reference degrees of freedom still differ. Take $n_1=n_2=10$, sample variances $4$ and $16$, and an observed mean difference of $2$. Both standard errors equal $\sqrt{2}\approx1.414214$, and both statistics equal $1.414214$. The pooled upper-tail probability on $18$ degrees of freedom is $0.087182$. Welch's formula gives approximately $13.235294$ degrees of freedom and upper-tail probability $0.090195$. Matching estimates of the contrast can still be calibrated differently.{{cite:nist_two_sample_t2002}} (§1.3.5.3)

For the samples with variances $4$ and $9$, the groups have different sizes, so the standard errors separate as well. Welch's standard error is $\sqrt{4/6+9/10}=1.251666$. The statistic at a zero null difference is $2.396806$ on approximately $13.720497$ degrees of freedom, and the two-sided tail probability is $0.031380$. The pooled calculation uses $1.387015$ and fourteen degrees of freedom. The larger sample carries the larger variance, so pooling spreads that variance into the smaller group's contribution and widens the estimated standard error.{{cite:nist_two_sample_t2002}} (§1.3.5.3, Welch–Satterthwaite formulation)

### Worked example — One-sided comparison of two recorded groups
One recorded group is $17,22,21,16,6,-2,27,15,16,20$ and the other is $4,10,7,-9,5,4,5,7,6,12$. The means are $15.8$ and $5.1$, a difference of $10.7$. The sample variances are $69.288889$ and $31.211111$. Equal group sizes make the pooled and Welch statistics agree at $3.3752$. Welch's approximate degrees of freedom are $15.74$, and the one-sided probability in the greater direction is $0.001966$. The pooled statistic uses $18$ degrees of freedom and one-sided probability $0.001686$. An approximate $95\%$ interval that uses the Welch reference and the common standard error runs from $4.0$ to $17.4$ after each endpoint is rounded to one decimal place. The interval remains wide because each group has ten observations and substantial within-group scatter.{{cite:nist_two_sample_t2002}} (§1.3.5.3, critical regions)

## Statistical use — Report the contrast, the standard error and the reference
A comparison states the estimated difference, the standard error, the degrees of freedom and whether the variance was pooled. Those pieces support both a test at a chosen null value and the interval obtained by inverting that test. For the first numerical sample the pooled standard error is $1.387015$. The two-sided $95\%$ Student critical value on fourteen degrees of freedom is $2.144787$, the half-width is $2.974850$, and the interval is $(0.025150, 5.974850)$. Every contrast inside the interval is retained by the two-sided $5\%$ pooled procedure. The point estimate $3$ is the centre of that interval, not a substitute for it.{{cite:nist_two_sample_t2002}} (§1.3.5.3)

The Student ratio compares a normal contrast with an independent estimate of its scale. The pooled two-sample statistic is that ratio for a difference of means, with the scale estimated from both within-group residual sums. Inverting the ratio produces an interval for the contrast. Squaring the ratio produces an equivalent one-degree-of-freedom comparison when the same residual variance is used.{{cite:dodge2008}} (p. 526, Student ratio construction)

## Connections
The [two-sample $t$ pivot](two-sample-t-pivot.qmd) isolates the exact Student law under a shared variance. A paired design replaces the two-sample standard error by the standard error of within-pair differences, because the two measurements on one person share a covariance. A rank procedure answers a different null. It is selected for that null, and the ordinary mean comparison remains the procedure whose statistic was derived above.{{cite:fay_proschan2010}} (§§5.1–5.3, pp. 10–25){{cite:nist_two_sample_t2002}} (§1.3.5.3, paired and unpaired samples)

## Assumptions and limits — Design and distribution both matter
Independent observations within each sample and independent groups are separate requirements. Clustered, serial or matched data need the corresponding covariance accounted for. Normality gives finite-sample t calibration; for nonnormal populations large-sample approximations depend on moment and sample-size conditions. Severe skewness, influential outliers or a very small group can make those approximations unreliable. The ordinary WMW rank-sum null addresses a different comparison and cannot be chosen merely by replacing the word *mean* with *median*.{{cite:fay_proschan2010}} (§§5.1–5.3, pp. 10–25)
