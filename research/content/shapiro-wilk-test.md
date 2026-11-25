## Lead context
It is a test of the composite hypothesis that a complete sample comes from some normal distribution. Location and scale are not specified in advance. A small value of the statistic is evidence against that hypothesis, and a large value is not evidence that the hypothesis is true.

## Motivating example
Eight reaction times, in seconds, are
$$
2.0,\; 2.2,\; 2.5,\; 2.7,\; 3.1,\; 3.4,\; 4.0,\; 8.5.
$$
Seven of them sit between $2$ and $4$. The eighth is more than twice the largest of those seven. A normal probability plot asks whether the ordered sample tracks the quantiles of a normal curve. The Shapiro–Wilk statistic turns that question into one number, $W$, small when the order statistics fail to line up with the expected normal order statistics. On these eight numbers $W$ falls below the $1\%$ point of its null distribution. The same eight numbers, after a natural logarithm, give a $W$ above the $10\%$ point. The calculation is the worked example. The second result does not prove that the logarithms are normal.

## Definition — A scaled slope against normal order statistics
Let $x_{(1)} \le \cdots \le x_{(n)}$ be the ordered sample, and write $m_i$ for the expected value of the $i$th order statistic in a standard normal sample of size $n$. Let $V$ be the covariance matrix of those order statistics. The best linear unbiased estimate of the slope in the regression of the $x_{(i)}$ on the $m_i$ uses both $m$ and $V$. Write
$$
b = \sum_{i=1}^{n} a_i x_{(i)}.
$$
The coefficient vector $a = (a_1,\ldots,a_n)$ is the normalised best linear unbiased vector, so $b$ is proportional to that slope estimate. It is not the slope itself. The Shapiro–Wilk statistic is
$$
W = \frac{b^2}{\sum_{i=1}^{n}(x_i - \bar x)^2}.
$$
The coefficients $a_i$ are determined by $m$ and by $V$. They are not the ordinary least-squares coefficients from a plot of $x_{(i)}$ against $m_i$ alone, because that plot’s residuals are correlated. For a symmetric reference distribution the coefficients are antisymmetric, $-a_i = a_{n+1-i}$, and the middle coefficient is zero when $n$ is odd.{{cite:shapiro_wilk1965}} (pp. 592–593, 603) {{cite:nist_shapiro2002}} (§7.2.1.3)

If the sample really is normal, the numerator and the denominator are estimating the same multiple of the variance, and $W$ tends to sit near its upper bound of $1$. If the sample is not normal, the two pieces are not estimating the same thing, and the null mean of $W$ is shifted to the left. Small values of $W$ are the evidence against normality. The distribution of $W$, for a sample from a normal distribution, depends only on $n$. That is the content of scale and origin invariance. Multiplying every observation by $c > 0$ multiplies $b$ by $c$ and therefore the numerator $b^2$ by $c^2$, and it multiplies the denominator by $c^2$. Adding a constant leaves $b$ unchanged, because the coefficients sum to zero, and it leaves the sum of squared deviations unchanged.{{cite:shapiro_wilk1965}} (pp. 592–593, Lemma 1 and the bound $W \le 1$)

For even $n = 2k$ the numerator can be computed from the upper half of the coefficients and the gaps between opposite order statistics,
$$
b = \sum_{i=1}^{k} a_{n-i+1}\bigl(x_{(n-i+1)} - x_{(i)}\bigr), \qquad W = b^2 \Big/ \sum_{i=1}^{n}(x_i - \bar x)^2.
$$
The coefficients for $n \le 50$ are tabulated. They are an input to the statistic, not a quantity to be re-derived from $V$ in the course of a single test.{{cite:shapiro_wilk1965}} (p. 603 and Table 5)

## Interpretation — What a small $p$-value settles, and what a large one does not
The test rejects for small $W$. A $p$-value is the probability, under normality, of a statistic at most as large as the one observed. A small $p$-value is evidence that this sample’s order statistics are a poor match to the normal pattern. It is not a measure of how badly a later $t$ test or analysis of variance will behave, and it is not a measure of the scientific size of the departure. The introduction of the procedure makes the modest claim: knowing that a normality assumption is wrong should temper the use of methods that were derived under it, and should send the analyst back to the plot, to a transformation, or to a procedure that does not need the assumption.{{cite:shapiro_wilk1965}} (p. 591)

