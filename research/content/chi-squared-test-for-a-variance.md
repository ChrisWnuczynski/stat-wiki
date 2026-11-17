## Motivating example
A manufacturing change can stabilize a product without changing its average measurement. The question is then whether the population variance has fallen below a target. A small observed variance is encouraging, but its sampling variability matters especially with only seven measurements. The normal-model chi-squared test calibrates that variability.{{cite:dodge2008}} (pp. 77–78, “Chi-Square Test”)

## Definition
The exact model is $X_1,\ldots,X_n\stackrel{\mathrm{iid}}\sim N(\mu,\sigma^2)$, with $n\ge2$ and $\sigma^2>0$, and $S^2=\sum_i(X_i-\overline X)^2/(n-1)$. The statistic uses squared units in both numerator and denominator. Specifying a standard deviation of $a$ means testing variance $a^2$, rather than inserting $a$ directly. The normality assumption is essential to the exact chi-squared calibration.{{cite:dodge2008}} (pp. 77–78)

## Properties — Why the mean costs one degree of freedom
::: {.callout-note collapse="true" title="Derivation of the pivot"}
Standardize the observations as $Z_i=(X_i-\mu)/\sigma$. The vector $Z$ has independent standard normal coordinates. Rotate it with an orthogonal matrix whose first row is $n^{-1/2}(1,\ldots,1)$. Its first coordinate is $\sqrt n(\overline X-\mu)/\sigma$; the remaining $n-1$ independent standard normal coordinates describe the residual subspace. Their squared sum equals $\sum_i(X_i-\overline X)^2/\sigma^2=(n-1)S^2/\sigma^2$, which has a chi-squared law with $n-1$ degrees of freedom. Under the null replace $\sigma^2$ by $\sigma_0^2$.
:::

For a lower alternative the $p$-value is $F_{\chi^2_{n-1}}(t)$; for an upper alternative it is $1-F_{\chi^2_{n-1}}(t)$. An equal-tail two-sided convention uses $\min\{1,2\min(F(t),1-F(t))\}$. The null distribution is asymmetric, so doubling an upper tail regardless of the observation gives the wrong answer. The corresponding critical regions allocate the desired error probability to the appropriate tail or tails.{{cite:nist_handbook2002}} (§1.3.5.8, “Critical Region”)

## Worked example — What seven forks can detect
For the tuning-fork data below, the lower-tail statistic is $6(0.488)/1.1=2.6618$, with $p=0.1501$. The lower 5% quantile is $1.6354$, so rejection requires $S^2\le1.1(1.6354)/6=0.2998$. This is a substantial reduction from the target variance. Failure to reject with seven observations does not establish that the process variances coincide. The quantile calculation follows the lower-tail rule.{{cite:nist_handbook2002}} (§1.3.5.8, “Test Statistic” and “Critical Region”)

**Your turn.** With $n=11$ and target variance $4$, what statistic results from $s^2=6$? Which tail is relevant to increased variability?

::: {.callout-tip collapse="true" title="Answer"}
The statistic is $10(6)/4=15$ on ten degrees of freedom. Increased variability uses the upper tail; its $p$-value is approximately $0.1321$.
:::

## Statistical use — Power and interval inversion
For a lower-tail cutoff $c$, the power at a true variance $v$ is
$$P_v(T\le c)=F_{\chi^2_{n-1}}\left(c\frac{\sigma_0^2}{v}\right).$$
This follows by writing $T=(v/\sigma_0^2)U$ with $U\sim\chi^2_{n-1}$. Smaller true variances increase the probability of rejection. Inverting the two-sided test yields the usual chi-squared confidence interval for variance.{{cite:nist_handbook2002}} (§1.3.5.8, confidence-interval formula)

### A composite null and its least favorable boundary
A practical lower-variability question can use $H_0:\sigma^2\ge\sigma_0^2$ against $H_1:\sigma^2<\sigma_0^2$. With a lower-tail critical value $c=\chi^2_{n-1,\alpha}$ and any null variance $v\ge\sigma_0^2$, the rejection probability is $F_{\chi^2_{n-1}}(c\sigma_0^2/v)\le F_{\chi^2_{n-1}}(c)=\alpha$. Thus the equality boundary is the null value giving the largest false-rejection probability. This proves that the same rule controls the whole composite null. An upper-tail test has the analogous boundary argument with inequalities reversed. The one-sided hypotheses concern a direction of variation chosen before examining the sample.{{cite:dodge2008}} (p. 78, one-sided hypotheses)

## Assumptions and limits
A few outliers can dominate $S^2$ because deviations are squared. Normality should therefore have substantive and graphical support; a large sample alone does not turn this exact normal pivot into a distribution-free procedure. Independent measurements are also required. The chi-squared test for one variance and Pearson's test for categorical counts use the same named reference family for different mathematical reasons.{{cite:dodge2008}} (pp. 77–78)
