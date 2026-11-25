## Lead context
Two samples from the same population usually give different estimates. The standard error puts a scale on that variation, so an estimate can be reported with an interval or compared with a hypothesised value. It depends on the statistic and the sampling design, as well as on sample size.{{cite:nist_glossary2002}} (Glossary, “standard error”) {{cite:nist_mean_limits2002}} (§1.3.5.2)

## Motivating example
Suppose a scale is used on repeated independent batches of 100 items. Individual item weights have a standard deviation of 20 grams, but the mean weight of each batch has a standard deviation of only 2 grams. The first number describes variation *within* a batch; the second describes how the batch average varies *between* batches. Reporting the latter as the standard error answers a question about the precision of the estimated population mean.{{cite:nist_glossary2002}} (Glossary, “standard error”)

## Intuition
Imagine taking the same size sample many times and plotting one estimate from each sample. The standard deviation of those estimates is the standard error, whether or not their distribution is normal. Its estimated value is calculated from the one sample actually observed. Repeating an experiment more often is a thought experiment for defining precision; it does not require physically collecting many samples.{{cite:nist_glossary2002}} (Glossary, “standard error”)

## Definition
For a random sample $X_1,\ldots,X_n$ with population mean $\mu$, finite population standard deviation $\sigma$, and $n\geq2$, let $\overline X=n^{-1}\sum_iX_i$ be the random sample mean. Its standard error is

$$
\operatorname{se}(\overline X)=\sqrt{\operatorname{Var}(\overline X)}=\frac{\sigma}{\sqrt n},
\qquad
\widehat{\operatorname{se}}(\overline X)=\frac{s}{\sqrt n}.
$$

Here $\operatorname{Var}$ is variance across repeated independent samples, $s$ is the sample standard deviation, and the hat indicates that the unknown $\sigma$ has been replaced by an estimate. The units of both standard errors match the units of $X_i$. The formula $s/\sqrt n$ describes an independent, identically distributed sample mean; another estimator or sampling design needs its own variance calculation.{{cite:nist_glossary2002}} (Glossary, “standard error”) {{cite:nist_mean_limits2002}} (§1.3.5.2)

## Properties
For two independent sample means, $\overline X_1$ and $\overline X_2$, with sample sizes $n_1,n_2$ and population variances $\sigma_1^2,\sigma_2^2$, the standard error of their difference is $\sqrt{\sigma_1^2/n_1+\sigma_2^2/n_2}$. This is the uncertainty scale for an estimated difference. If the means are dependent, subtract twice their covariance inside the square root; ignoring positive covariance can overstate the standard error of a paired difference.{{cite:grinstead_snell1997}} (Ch. 6, §6.2, Ex. 23)

For an affine transformation of an estimator, $\operatorname{se}(aT+b)=|a|\operatorname{se}(T)$ for constants $a,b$. Adding a fixed offset changes the estimate but not its precision; changing units scales both the estimate and its standard error. For an independent sample mean, doubling $n$ divides its standard error by $\sqrt2$, while halving the standard error takes four times as many observations when $\sigma$ stays fixed.{{cite:nist_mean_limits2002}} (§1.3.5.2)

When $X_i$ are independent normal observations, the standardised mean $(\overline X-\mu)/(s/\sqrt n)$ has an exact Student $t$ distribution with $n-1$ degrees of freedom. Thus an exact two-sided interval for $\mu$, under that model, is $\overline X\pm t_{n-1,1-\alpha/2}s/\sqrt n$, where $t_{n-1,1-\alpha/2}$ is the indicated $t$ quantile and $1-\alpha$ is the chosen coverage. The multiplier accounts for estimating $\sigma$; the standard error alone does not set the coverage.{{cite:siegrist2022_normals}} (§6.08) {{cite:nist_mean_limits2002}} (§1.3.5.2)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For independent identically distributed $X_i$ with variance $\sigma^2$, variance additivity gives $\operatorname{Var}(\overline X)=n^{-2}\sum_i\operatorname{Var}(X_i)=\sigma^2/n$. For independent means the covariance of the two averages is zero, so $\operatorname{Var}(\overline X_1-\overline X_2)=\operatorname{Var}(\overline X_1)+\operatorname{Var}(\overline X_2)$. In general, $\operatorname{Var}(A-B)=\operatorname{Var}(A)+\operatorname{Var}(B)-2\operatorname{Cov}(A,B)$, proving the dependent-sample qualification too. Finally $\operatorname{Var}(aT+b)=a^2\operatorname{Var}(T)$ proves the affine rule and the square-root sample-size comparison.{{cite:grinstead_snell1997}} (Ch. 6, §6.2, Ex. 23)

