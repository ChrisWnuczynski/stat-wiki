

## Lead context

Two samples can share a mean and a standard deviation and still differ in how much probability sits in the shoulders and the extremes. Kurtosis is the moment summary that compares that fourth-power balance with a normal curve.{{cite:nist_skewness2002}} (§1.3.5.11, “Skewness and Kurtosis”)

## Motivating example

A normal sample of 10,000 draws had moment kurtosis 2.96, close to the normal value 3, and skewness 0.03. A double-exponential sample of the same size, symmetric and more peaked, with heavier tails, had skewness 0.06 and kurtosis 5.9. A Cauchy sample, restricted in the histogram to the interval from \(-10\) to \(10\), still produced a moment kurtosis of 6,693, because the unrestricted draws ran from about \(-29{,}000\) to about \(89{,}000\). The pictures and the coefficients are describing the same contrast.{{cite:nist_skewness2002}} (§1.3.5.11, “Examples”)

## Intuition

The fourth power makes a deviation of 4 count as much as 256 deviations of 1. Dividing by the fourth power of the standard deviation removes the units, so a change of scale does not change the coefficient. A value above the normal benchmark means the fourth-power mass is more extreme than a normal curve with the same variance. A value below it means the observations are more tightly confined. A uniform distribution is the light-tailed extreme of that comparison.{{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Kurtosis”){{cite:dodge2008}} (p. 91)

## Definition

For a random variable with mean \(\mu\) and positive standard deviation \(\sigma\), the moment coefficient is
\[
\beta_2=\frac{\mu_4}{\sigma^4},\qquad \mu_4=\mathbb E[(X-\mu)^4].
\]
A normal law has \(\beta_2=3\). The excess form is \(\gamma_2=\mu_4/\sigma^4-3\), so the normal value is zero.{{cite:dodge2008}} (pp. 91, 343) For observations \(Y_1,\ldots,Y_N\) with mean \(\bar Y\), the sample coefficient used with the normal benchmark of 3 is
\[
\frac{\sum_{i=1}^N(Y_i-\bar Y)^4/N}{s^4},
\]
where \(s\) is the standard deviation computed with \(N\) in the denominator, not \(N-1\). Subtracting 3 gives the excess. The two conventions name different numbers, and a report has to say which one was computed.{{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Kurtosis” and “Alternative Definition of Kurtosis”)

Read a histogram before treating the coefficient as a description of shape. High kurtosis points toward heavy tails or outliers, and low kurtosis toward light tails. A Weibull sample with shape 1.5 had skewness 1.08 and kurtosis 4.46, a moderate departure on both scores. When the coefficient and the histogram agree that the normal model is a poor description, a transformation or a different distributional model is the next modelling choice. The Cauchy calculation shows why the coefficient alone can be a poor summary: a few extreme draws made the skewness 69.99 and the kurtosis 6,693 even though the distribution is symmetric.{{cite:nist_skewness2002}} (§1.3.5.11, “Examples” and “Dealing with Skewness and Kurtosis”)

A kurtosis of 3 is the normal benchmark, and a kurtosis of 0 is the benchmark only for the excess convention. Software that prints “kurtosis” may be printing either number.{{cite:nist_skewness2002}} (§1.3.5.11, “Alternative Definition of Kurtosis”) A large positive coefficient does not by itself name the distribution. The double-exponential sample at 5.9 and the Cauchy sample at 6,693 are both above 3, and they are not the same shape. A symmetric law can have a wild sample coefficient when the tails are heavy enough to wreck the sample moments.{{cite:nist_skewness2002}} (§1.3.5.11, “Examples”)

Pearson’s papers of 1894 and 1895 treated departures from the normal curve through moments of order 3 and 4. Gram and Thiele had already studied the symmetry of frequency curves before 1890. The coefficient \(\beta_2=\mu_4/\sigma^4\), with the normal value 3, is the fourth-moment piece of that programme, and the excess \(\gamma_2=\beta_2-3\) is the later shift that puts the normal value at zero.{{cite:dodge2008}} (pp. 91, 343–344)

## Properties

A curve with \(\beta_2<3\) is called platykurtic, and one with \(\beta_2>3\) is called leptokurtic, relative to the normal curve.{{cite:dodge2008}} (p. 91) For a normal law the centred moments satisfy the recurrence \(\mu_s=(s-1)\sigma^2\mu_{s-2}\). With \(\mu_0=1\) and \(\mu_1=0\) this gives \(\mu_2=\sigma^2\) and \(\mu_4=3\sigma^4\), which is why the ratio equals 3.{{cite:dodge2008}} (pp. 91–92) Positive excess is the numerical sign attached to a heavy-tailed or outlier-prone sample, and negative excess is the sign attached to a light-tailed sample.{{cite:nist_skewness2002}} (§1.3.5.11, “Alternative Definition of Kurtosis”)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The normal recurrence with \(s=2\) gives \(\mu_2=1\cdot\sigma^2\cdot\mu_0=\sigma^2\). The centred third moment is \(\mu_3=2\sigma^2\mu_1=0\). The fourth moment is \(\mu_4=3\sigma^2\mu_2=3\sigma^4\). Dividing by \(\sigma^4\) leaves 3. The same identity is the reason an excess coefficient subtracts 3 rather than some other constant.{{cite:dodge2008}} (pp. 91–92)
:::
:::

## Worked example

For \(1,2,3,4,5\) the mean is 3 and the deviations are \(-2,-1,0,1,2\). Then
\[
m_2=\frac{4+1+0+1+4}{5}=2,\qquad m_4=\frac{16+1+0+1+16}{5}=6.8,
\]
and the moment kurtosis is \(6.8/2^2=1.7\). The excess is \(1.7-3=-1.3\). The five points have no outlier, and the coefficient sits below the normal value.

For \(1,1,1,1,6\) the mean is 2 and the deviations are \(-1,-1,-1,-1,4\). Then \(m_2=20/5=4\) and \(m_4=260/5=52\), so the kurtosis is \(52/4^2=3.25\) and the excess is \(0.25\). One large observation is enough to push this sample above 3. Both calculations use the divisor \(N\) inside \(m_2\).{{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Kurtosis”){{cite:dodge2008}} (p. 91)

**Your turn.** For \(0,0,0,0,0,6\), compute the mean, \(m_2\), \(m_4\) and the moment kurtosis with divisor \(n\). State whether the coefficient is above or below the normal value 3.

::: {.callout-tip collapse="true" title="Answer"}
The mean is 1. The squared deviations sum to \(5\cdot 1+25=30\), so \(m_2=5\). The fourth powers sum to \(5\cdot 1+625=630\), so \(m_4=105\). The kurtosis is \(105/5^2=4.2\), which is above 3.
:::

## Assumptions and limits

The coefficient needs a positive standard deviation. The population moment \(\mu_4\) has to exist before \(\beta_2\) is a property of the law rather than only of a sample. A sample from a Cauchy law still produces a finite coefficient whenever the observed standard deviation is positive, and that coefficient can be driven by a handful of draws, as in the sample whose extremes were about \(-29{,}000\) and \(89{,}000\). Comparing coefficients also requires a shared convention for the divisor and for whether 3 has been subtracted.{{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Kurtosis” and “Examples”){{cite:dodge2008}} (p. 343)

## Connections

[Skewness](skewness.qmd) is the third-moment companion, and a [histogram](histogram.qmd) shows the shape that one coefficient compresses. [Variance](variance.qmd) fixes the scale that kurtosis then compares. A [normal quantile plot](normal-quantile-plot.qmd) is the graphical check when the question is whether a normal model is adequate. Tails that stay heavy in the sense of a power law are treated with [power-law tails](power-law-tails-and-the-frechet-law.qmd).
