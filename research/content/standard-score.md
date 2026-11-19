## Lead context

Two scores on different tests are not comparable until each is written as a distance from its own mean, in units of its own standard deviation. That rescaled distance is the standard score.

It is also called a $z$-score. It is the number of standard deviations an observation falls above or below the mean. The device is used most often for nearly normal observations, and it may be used with any distribution that has a mean and a standard deviation.{{cite:openintro2019}} (Ch. 4, §4.1.2)

## Motivating example

Ann scored 1300 on the SAT and Tom scored 24 on the ACT. The SAT scores have mean 1100 and standard deviation 200. The ACT scores have mean 21 and standard deviation 6. The raw numbers 1300 and 24 cannot be lined up. Ann is one standard deviation above the SAT mean, because $1100+200=1300$. Tom is half a standard deviation above the ACT mean, because $21+0.5\times 6=24$. On that common scale Ann's score sits further above her reference group than Tom's does.{{cite:openintro2019}} (Ch. 4, §4.1.2)

## Definition

If $x$ is an observation from a distribution with mean $\mu$ and standard deviation $\sigma$, the standard score is

$$
z=\frac{x-\mu}{\sigma}.
$$


An observation one standard deviation above the mean has $z=1$. An observation 1.5 standard deviations below the mean has $z=-1.5$. An observation equal to the mean has $z=0$. Observations above the mean have positive scores, and observations below the mean have negative scores. For a sample with mean $\bar x$ and sample standard deviation $s$, the same ratio with $\bar x$ and $s$ in place of $\mu$ and $\sigma$ puts the sample on a scale with mean 0 and standard deviation 1.{{cite:openintro2019}} (Ch. 4, §4.1.2)

The population standard deviation in the denominator is the positive square root of $\mathbb E[(X-\mathbb EX)^2]$. The sample version uses

$$
s=\sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar x)^2}.
$$


Dividing by $s$ removes the unit of measurement. A length in millimetres and a score in test points become pure numbers of standard deviations.{{cite:dodge2008}} (p. 506){{cite:nist_handbook2002}} (§1.3.5.6, standard deviation)

## Properties

The map $x\mapsto (x-\mu)/\sigma$ is linear. It sends $\mu$ to 0 and sends $\mu+\sigma$ to 1. Adding a constant to every observation adds the same constant to the mean and leaves the standard deviation unchanged, so the standard scores are unchanged. Multiplying every observation by a positive constant multiplies the mean and the standard deviation by that constant, and the ratio is again unchanged. The absolute value $|z|$ ranks how unusual an observation is relative to its own mean and spread, when the comparison is between distributions of similar shape. If $|z_1|>|z_2|$, the first observation is further from its mean, in standard-deviation units, than the second is from its mean. The comparison is especially clear when the distributions are symmetric.{{cite:openintro2019}} (Ch. 4, §4.1.2)

For a normal distribution the standard score is the argument of the standard normal curve. Tail areas are read from that curve after the observation has been converted. The conversion does not require the original observation to have been normal. What the normal table then returns is a normal probability, which matches the data only to the extent that the normal model matches them. A long-tailed sample can have a standard deviation so inflated by extremes that a typical observation receives a $z$-score near zero even though it is unusual on another scale. The median absolute deviation is the scale to consider in that case.{{cite:openintro2019}} (Ch. 4, §4.1.2, §4.1.3){{cite:nist_handbook2002}} (§1.3.5.6, Cauchy example)

Before ridge regression, each predictor is divided by its estimated standard deviation, the square root of the average squared deviation from its mean, so that every standardised predictor has standard deviation one. A change of unit, such as measuring income in dollars rather than in thousands of dollars, then does not change the fitted contribution of that predictor. The coefficient is on a scale the penalty can compare across columns.{{cite:james_islr2013}} (p. 217, §6.2, equation (6.6))

## Worked example

Ann's SAT score gives

$$
z_{\text{Ann}}=\frac{1300-1100}{200}=\frac{200}{200}=1.
$$


Tom's ACT score gives

$$
z_{\text{Tom}}=\frac{24-21}{6}=\frac{3}{6}=0.5.
$$


Ann is one standard deviation above her mean. Tom is half a standard deviation above his. On the three numbers 2, 4 and 6 the sample mean is 4, the squared deviations from 4 are 4, 0 and 4, and the sample standard deviation is $\sqrt{8/2}=2$. The standard score of 6 is $(6-4)/2=1$, and the standard score of 2 is $(2-4)/2=-1$.{{cite:openintro2019}} (Ch. 4, §4.1.2){{cite:nist_handbook2002}} (§1.3.5.6, sample standard deviation)

**Your turn.** A test has mean 78 and standard deviation 6. What is the standard score of a mark of 90?

::: {.callout-tip collapse="true" title="Answer"}
The score is $(90-78)/6=12/6=2$. The mark is two standard deviations above the mean.
:::

## Assumptions and limits

The formula needs a positive standard deviation. A batch in which every observation equals the mean has $s=0$, and the ratio is undefined. The score describes distance from the mean in units of spread. It does not describe distance from the median, and it does not repair a mean that has been pulled by a single wild point. Two observations with the same $z$-score can sit in distributions of very different shape. The normal tail area attached to a $z$-score is a statement about a normal model. It is not a statement about every histogram that happens to have been standardised. A comparison of $|z|$ across two tests assumes that a standard deviation is a fair unit in both. If one test has a heavy tail and the other does not, the more unusual observation on a median scale need not be the one with the larger $|z|$.{{cite:openintro2019}} (Ch. 4, §4.1.2){{cite:nist_handbook2002}} (§1.3.5.6)

## History

The standard deviation that sits in the denominator was named by Pearson in a lecture to the Royal Society in 1893, used again in his 1894 paper on asymmetrical frequency curves, and written $\sigma$. Gosset later kept the sample standard deviation distinct from that population quantity. The ratio of a deviation to $\sigma$ is the reduction of a measurement to that scale. The teaching form $z=(x-\mu)/\sigma$, with the SAT and ACT as the numerical comparison, is the form in which a first course now introduces the same ratio, before using it to read a normal tail.{{cite:dodge2008}} (p. 506){{cite:openintro2019}} (Ch. 4, §4.1.2, §4.1.3)