A large $p$-value means that $W$ did not fall in the rejection region for that $n$. Many non-normal distributions produce samples whose $W$ sits above a $5\%$ or $10\%$ point, especially when $n$ is small. Failure to reject is the statement the test is able to make. It is not a demonstration that the distribution is normal. In the paper’s own numerical illustration, a $W$ above the $10\%$ point is treated as compatible with a normal sample of the remaining effects, and the plot is still part of the argument. The statistic was proposed as a supplement to the normal probability plot, not as a replacement for it.{{cite:shapiro_wilk1965}} (pp. 607, 610)

The null distribution moves with $n$. The lower $5\%$ point of $W$ is $0.818$ at $n = 8$, $0.905$ at $n = 20$ and $0.947$ at $n = 50$. A numerical value such as $0.85$ is above the $5\%$ point at $n = 8$ and below it at $n = 20$. The same $W$ is therefore not the same significance statement at two sample sizes. At $n = 20$ the test is already sensitive to strong skewness: in the published sampling comparison, a $5\%$ test has empirical power $0.98$ against a chi-squared distribution on one degree of freedom. Sensitivity at one sample size is not a power curve, and the critical-value table is not one either. What the table does show is that a larger $n$ requires $W$ closer to $1$ before the sample is passed at a fixed level.{{cite:shapiro_wilk1965}} (Table 6, p. 605; Table 7, p. 608; p. 609)

The normal model in a one-way layout is a statement about the errors. The observations follow $Y_{ij} = \mu + \tau_i + \varepsilon_{ij}$ with the $\varepsilon_{ij}$ independent and $N(0, \sigma^2)$. The raw responses are those errors plus the group means. A Shapiro–Wilk test of the pooled responses confuses a difference of means with a failure of normality.{{cite:dodge2008}} (p. 399)

Normal Q–Q plots of within-group fitted residuals can help diagnose departures from the error model, but do not establish normality. The fitted residuals are not generally an independent sample: subtracting each fitted group mean constrains the residuals in that group to sum to zero. With two groups of size two, the residuals in group $i$ are exactly $(d_i, -d_i)$, where $d_i = (Y_{i1} - Y_{i2})/2$, even when the errors are independent and normal. The ordinary Shapiro–Wilk $p$-value calibration therefore does not generally apply to pooled fitted residuals; a formal test requires calibration that accounts for the fitted model.

## Worked example — The same eight times, raw and logged
The assumptions for the calculation are that the eight times are a complete sample, with no missing values, and that the question is the composite normal hypothesis. The coefficients for $n = 8$, reading down the tabulated column, are
$$
a_8 = 0.6052,\; a_7 = 0.3164,\; a_6 = 0.1743,\; a_5 = 0.0561,
$$
and $a_i = -a_{9-i}$. The ordered sample is already $2.0, 2.2, 2.5, 2.7, 3.1, 3.4, 4.0, 8.5$. The gaps that enter $b$ are
$$
8.5 - 2.0 = 6.5,\; 4.0 - 2.2 = 1.8,\; 3.4 - 2.5 = 0.9,\; 3.1 - 2.7 = 0.4.
$$
Hence
$$
\begin{align*}
b &= 0.6052 \times 6.5 + 0.3164 \times 1.8 + 0.1743 \times 0.9 + 0.0561 \times 0.4 \\
&= 3.93380 + 0.56952 + 0.15687 + 0.02244 = 4.68263.
\end{align*}
$$
The sample mean is $28.4/8 = 3.55$, and the sum of squared deviations from it is $1549/50 = 30.98$. Therefore
$$
W = \frac{4.68263^2}{30.98} = 0.70778.
$$
The lower $1\%$ point at $n = 8$ is $0.749$ and the lower $5\%$ point is $0.818$. The observed $0.70778$ is below the $1\%$ point, so the $1965$ table rejects normality at $1\%$.{{cite:shapiro_wilk1965}} (Tables 5 and 6, pp. 603–605)

The normal probability plot makes the same departure visible without producing $W$. One plotting position for the $i$th ordered value is $(i - 1/2)/n$. For $n = 8$ the standard normal quantiles of those eight positions run from $-1.534$ to $1.534$. The step from $4.0$ to $8.5$ is $4.5$, and the step from $3.4$ to $4.0$ is $0.6$. The corresponding quantile steps are $0.647$ and $0.398$. The data step is $7.5$ times the one before it; the quantile step is $1.62$ times the one before it. That is the gap $b$ has charged at the largest coefficient, $0.6052$.{{cite:dodge2008}} (p. 382)

`shapiro.test` on these eight numbers returns $W = 0.70772$ and an approximate $p$-value $0.002753$. The statistic matches the four-decimal table to three significant figures. The $p$-value is not an exact tail probability from Table 6. The returned probability is an approximation except at $n = 3$, where it is exact; separate approximations are used for $4 \le n \le 11$ and for $n \ge 12$. Both the table and the software agree that the result is below the $1\%$ point.{{cite:r_shapiro_test2026}} (Value and Source)

