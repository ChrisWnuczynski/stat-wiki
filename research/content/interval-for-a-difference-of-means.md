## Motivating example
Comparing before-and-after averages requires uncertainty for their difference, rather than two separate intervals inspected for overlap. For the safety example, a negative difference means fewer lost working hours after the change. Whether that association estimates an effect of the safety measures depends on the design and on other changes over time. The two-sample formula addresses sampling variation under independence.{{cite:openintro2019}} (§7.3.1, confidence interval for a difference of means)

## Definition
The pooled interval is exact for independent normal samples with a common positive population variance and sizes at least two. The means may differ. Equality of variances is a modelling assumption; a nonsignificant variance test alone provides little assurance in small samples. If a common variance lacks substantive support, a Welch interval estimates the standard error as $\sqrt{s_1^2/n_1+s_2^2/n_2}$ and uses approximate degrees of freedom.{{cite:openintro2019}} (§7.3, “Pooled standard deviation estimate”)

## Properties — From independent pieces to a pivot
Let $\nu=n_1+n_2-2$. Under the common-variance normal model, the standardized mean difference
$$Z=\frac{(\overline X_1-\overline X_2)-(\mu_1-\mu_2)}{\sigma\sqrt{1/n_1+1/n_2}}$$
is standard normal. The residual sums of squares from the two samples are independent, with total $V=\nu S_p^2/\sigma^2\sim\chi^2_\nu$. Orthogonality of each sample mean to its residuals gives independence of $Z$ and $V$. Thus $Z/\sqrt{V/\nu}$ is $t_\nu$. Rearranging $|T|\le t_{\nu,1-\alpha/2}$ yields the pooled interval and preserves its coverage event. The pooled formula and degrees of freedom use information from both samples.{{cite:nist_handbook2002}} (§1.3.5.3, equal-variance two-sample statistic)

## Worked example — Unequal sample sizes
Construct two independent normal samples with summaries $n_1=10$, $\bar x_1=12$, $s_1=2$ and $n_2=15$, $\bar x_2=9$, $s_2=3$. Under the common-variance assumption,
$$s_p^2=\frac{9(4)+14(9)}{23}=\frac{162}{23},\qquad SE=\sqrt{\frac{162}{23}\left(\frac1{10}+\frac1{15}\right)}=1.0835.$$
Using $t_{23,0.975}=2.0687$ gives $3\pm2.2413$, or $(0.7587,5.2413)$. The positive interval estimates the direction and magnitude of the mean difference, conditional on the model. Each variance is weighted by residual degrees of freedom, rather than by its sample size alone.{{cite:openintro2019}} (§7.3, “Pooled standard deviation estimate”)

**Your turn.** If both sample sizes are 10, both sample standard deviations are 2, and the mean difference is 1, find the pooled standard error. Does the 95% pooled interval include zero?

::: {.callout-tip collapse="true" title="Answer"}
Here $s_p=2$ and $SE=2\sqrt{1/10+1/10}=0.8944$. The multiplier is $t_{18,0.975}=2.1009$, giving $1\pm1.8791=(-0.8791,2.8791)$, which includes zero.
:::

## Interpretation — The safety summaries
The two reported standard deviations give $s_p^2=(14.1^2+14.3^2)/2=201.65$, so the unrounded standard error is $2.8401$ hours. The 95% interval is approximately $(-22.64,-11.36)$. These summaries support a reduction in mean hours under the independent-samples model. Consecutive months can be correlated, and before-and-after periods can differ in workforce or workload, so the interval's narrowness cannot settle those design questions.{{cite:openintro2019}} (§7.3.1, independence conditions)

### When Welch changes the calculation
For independent normal samples with different variances, the mean difference remains normal, but dividing by its estimated standard error no longer produces an exact ordinary $t$ pivot. Welch's approximation uses
$$\nu_W=\frac{(s_1^2/n_1+s_2^2/n_2)^2}{(s_1^2/n_1)^2/(n_1-1)+(s_2^2/n_2)^2/(n_2-1)}.$$
The resulting interval is the estimated mean difference plus or minus $t_{\nu_W,1-\alpha/2}\sqrt{s_1^2/n_1+s_2^2/n_2}$. The degrees of freedom may be noninteger. Unlike a preliminary variance test followed by a selected interval, this approach uses one prespecified rule for unequal variances. For balanced sample sizes the pooled and unpooled standard errors coincide algebraically, but their reference degrees of freedom can differ.{{cite:nist_handbook2002}} (§1.3.5.3, Welch–Satterthwaite formula)

## Common misconceptions
Pairing is a property of the design. If the same units are measured twice, analyze their differences and use the variation of those differences; pretending the samples are independent discards the covariance term. Conversely, equal sample sizes do not create pairing. A confidence interval for a population mean difference also differs from a prediction interval for the difference between two future individual measurements.{{cite:nist_handbook2002}} (§1.3.5.3, paired and unpaired data)

## Lead context
An interval for a difference of means compares two normal samples.

With equal variances the pooled variance uses both samples, and the standard error of $\bar x_1-\bar x_2$ is $s_p\sqrt{1/n_1+1/n_2}$. The critical value comes from a $t$ distribution whose degrees of freedom are $n_1+n_2-2$. The resulting interval is for the difference of population means. It is not a pair of intervals for the two means, and overlap of those two intervals is a different event.{{cite:openintro2019}} (§7.3.1, confidence interval for a difference of means)

## Intuition
For $n_1=10$, $\bar x_1=12$, $s_1=2$ and $n_2=15$, $\bar x_2=9$, $s_2=3$, the pooled variance is $162/23$ and the standard error is about $1.0835$. The $0.975$ quantile of $t_{23}$ is about $2.0687$, the margin is about $2.2413$, and the $95\%$ interval is about $(0.7587,5.2413)$. Both endpoints are positive, so zero is outside the interval. A second pair of samples with $n_1=n_2=10$, both standard deviations $2$, and a difference of sample means equal to $1$ has standard error about $0.8944$. The $t_{18}$ quantile is about $2.1009$, the margin is about $1.8791$, and the interval is about $(-0.8791,2.8791)$, which contains zero.{{cite:openintro2019}} (§7.3, “Pooled standard deviation estimate”)

## Statistical use
Separate $95\%$ intervals can overlap while the interval for the difference excludes zero. If two sample means are $0$ and $3$ and each has known standard error $1$, the separate intervals are about $[-1.96,1.96]$ and $[1.04,4.96]$. They overlap. The standard error of the difference is $\sqrt{2}\approx 1.4142$, and the interval for the difference is about $[0.228,5.772]$, which excludes zero. The overlap rule is answering whether each mean's interval meets the other. The difference interval is answering whether zero is plausible for $\mu_1-\mu_2$. With estimated variances the numerical endpoints move, and the logical gap between the two questions remains.{{cite:openintro2019}} (§7.3.1, confidence interval for a difference of means){{cite:nist_handbook2002}} (§1.3.5.3, equal-variance two-sample statistic)

## Connections
A pooled interval assumes a common variance. If the sample variances are far apart and the sample sizes differ, the pooled standard error can misstate the uncertainty; a Welch interval uses a different standard error and a different degrees-of-freedom approximation. The interval is also not a prediction interval for the difference of two new observations. A prediction interval has to include the noise of those two observations, so it is wider than the interval for the difference of means. Finally, the coverage is a property of the procedure under the normal equal-variance model. One computed interval either contains the difference or it does not. The probability $0.95$ refers to the method, repeated on new samples.{{cite:nist_handbook2002}} (§1.3.5.3, Welch–Satterthwaite formula){{cite:openintro2019}} (§7.3.1, independence conditions)
