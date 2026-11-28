## Motivating example
Two groups can have the same mean and very different experiences. The waiting times $2,4,6,8,10$ and $6,6,6,6,6$ both average six minutes, but only the second guarantees a six-minute wait in the observed sample. A useful summary describes centre, spread, sample size and shape together. Numerical summaries compress information, so a small set of numbers should be read alongside a suitable plot.{{cite:openintro2019}} (§2.1, “Examining numerical data”)

## Intuition — Match the summary to the question
A mean answers a question about totals per observation: multiplying it by the number of observations recovers the total. A median answers a rank question: it divides the ordered observations into lower and upper halves. For a skewed distribution those are different descriptions of a typical value. For categories, a table of counts or proportions is usually more meaningful than arithmetic performed on numerical category codes.{{cite:openintro2019}} (§2.1, mean and median; §2.2, categorical data)

Spread also has several meanings. Standard deviation describes squared deviations from the mean, the interquartile range describes the central half, and the range describes endpoints. An unusually large observation directly changes the mean and squared deviations; it need not move the middle order statistics. This is why choosing a resistant summary is a scientific decision about which features matter, rather than a contest in which one formula is always best.{{cite:nist_handbook2002}} (§1.3.5.6, “Measures of Scale”)

## Properties — Location, scale and information loss
For $y_i=a+bx_i$, the sample mean is $\bar y=a+b\bar x$. Subtracting this mean gives $y_i-\bar y=b(x_i-\bar x)$, so $s_y^2=b^2s_x^2$ and $s_y=|b|s_x$. A change of units therefore rescales the standard deviation; a shift of the zero point does not. For an increasing affine transformation, all interpolated sample quantiles transform in the same way. Their differences lose the additive constant.{{cite:nist_handbook2002}} (§1.3.5.1, location; §1.3.5.6, scale definitions)

These identities are also practical error checks. Adding a constant to each value must leave the variance alone. Reporting a variance in the same units as the measurements is a units error: a variance has squared units, while a standard deviation has measurement units. A range has measurement units too, but it does not describe typical deviation from any centre.

The list of summaries is not a reconstruction of the data. Equal mean and median do not establish symmetry, and an interquartile-range-to-standard-deviation ratio does not by itself identify a distribution. Two samples can share these summaries while differing in modality, gaps, rounding or tail behaviour. A normal reference such as $\mathrm{IQR}\approx1.349\sigma$ is a population-model benchmark rather than a classification rule.{{cite:openintro2019}} (§2.1, histograms, shape and robust statistics)

## Worked example — An explicit five-number summary
For the ordered observations $1,2,3,4,10$, the mean is $4$, the median is $3$, and the quartiles at positions $1+(n-1)p$ are $2$ and $4$. Thus the five-number summary is $(1,2,3,4,10)$, the range is $9$, and the interquartile range is $2$. That $1+(n-1)p$ position rule is Hyndman–Fan type 7, R's default [sample quantile](sample-quantile.qmd) convention, whereas [five-number summary and boxplot](five-number-summary-and-boxplot.qmd) uses the $p(n+1)$ rule, which is type 6.{{cite:r_stats_quantile}} (Details, Type 6 and Type 7) Squared deviations from the mean are $9,4,1,0,36$, with sum $50$. Dividing by $n-1=4$ gives sample variance $12.5$ and standard deviation $3.536$ to three decimals. The right endpoint makes a substantial contribution to squared spread while leaving the median at $3$.

If every value is multiplied by $10$ and then increased by $5$, the mean becomes $45$, the median $35$, the standard deviation approximately $35.355$, the range $90$, and the interquartile range $20$. The sample variance is $1250$. The calculations follow the affine identities directly, providing a second route for checking a software result.{{cite:nist_handbook2002}} (§1.3.5.6, sample variance and standard deviation)

**Your turn.** Find the mean, median, range and sample variance of $2,2,5,7$. Explain which of these changes when every observation increases by $100$.

::: {.callout-tip collapse="true" title="Answer"}
The mean is $4$, the median is $(2+5)/2=3.5$, and the range is $5$. Squared deviations from $4$ sum to $4+4+1+9=18$, giving sample variance $18/3=6$. Increasing every observation by $100$ increases the mean and median by $100$ and leaves both measures of spread unchanged.
:::

## Statistical use — Describing the patients' ages
For the patient-age data, a mean of approximately $60.83$ and median $60$ indicate similar numerical centres, while quartiles $51$ and $70$ identify the middle half directly. The range from $40$ to $95$ adds endpoint information. Those statements describe this group of patients; generalising to another population requires a sampling argument. The relationship between mean and median alone cannot establish approximate symmetry, and the ratio $19/11.89\approx1.598$ cannot establish that a distribution is flat. Inspecting the age plot is needed to assess shape.{{cite:openintro2019}} (§2.1, histograms and shape)

## Assumptions and limits
Always report the number of nonmissing observations used. A standard deviation computed after deleting missing ages can describe a different subset from a mean computed on another variable. Different quartile interpolation conventions can also give slightly different results for the same ordered sample. State the convention when exact reproduction matters, especially in small samples. Finally, the standard deviation of observations and the standard error of their mean answer different questions: one describes variation among people, while the other describes sampling variation of an estimator.

## Connections — Why the variance divisor is one smaller
For iid observations with mean $\mu$ and finite variance $\sigma^2$, the identity $\sum_i(X_i-\bar X)^2=\sum_i(X_i-\mu)^2-n(\bar X-\mu)^2$ separates deviations around the estimated and population means. Its expectation is $n\sigma^2-n(\sigma^2/n)=(n-1)\sigma^2$. Dividing by $n-1$ therefore gives an unbiased sample variance. The square root does not preserve unbiasedness, so the sample standard deviation need not be an unbiased estimator of $\sigma$. This argument depends on the iid sampling variance of the mean; correlated observations require a different calculation.

For independent observations with a finite variance, the divisor n minus 1 estimates that variance, while the divisor n estimates the mean squared deviation from the sample mean and is smaller by the factor (n-1)/n. Quoting one divisor without the other hides which of those two targets was estimated.