Now replace each time by its natural logarithm. The ordered logs are $0.693, 0.788, 0.916, 0.993, 1.131, 1.224, 1.386, 2.140$, to three decimals. The same four coefficients give $b = 1.12618$ and a sum of squared deviations $1.45981$, so $W = 0.86879$. At $n = 8$ the lower $10\%$ point is $0.851$ and the lower $50\%$ point is $0.932$. The value $0.869$ lies above the $10\%$ point, so the $1965$ $5\%$ test and the $10\%$ test both fail to reject. `shapiro.test` returns $W = 0.86886$ and $p = 0.1469$, the same conclusion.{{cite:shapiro_wilk1965}} (Table 6, p. 605) {{cite:r_shapiro_test2026}} (Value)

The transformation changed the conclusion. It did not certify the log-times as normal. A sample of size $8$ whose $W$ is $0.87$ has simply failed to reach the rejection region. The plot of the logs against the same normal quantiles is straighter than the raw plot, and that is a description of these eight points. It is not a proof of the distribution.

**Your turn.** A sample of size $8$ has $W = 0.85$, and a sample of size $20$ has the same $W = 0.85$. The lower $5\%$ points are $0.818$ at $n = 8$ and $0.905$ at $n = 20$. What does the $5\%$ test do in each case?

::: {.callout-tip collapse="true" title="Answer"}
The test rejects for small $W$. At $n = 8$, $0.85 > 0.818$, so the $5\%$ test does not reject. At $n = 20$, $0.85 < 0.905$, so the $5\%$ test rejects. The number $0.85$ is not a significance statement until it is compared with the critical value for that sample size.
:::

## Statistical use — Residuals, software, and the plot
The ordinary Shapiro–Wilk $p$-value is calibrated under a null model of independent, identically distributed normal observations. For a single group of independent, identically distributed observations, subtracting its sample mean leaves $W$ unchanged by location invariance, so centring alone does not alter the test. This invariance does not justify applying the ordinary calibration to residuals pooled after fitting separate group means.

The function `shapiro.test` accepts a numeric vector of length $3$ to $5000$ after missing values are removed. It returns $W$ and an approximate $p$-value. For $n = 3$ that $p$-value is exact; between $4$ and $11$, and again from $12$ upward, the reference distribution is an approximation.{{cite:r_shapiro_test2026}} (Usage, Arguments, Value and Source) The documentation of that returned $p$-value says the approximation is adequate for $p$-values below $0.1$, and it attributes the statement to Royston’s 1995 paper.{{cite:r_shapiro_test2026}} (Value) A result near $0.15$, such as the logged times in the worked example below, is on the side of the approximation where that report does not claim accuracy, which is another reason to read it together with the probability plot rather than as a sharp probability.

The coefficients themselves need not be recomputed. For $n \le 50$ they are the tabulated values used in the worked example below. For larger $n$ the original difficulty was precisely that the coefficients and the percentage points become awkward to tabulate. Software is the practical source of $W$ in that range. The hand calculation in that worked example is a check that the software statistic is the $1965$ statistic, not a second definition.{{cite:shapiro_wilk1965}} (p. 610)

## Assumptions and limits — Complete samples and a null that depends on $n$
The derivation assumes a complete sample: every order statistic from $1$ to $n$ is present. A sample with missing values, or a censored sample, is not this statistic. The null is the whole normal family, not a normal distribution with a stated mean and variance. That is why scale and origin invariance matter, and why $W$ does not answer a simple goodness-of-fit question in which $\mu$ and $\sigma$ were given before the data.{{cite:shapiro_wilk1965}} (pp. 591–593)

The percentage points in the $1965$ table run to $n = 50$ and are themselves based on sampling and a curve fit for the larger sizes in that range. Quoting a point from that table is not the same act as quoting an exact binomial tail. The $p$-value from `shapiro.test` adds a further approximation except at $n = 3$. For the eight raw times the distinction is harmless, because $0.708$ is below the tabulated $1\%$ point $0.749$ and the software $p$-value is $0.00275$. For a $W$ close to a critical value, the table and the software probability can be reported side by side rather than collapsed into one number.{{cite:shapiro_wilk1965}} (Table 6, note on the approximation) {{cite:r_shapiro_test2026}} (Source)

