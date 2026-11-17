## Motivating example
Two independent samples can differ in spread as well as mean. A confidence interval for their population mean difference should allow each sample to estimate its own variance. The unpooled standard error does this directly, without requiring an equality-of-variances assumption.{{cite:cetinkaya_hardin2024}} (§20.4)

## Definition — An interval with an estimated variance and effective degrees of freedom
Let $\overline X,\overline Y$ be independent sample means with sample sizes at least two, with sample variances $S_X^2,S_Y^2$ computed using divisors $n_X-1,n_Y-1$. Put $a=S_X^2/n_X$ and $b=S_Y^2/n_Y$, with $a+b>0$. The Welch interval for $\delta=\mu_X-\mu_Y$ is
$$
\overline X-\overline Y\ \pm\ t_{\nu,1-\alpha/2}\sqrt{a+b},\qquad
\nu=\frac{(a+b)^2}{a^2/(n_X-1)+b^2/(n_Y-1)}.
$$
The degrees of freedom can be noninteger. They describe an approximation to the distribution of the estimated standard error, rather than a literal count of observations.{{cite:delacre2017_welch}} (p. 96, eqs. 3–4)

## Interpretation — Why the less certain variance matters
The squared standard error is a sum of two variance estimates. The degrees-of-freedom approximation combines their sampling uncertainties: a component with large $S^2/n$ and few observations can dominate the uncertainty. Pooling instead treats the two sample variances as estimates of the same population quantity, which changes both the standard error and its calibration.{{cite:delacre2017_welch}} (pp. 95–96)

The Welch interval is approximate even under independent normal sampling with unequal population variances. Normality can be relaxed through large-sample approximations, but strong skewness, influential outliers, dependence and very small samples still matter. Pairing requires analysing within-pair differences rather than using this independent-samples formula.{{cite:cetinkaya_hardin2024}} (§§20.4 and 21.1)

## Worked example — Unequal sample sizes and spreads
Suppose $n_X=10$, $\overline x=13$, $s_X=2$, and $n_Y=20$, $\overline y=10$, $s_Y=4$. Then $a=0.4$, $b=0.8$, and
$$
SE=\sqrt{1.2}=1.09545,\qquad
\nu=27.9818.
$$
For a two-sided $95\%$ interval, $t_{\nu,0.975}=2.04847$. The interval is $3\pm2.04847(1.09545)$, or approximately $(0.7560,5.2440)$. The mean difference and both limits are in the measurement units of the response.{{cite:delacre2017_welch}} (p. 96, eqs. 3–4)

For the student-weight comparison with sample sizes $15$ and $10$, standard deviations $15$ and $12$, and mean difference $-9.5$, the same computation gives $SE=5.42218$, $\nu=22.0999$, critical value $2.07333$, and limits $(-20.74196,1.74196)$. A confidence interval spanning zero expresses uncertainty about the sign, rather than equality of the two population means.{{cite:cetinkaya_hardin2024}} (§20.4)

**Your turn.** If the two groups have equal sample sizes $n$ and equal sample variances, simplify the degrees of freedom.

::: {.callout-tip collapse="true" title="Answer"}
Here $a=b$, so $\nu=4a^2/[2a^2/(n-1)]=2(n-1)$. The Welch and pooled calculations agree in this special case.
:::

## Check yourself

### A known-variance reference calculation {#self-check-ex-inf-two-standard-errors}
[Two standard errors](../questions/ex-inf-two-standard-errors.qmd): find the exact normal coverage and the multiplier for a 99% interval.

::: {.callout-tip collapse="true" title="Answer"}
The coverage is $2\Phi(2)-1=0.9545$. A 99% interval requires the standard-normal 0.995 quantile, approximately $2.57583$. Known variance gives an exact normal calculation, while the Welch degrees of freedom calibrate an estimated variance approximately.
:::

### Pairing changes the unit of analysis {#self-check-ex-inf-paired-or-not}
[Paired or two-sample?](../questions/ex-inf-paired-or-not.qmd): classify the four study designs.

::: {.callout-tip collapse="true" title="Answer"}
Before-and-after blood pressure, repeated reaction times on each driver, and twin pairs are paired designs. The distinct, unmatched plots receiving the two fertilisers use an independent two-sample comparison. Each paired analysis is a one-sample analysis of within-pair differences.
:::