Under independent normal sampling, $Z=\sqrt n(\overline X-\mu)/\sigma$ is standard normal, $U=(n-1)s^2/\sigma^2$ is chi-squared with $n-1$ degrees of freedom, and $Z$ and $U$ are independent by the normal sample theorem. Therefore $Z/\sqrt{U/(n-1)}=(\overline X-\mu)/(s/\sqrt n)$ has the stated $t$ distribution. Its central $1-\alpha$ probability, rearranged to put $\mu$ between the two limits, proves the interval claim.{{cite:siegrist2022_normals}} (§6.08) {{cite:nist_mean_limits2002}} (§1.3.5.2)
:::
:::

## Statistical use
An analyst reports an estimate with its standard error to show sampling precision, then uses a critical multiplier to form an interval or a test statistic. A normal-reference multiplier near two is useful only when a suitable normal approximation holds. Small normal samples with unknown variance call for a $t$ multiplier, as in the exact result above. Dividing the difference between an estimate and a hypothesised value by its standard error expresses that difference on the sampling-uncertainty scale; the appropriate reference distribution depends on the model.{{cite:nist_mean_limits2002}} (§1.3.5.2)

## Worked example
An independent sample of 25 readings has mean 50.0 and sample standard deviation 10.0 units. The estimated standard error is $10/\sqrt{25}=2.0$ units. If a normal population model is plausible, the exact 95% interval uses $t_{24,0.975}\approx2.064$ and is $50.0\pm2.064(2.0)$, or about $(45.87,54.13)$ units. By contrast, $50\pm2$ is a one-standard-error band and is much narrower. The standard deviation of individual readings, 10, is not the standard error of their mean.{{cite:nist_mean_limits2002}} (§1.3.5.2)

**Your turn.** Suppose another independent sample of 25 readings from a population with the same standard deviation has a mean of 54. What is the estimated standard error of the difference between the two means, and how many standard errors apart are 50 and 54? Use 10 as the standard deviation estimate for each group.

::: {.callout-tip collapse="true" title="Answer"}
Each mean has estimated standard error $10/5=2$. Independence gives $\widehat{\operatorname{se}}(\overline X_1-\overline X_2)=\sqrt{2^2+2^2}=\sqrt8\approx2.83$. The difference of 4 units is about $4/\sqrt8\approx1.41$ standard errors. The corresponding test or interval also needs a reference distribution under its sampling model.
:::

## Common misconceptions
A standard error is not the standard deviation of the data. The two can have the same units, but their sampling targets differ. Neither is the *bias* of an estimator: a systematically wrong estimator can have a tiny standard error. One standard error on either side of an estimate is also not automatically a 95% interval; the exact normal calculation in the normal example on this page gives only about 68.3% coverage with a one-standard-error multiplier.{{cite:nist_glossary2002}} (Glossary, “standard error”) {{cite:nist_mean_limits2002}} (§1.3.5.2)

## Assumptions and limits
The square-root-of-$n$ rule assumes independent observations with a common finite variance. Positive dependence, repeated measures, or clusters can change the variance of an average; treating correlated observations as independent commonly understates uncertainty. Even with a correctly calculated standard error, sampling bias, measurement error, and a wrong model are different problems that a small standard error cannot fix. The exact $t$ interval above needs independent normal observations; outside that model, its coverage may be approximate or poor.{{cite:nist_mean_limits2002}} (§1.3.5.2) {{cite:siegrist2022_normals}} (§6.08)

## Connections
An [estimator](estimator.qmd) is the random rule whose sampling spread the standard error describes; its realised estimate is a number from one dataset. [Sample variance and standard deviation](sample-variance-and-standard-deviation.qmd) describe spread of observations and supply $s$ for the mean's estimated standard error. A [confidence interval](confidence-interval.qmd) uses a standard error together with a calibrated multiplier, while a [pivot](pivot.qmd) divides estimation error by a scale to obtain a reference distribution.{{cite:nist_glossary2002}} (Glossary, “standard error”) {{cite:nist_mean_limits2002}} (§1.3.5.2)

## History
In 1908, William Sealy Gosset, writing as “Student,” investigated how to judge a sample mean when a small sample is the only source of information about variability. He noted that substituting a sample estimate for the population spread adds uncertainty, particularly with few observations. His paper developed a reference distribution for a standardised mean under normal sampling rather than treating the estimated spread as known.{{cite:student1908}} (pp. 1–5)

The problem remains visible in modern interval practice. The NIST e-Handbook presents the mean interval with a sample-standard-deviation standard error and a $t$ quantile, explaining how its width responds to variability and sample size. Its glossary defines standard error through a statistic's sampling distribution, a definition that applies beyond means and Student's original normal-sample calculation.{{cite:nist_mean_limits2002}} (§1.3.5.2) {{cite:nist_glossary2002}} (Glossary, “standard error”)