## Common misconceptions — A large probability is not a proof of normality
The logged sample is the counterexample to the most common reading. Its $W$ is about $0.869$, its software $p$-value is about $0.15$, and the $1965$ $10\%$ point at $n = 8$ is $0.851$. Nothing in that comparison says the logarithms came from a normal distribution. It says a normal sample of size $8$ often produces a $W$ this far from $1$. The raw sample, with $W = 0.708$ and $p = 0.00275$, is the case the test was built to flag. Treating the two $p$-values as “not normal” and “normal” uses the second one as a proof it cannot be.

A related confusion is to read a very small $p$-value in a large sample as a large departure. The power against a fixed alternative grows with $n$. Against a $t$ distribution on $7$ degrees of freedom, a symmetric law with kurtosis $5$, a $5\%$ Shapiro–Wilk test rejected about $58\%$ of samples of size $200$ and about $90\%$ of samples of size $500$. Against asymmetric alternatives the same test had reached good power once $n$ was at least $50$. The comparison’s conclusion is that this power rises with the sample size, while remaining low for samples of size $30$ and below. A significant result in a large sample can also come from a small deviation from normality, and that small deviation need not affect a parametric procedure that uses the same observations. Those are different questions, and the second one is not a function of $W$ alone.{{cite:razali_wah2011}} (Table 1, p. 28; p. 29; Table 2, p. 30; p. 32) {{cite:ghasemi_zahediasl2012}} (§3, Normality Tests)

## History — The 1965 analysis-of-variance form
S. S. Shapiro and M. B. Wilk introduced $W$ in 1965 as a summary of the normal probability plot. The slope of the regression of the order statistics on their normal expected values estimates the scale if the plot is linear. Dividing the square of that slope by the ordinary sum of squares produces a scale-free statistic for the composite null. The coefficients are the normalised best linear unbiased coefficients, which bring in the covariances of the order statistics as well as their means. The null percentage points were obtained by sampling, and a comparison at sample size $20$ found the test sensitive across a wide range of alternatives, particularly skewness and long tails.{{cite:shapiro_wilk1965}} (pp. 591–593, 608, 610)

The same statistic is stated with its $1965$ origin, the formula, and the fact that the coefficients come from the means, variances and covariances of the normal order statistics. The implementation in `shapiro.test` follows Royston’s later algorithm: the returned $p$-value is exact only for $n = 3$, and approximations are used for $4 \le n \le 11$ and for $n \ge 12$.{{cite:nist_shapiro2002}} (§7.2.1.3) {{cite:r_shapiro_test2026}} (Source and References)

## Connections — The normal plot, the transformation, and the t test
A [normal quantile plot](normal-quantile-plot.qmd) is the picture $W$ summarises. The [normal distribution](normal-distribution.qmd) is the hypothesis under test. [Transformations of data](transformations-of-data.qmd) are one response when the raw sample is rejected and the scientific scale can change, as with the logarithms above. The [one-sample $t$ test](one-sample-t-test.qmd) and the [two-sample $t$ test](two-sample-t-test.qmd) are procedures whose derivations use normality; a Q–Q plot of fitted residuals can help diagnose departures from the error model, but does not establish normality or replace the $t$ inference. An ordinary Shapiro–Wilk $p$-value on pooled fitted residuals does not generally have the calibration of a test on an independent, identically distributed normal sample.

## Check yourself
**1.** Every reaction time in the worked example is multiplied by $10$. What happens to $W$?

::: {.callout-tip collapse="true" title="Answer"}
Each order statistic is multiplied by $10$, so each gap in $b$ is multiplied by $10$ and $b$ is multiplied by $10$. The sum of squared deviations is multiplied by $100$. The ratio $b^2$ over that sum is unchanged. The same conclusion is the scale invariance of $W$.
:::

**2.** At $n = 50$ the lower $5\%$ point of $W$ is $0.947$, and a sample of that size has $W = 0.96$. Does the $5\%$ test reject, and does the result establish normality?

::: {.callout-tip collapse="true" title="Answer"}
The test rejects for small $W$. Here $0.96 > 0.947$, so the $5\%$ test does not reject. Failing to reject means the statistic missed the rejection region. It does not establish that the sample came from a normal distribution.
:::

**3.** A one-way layout has different group means, and a Shapiro–Wilk test of all the raw responses pooled together gives a small $W$. Which series is the normality assumption of that layout about?

::: {.callout-tip collapse="true" title="Answer"}
The errors. Each observation is a group mean plus an error, so the pooled raw responses mix those means into the shape. Normal Q–Q plots of within-group fitted residuals can help diagnose departures from the error model, but do not establish normality. Fitting the group means makes the residuals dependent, so the ordinary Shapiro–Wilk $p$-value calibration does not generally apply to the pooled residuals.
:::
