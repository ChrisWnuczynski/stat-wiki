## Motivating example
A tablet producer needs uncertainty for consistency as well as for average weight. A sample standard deviation of 1.3 mg estimates variation among tablets, while its confidence interval expresses uncertainty about that population spread. Because squared normal residuals have a skewed distribution, symmetric error bars around the variance estimate are generally inappropriate.{{cite:dodge2008}} (pp. 77–78, normal-variance chi-squared statistic)

## Definition
Let the observations be independent $N(\mu,\sigma^2)$, with unknown mean, positive variance, and $n\ge2$. Write $\nu=n-1$ and $A=\nu S^2$. Orthogonally rotating the standardized observation vector separates its mean coordinate from $\nu$ independent normal residual coordinates. Their squared norm is $A/\sigma^2\sim\chi^2_\nu$. This establishes the normal-sample pivot underlying the variance interval.{{cite:dodge2008}} (pp. 77–78)

## Properties — Inverting decreasing dependence
For positive quantiles $q_l<q_u$,
$$q_l\le A/\sigma^2\le q_u\quad\Longleftrightarrow\quad A/q_u\le\sigma^2\le A/q_l.$$
The inequalities reverse their endpoint roles because division by a positive variance is decreasing in that variance. Choosing $q_l=\chi^2_{\nu,\alpha/2}$ and $q_u=\chi^2_{\nu,1-\alpha/2}$ yields equal-tail coverage $1-\alpha$. Taking square roots carries exactly the same event to an interval for $\sigma$. The interval is positive and asymmetric.{{cite:nist_handbook2002}} (§1.3.5.8, confidence-interval formula)

Different tail allocations whose probabilities sum to $\alpha$ also give valid intervals. The equal-tail choice is conventional; it does not generally minimize length on every transformed scale. A one-sided upper bound uses $A/\chi^2_{\nu,\alpha}$, with probability $1-\alpha$ of exceeding the true variance.{{cite:dodge2008}} (pp. 106–107, pivot construction and error allocation)

## Worked example — Reading squared units
For the tablet data, $A=24(1.3^2)=40.56$ mg squared. Unrounded chi-squared quantiles give the variance interval $(1.0304,3.2707)$ mg squared and the standard-deviation interval $(1.0151,1.8085)$ mg. Rounding standard-deviation endpoints to two decimals produces $(1.02,1.81)$. Since the lower endpoint exceeds 1.0 mg, the corresponding equal-tail 5% test rejects that proposed standard deviation under the normal model.{{cite:nist_handbook2002}} (§1.3.5.8, interval and test relationship)

**Your turn.** For $n=10$ and $s=2$, express the 95% variance interval using chi-squared quantiles and calculate its endpoints.

::: {.callout-tip collapse="true" title="Answer"}
There are nine degrees of freedom and $A=9(4)=36$. The interval is $(36/\chi^2_{9,0.975},36/\chi^2_{9,0.025})$, approximately $(1.8925,13.3314)$. Square roots give approximately $(1.3757,3.6512)$ for the standard deviation.
:::

### Estimating spread is not estimating the mean
Replacing the sample size by a larger number affects the variance interval through both $A=(n-1)s^2$ and the reference quantiles. A narrow confidence interval for a mean can arise from many highly variable observations, because the mean's standard error is $\sigma/\sqrt n$. The variance interval instead targets the spread among individual observations. It should therefore be reported in squared units, or transformed to a standard-deviation interval when the measurement units make interpretation easier. If the population mean is genuinely known, the different sum $\sum_i(X_i-\mu)^2/\sigma^2$ has $n$ normal squared coordinates; estimating the mean is precisely what reduces the residual dimension to $n-1$. The unknown-mean interval cannot simply be given $n$ degrees of freedom.{{cite:dodge2008}} (pp. 77–78, unknown-mean normal sample)

## Assumptions and limits
Normality supports the exact distribution, independently of the unknown mean. It is a stronger premise than merely having a finite variance. Heavy tails and outliers change the sampling distribution of $S^2$, potentially changing coverage substantially. For a large independent sample from a nonnormal distribution, a variance interval can instead use an estimate of the fourth-moment contribution to the variance of $S^2$; that is a different procedure. The confidence statement always concerns repeated samples from the specified population.{{cite:dodge2008}} (p. 107, domains and limitations of confidence intervals)
