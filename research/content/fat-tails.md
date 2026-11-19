## Lead context

A normal sample keeps most of its observations within a few standard deviations of the mean. A fat-tailed sample does not: a few observations sit so far out that they dominate fourth-moment and variance calculations. The comparison with the normal curve is the content of the word.{{cite:nist_skewness2002}} (§1.3.5.11, “Skewness and Kurtosis”)

## Motivating example

Three samples of 10,000 draws show the contrast. A normal sample had kurtosis 2.96, close to the normal value 3, and a range of 7.87 against a standard deviation of 0.997. A double-exponential sample had kurtosis 5.9, standard deviation 1.417 and range 17.556. A Cauchy sample had kurtosis 6,693, standard deviation 998.389 and range 118,953.6, while its median absolute deviation stayed at 1.16. The centre of the Cauchy sample is ordinary. The tails are what make the moment summaries enormous.{{cite:nist_skewness2002}} (§1.3.5.11, “Examples”){{cite:nist_handbook2002}} (§1.3.5.6, the normal, double-exponential and Cauchy samples)

## Intuition

The fourth power of a deviation grows much faster than the deviation itself. Kurtosis divides that fourth-power average by the fourth power of the standard deviation, so the comparison is free of units. Above 3, the sample has a heavier fourth-power tail than a normal law. A survival probability makes the same point without moments: the chance of passing a high threshold stays visible for a fat tail and collapses for a thin one. A histogram that trails off in one direction is the picture of a long tail.{{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Kurtosis”){{cite:openintro2019}} (Ch. 2, §2.1.3)

## Definition

Relative to a normal distribution, a sample is heavy-tailed when its moment kurtosis exceeds 3, and light-tailed when the coefficient is smaller. The coefficient is

$$
\frac{\sum_{i=1}^N(Y_i-\bar Y)^4/N}{s^4},
$$


with $s$ computed using $N$ in the denominator. Subtracting 3 gives the excess, which is positive for the heavy-tailed side of the same comparison. A uniform distribution is the light-tailed extreme named with that definition.{{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Kurtosis” and “Alternative Definition of Kurtosis”)

An exponential law with parameter $\theta>0$ has distribution function $1-e^{-\theta x}$ on the positive line, so its upper-tail probability is $e^{-\theta x}$. Its mean is $1/\theta$ and its variance is $1/\theta^2$. Those two moments exist. The fourth-moment calculation below gives kurtosis 9 for every $\theta>0$, so the exponential tail is heavy relative to a normal curve and still has a finite variance.{{cite:dodge2008}} (p. 194)

## Statistical use

Use kurtosis together with a histogram. A coefficient a little above 3, such as the double-exponential sample at 5.9, and a coefficient in the thousands, such as the Cauchy sample, are both “heavy” by the normal benchmark and they do not describe the same tail. When the standard deviation has been wrecked by extremes, report a median absolute deviation or an interquartile range beside it. A long right tail on a histogram is a reason to look at a transformation or at a distribution supported on the positive line, of which the exponential is one example.{{cite:nist_skewness2002}} (§1.3.5.11, “Examples” and “Dealing with Skewness and Kurtosis”){{cite:nist_handbook2002}} (§1.3.5.6){{cite:openintro2019}} (Ch. 2, §2.1.3)

For the unit exponential, $\theta=1$, the raw moments are $\mathbb E[X^k]=k!$. Then

$$
\mathbb E[(X-1)^4]=24-4\cdot 6+6\cdot 2-4\cdot 1+1=9,
$$


and dividing by $\sigma^4=1$ leaves kurtosis 9, which is an excess of 6. The survival at 4 is $e^{-4}\approx 0.018316$. A normal law, by the moment recurrence, has kurtosis exactly 3. The exponential is therefore fat-tailed relative to the normal by the kurtosis test, and it still has a finite variance.{{cite:dodge2008}} (pp. 91–92, 194){{cite:nist_skewness2002}} (§1.3.5.11, normal value 3)

The Cauchy sample is a more extreme case of the same idea. Collecting further Cauchy draws does not settle the standard deviation, and the median absolute deviation remains the stable description of the central spread.{{cite:nist_handbook2002}} (§1.3.5.6, “Cauchy Distribution”)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The exponential density is the derivative of $1-e^{-\theta x}$, namely $\theta e^{-\theta x}$ for $x>0$. Integration by parts gives $\mathbb E[X^k]=k/\theta\cdot\mathbb E[X^{k-1}]$, hence $\mathbb E[X^k]=k!/\theta^k$. At $\theta=1$ the binomial expansion of $\mathbb E[(X-1)^4]$ is the alternating sum of raw moments written above, which equals 9. If $Y$ is that unit exponential and $X=Y/\theta$, then $\mathbb E[(X-1/\theta)^4]=\mathbb E[(Y-1)^4]/\theta^4=9/\theta^4$ and $\sigma^4=1/\theta^4$, so the ratio is 9 for every $\theta>0$. The variance formula $\mathbb E[X^2]-(\mathbb E[X])^2=2-1=1$ is the $\theta=1$ case of $1/\theta^2$.{{cite:dodge2008}} (p. 194)
:::
:::

## Worked example

The five numbers 1, 2, 3, 4, 5 have mean 3, second central moment $m_2=2$ and fourth central moment $m_4=6.8$, so their moment kurtosis is $6.8/4=1.7$, below the normal value. The five numbers 1, 1, 1, 1, 6 have mean 2, $m_2=4$ and $m_4=52$, so their kurtosis is $52/16=3.25$, above 3. The single value 6 is the entire difference between a light-tailed and a heavy-tailed coefficient on these two samples of size 5.

For a unit exponential, the tail probability past 4 is $e^{-4}\approx 0.018316$, and the kurtosis of the law is 9. The sample coefficient 3.25 and the exponential coefficient 9 are both on the heavy side of 3, at very different distances.{{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Kurtosis”){{cite:dodge2008}} (p. 194)

**Your turn.** For a unit exponential, compute the survival probability past 1, and the kurtosis excess over the normal value 3.

::: {.callout-tip collapse="true" title="Answer"}
The survival past 1 is $e^{-1}\approx 0.367879$. The kurtosis is 9, so the excess is $9-3=6$.
:::

## Common misconceptions

A kurtosis above 3 means heavier tails than a normal curve. It does not mean that the variance is infinite. The exponential law has kurtosis 9 and variance 1. A sample kurtosis in the thousands, as in the Cauchy sample of 6,693, is compatible with a symmetric law. The sample moments are then a poor description of the centre, which is why the median absolute deviation of that sample stayed near 1.16 while the standard deviation did not.{{cite:nist_handbook2002}} (§1.3.5.6, “Cauchy Distribution”){{cite:dodge2008}} (p. 194){{cite:nist_skewness2002}} (§1.3.5.11, “Examples”)

The kurtosis comparison needs a finite fourth moment and a positive standard deviation. A sample can still produce a number when the population moment does not exist, and that number can be dominated by a few draws. The exponential tail formula $e^{-\theta x}$ is the survival of that specific law, not a description of every right-skewed histogram. A long tail in a plot can be skewness, a heavy two-sided tail, or a single outlier, and the coefficient does not by itself decide which.{{cite:nist_skewness2002}} (§1.3.5.11, “Examples”){{cite:openintro2019}} (Ch. 2, §2.1.3)

## Connections

[Kurtosis](kurtosis.qmd) is the moment comparison used above, and [skewness](skewness.qmd) describes a long tail on one side. [Power-law tails and the Fréchet law](power-law-tails-and-the-frechet-law.qmd) treat a much heavier upper tail, of the form that can leave the variance infinite, through the scaling of the sample maximum. [Exponential tails and the Gumbel law](exponential-tails-and-the-gumbel-law.qmd) treat the maximum of exponential observations, whose survival is the $e^{-\theta x}$ used here. A [histogram](histogram.qmd) is the display on which either tail is first seen. The [Pareto distribution](pareto-distribution.qmd) is the named family with a power-law tail.

The normal value 3 for the fourth-moment ratio goes back to the moment description of the normal curve used by Pearson, with the recurrence that produces $\mu_4=3\sigma^4$. Calling a sample heavy-tailed when its kurtosis exceeds that benchmark, and light-tailed when it falls short, is the descriptive use of the same coefficient. The exponential distribution, already the continuous analogue of the geometric law, supplies a calculated case with kurtosis 9 and a finite variance.{{cite:dodge2008}} (pp. 91–92, 194){{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Kurtosis”)
