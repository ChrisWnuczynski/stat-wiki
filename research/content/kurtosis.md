## Lead context

Two samples can share a mean and a standard deviation and still differ in how much probability sits in the tails. Kurtosis is the moment comparison of that fourth-power balance with a normal curve. A value near 3 matches the normal benchmark. A larger value means more of the fourth-power mass sits in the extremes. {{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Kurtosis”) {{cite:dodge2008}} (p. 91)

## Motivating example

A normal sample of 10,000 draws had moment kurtosis 2.96, close to the normal value 3, and skewness 0.03. A double-exponential sample of the same size, symmetric and more peaked, with heavier tails, had skewness 0.06 and kurtosis 5.9. A Cauchy sample, restricted in the histogram to the interval from $-10$ to $10$, still produced a moment kurtosis of 6,693, because the unrestricted draws ran from about $-29{,}000$ to about $89{,}000$. The pictures and the coefficients are describing the same contrast. A Weibull sample with shape 1.5 had skewness 1.08 and kurtosis 4.46, a moderate departure on both scores. {{cite:nist_skewness2002}} (§1.3.5.11, “Examples”)

## Intuition

The fourth power makes a deviation of 4 count as much as 256 deviations of 1, because $4^4=256$. Dividing by the fourth power of the standard deviation removes the units, so a change of scale does not change the coefficient. A value above the normal benchmark means the fourth-power mass is more extreme than a normal curve with the same variance. A value below it means the observations are more tightly confined. A uniform distribution is the light-tailed end of that comparison. High kurtosis points toward heavy tails or outliers. Low kurtosis points toward light tails. {{cite:nist_skewness2002}} (§1.3.5.11, “Skewness and Kurtosis”) {{cite:dodge2008}} (p. 91)

## Definition

For a random variable with mean $\mu$ and standard deviation $\sigma$, the coefficient of kurtosis is the standardised fourth central moment

$$
\beta_2=\frac{\mu_4}{\sigma^4},\qquad \mu_4=\mathrm{E}(X-\mu)^4.
$$


For a normal distribution the centred moments satisfy $\mu_s=(s-1)\sigma^2\mu_{s-2}$, with $\mu_0=1$ and $\mu_1=0$, so $\mu_2=\sigma^2$ and $\mu_4=3\sigma^4$. Therefore $\beta_2=3$. A distribution with $\beta_2<3$ is called platykurtic. A distribution with $\beta_2>3$ is called leptokurtic. NIST’s reading of the same inequality is in terms of tails: high kurtosis goes with heavy tails or outliers, and low kurtosis with light tails. {{cite:dodge2008}} (pp. 91–92) {{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Kurtosis”) These labels compare standardised fourth moments with the normal benchmark; they do not determine the height, shape or modality of a density peak.

For a sample $y_1,\ldots,y_N$ the moment kurtosis uses the divisor $N$ both in the central moments and in the standard deviation:

$$
\frac{\sum_{i=1}^N(y_i-\bar y)^4/N}{s^4},
$$


where $s^2=\sum_i(y_i-\bar y)^2/N$. Some software subtracts 3 and calls the result kurtosis, so that a normal sample is centred at 0. That excess convention is a shift of the same ratio. The handbook uses the unshifted definition, with normal benchmark 3. {{cite:nist_skewness2002}} (§1.3.5.11, “Alternative Definition of Kurtosis”) {{cite:dodge2008}} (p. 91)

## Properties

The coefficient does not depend on the unit of measurement, because both the fourth moment and $\sigma^4$ scale by the fourth power of a change of unit. It does depend on the convention. A reported kurtosis of 0 and a reported kurtosis of 3 can be the same normal benchmark under the two definitions. The sign of an excess, kurtosis minus 3, is the sign of the departure from the normal fourth moment. {{cite:nist_skewness2002}} (§1.3.5.11, “Alternative Definition of Kurtosis”) {{cite:dodge2008}} (p. 91)

A symmetric law can still produce a wild sample coefficient when the tails are heavy enough to wreck the sample moments. The Cauchy sample is the illustration: the distribution is symmetric, the histogram on $[-10,10]$ looks single-peaked, and the sample kurtosis is 6,693 because a few draws are enormous. The same draws made the sample skewness 69.99. The coefficient is then a warning about the moments, not a description of a skew that the population has. {{cite:nist_skewness2002}} (§1.3.5.11, “Examples”)

Dodge’s grouped example makes the same ratio from class frequencies. Seventy-five bakeries, daily turnover grouped in intervals of width 20, gave a fourth-moment total $281{,}020{,}067.84$, a mean of 290.60, and a standard deviation of 33.88. The coefficient, as Dodge rounds it, is 2.84,

$$
\frac{(1/75)\cdot 281020067.84}{(33.88)^4}\approx 2.84,
$$


below 3, so the grouped distribution was called platykurtic. The arithmetic uses class centres. Changing the grouping changes the coefficient. {{cite:dodge2008}} (pp. 91–92)

## Worked example

For the sample $1,2,3,4,5$ the mean is 3 and the deviations are $-2,-1,0,1,2$. With divisor $n=5$,

$$
m_2=\frac{4+1+0+1+4}{5}=2,\qquad m_4=\frac{16+1+0+1+16}{5}=6.8,
$$


and the moment kurtosis is $6.8/2^2=1.7$. The excess is $1.7-3=-1.3$. The five points have no outlier, and the coefficient sits below the normal value.

For $1,1,1,1,6$ the mean is 2 and the deviations are $-1,-1,-1,-1,4$. Then $m_2=20/5=4$ and $m_4=260/5=52$, so the kurtosis is $52/4^2=3.25$ and the excess is $0.25$. One large observation is enough to push this sample above 3. Both calculations use the divisor $N$ inside $m_2$. {{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Kurtosis”) {{cite:dodge2008}} (p. 91)

**Your turn.** For $0,0,0,0,0,6$, compute the mean, $m_2$, $m_4$, and the moment kurtosis with divisor $n$. State whether the coefficient is above or below the normal value 3.

::: {.callout-tip collapse="true" title="Answer"}
The mean is 1. The squared deviations sum to $5\cdot 1+25=30$, so $m_2=5$. The fourth powers sum to $5\cdot 1+625=630$, so $m_4=105$. The kurtosis is $105/5^2=4.2$, which is above 3.
:::

## Assumptions and limits

The population coefficient requires a finite fourth moment. A Cauchy distribution does not have one, which is why a Cauchy sample can report a kurtosis in the thousands without estimating a population $\beta_2$. The sample formula also needs a positive standard deviation. A sample in which every observation is equal makes the ratio undefined.

The divisor is part of the definition. Using $N-1$ in the standard deviation and $N$ in the fourth moment produces a different number. Software that prints “kurtosis” may be printing the excess. The handbook’s instruction is to check the convention before comparing a printed value with 3. Significant skewness or kurtosis is evidence against a normal model for a procedure that needs one. The next step is a transformation, such as a log or a square root for moderate right skew, or a different distributional model. The coefficient does not choose the model. {{cite:nist_skewness2002}} (§1.3.5.11, “Alternative Definition of Kurtosis” and “Dealing with Skewness and Kurtosis”)

## Connections

[Skewness](skewness.qmd) is the standardised third moment, zero for a symmetric law, and it is the companion shape summary. A [normal distribution](normal-distribution.qmd) is the benchmark $\beta_2=3$. [Fat tails](fat-tails.qmd) are the pattern a kurtosis above 3 is used to flag, with the Cauchy sample as the extreme in which the sample moments themselves break. A histogram remains the picture that shows whether a large coefficient is one outlier, a heavy tail, or a grouping artefact. The bakery calculation is a grouped fourth moment. The five-point calculations are the same moment on a list small enough to recompute by hand. {{cite:dodge2008}} (pp. 91–92) {{cite:nist_skewness2002}} (§1.3.5.11, “Examples”)
