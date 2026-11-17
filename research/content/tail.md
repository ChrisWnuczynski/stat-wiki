## Lead context
Most of a distribution can sit in a small central range while a thin remainder stretches far to one side or both. That remainder is the tail, and its probability is the quantity used for a percentile, a long-tailed histogram, or the chance of an extreme value.{{cite:openintro2019}} (Ch. 2, §2.1.3; Ch. 4, §4.1.3)

## Motivating example
Cumulative SAT scores are described by a normal model with mean 1,100 and standard deviation 200. The probability of a score of at least 1,190 is an upper-tail probability. The standardised cutoff is \((1190-1100)/200=0.45\), the area to the left of that point is 0.6736, and the upper tail is \(1-0.6736=0.3264\). The same picture, read from the left, is the proportion of takers below the cutoff.{{cite:openintro2019}} (Ch. 4, §4.1.3)

## Intuition
A tail probability is the share of the distribution beyond a cutoff. The lower tail is the share below the cutoff, and the upper tail is the share above it. On a histogram, a long tail is the direction in which the bars trail off. Data that trail off to the right are right-skewed and are said to have a long right tail. Data that trail off to the left have a long left tail. A symmetric histogram trails off in both directions together.{{cite:openintro2019}} (Ch. 2, §2.1.3){{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Skewness”)

## Definition
For a random variable \(X\) and a cutoff \(c\), the upper-tail probability is \(P(X>c)\) and the lower-tail probability is \(P(X\le c)\). When \(X\) is continuous these two probabilities add to 1. For a normal law the calculation is done on the standardised value \(z=(c-\mu)/\sigma\), and the lower tail at \(z\) is the area of the standard normal to the left of \(z\).{{cite:openintro2019}} (Ch. 4, §4.1.3) An exponential law with parameter \(\theta>0\) has an explicit upper tail: its distribution function is \(1-e^{-\theta x}\), so \(P(X>x)=e^{-\theta x}\) for \(x>0\).{{cite:dodge2008}} (p. 194)

A long tail in a sample is a shape, not yet a probability. It is the direction in which a histogram decays slowly. Negative skewness is the moment sign attached to a long left tail, and positive skewness to a long right tail.{{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Skewness”){{cite:openintro2019}} (Ch. 2, §2.1.3)

## Properties
Lower and upper tails at the same cutoff add to 1 for a continuous distribution. In the SAT example the lower tail 0.6736 and the upper tail 0.3264 add to 1. At the standard normal point \(z=1\), the lower tail is 0.8413447, about 0.841, so the upper tail is \(1-0.8413447=0.1586553\).{{cite:openintro2019}} (Ch. 4, §4.1.3) For a unit exponential the upper tail at \(x\) is \(e^{-x}\), which at \(x=0\) equals 1 and at \(x=4\) equals \(e^{-4}\approx 0.018316\). The exponential mean \(1/\theta\) is a different functional of the same distribution: it averages the whole curve, and the tail probability only asks about the region beyond \(x\).{{cite:dodge2008}} (p. 194)

## Statistical use
A tail probability answers questions such as the proportion of people below a score, or the chance a waiting time exceeds a limit. Draw the curve and shade the region before computing the standardised value. A histogram tail is used earlier, at the descriptive stage, to name skew and to notice a handful of extreme observations, such as interest rates above 20% when most of the rates are under 15%. High kurtosis is a numerical companion when the tails, rather than one-sided length, are the feature of interest.{{cite:openintro2019}} (Ch. 2, §2.1.3; Ch. 4, §4.1.3){{cite:nist_skewness2002}} (§1.3.5.11, heavy tails and kurtosis)

## Worked example
For the SAT model, a cutoff of 1,190 has
\[
z=\frac{1190-1100}{200}=0.45.
\]
The lower-tail area at this \(z\) is 0.6736, so the upper tail is 0.3264. For a unit exponential the upper tail at 2 is \(e^{-2}\approx 0.135335\), and the lower tail is \(1-e^{-2}\approx 0.864665\). The two calculations use different laws and different cutoffs. Both are tail probabilities.{{cite:openintro2019}} (Ch. 4, the normal calculation){{cite:dodge2008}} (p. 194)

**Your turn.** A standard normal lower tail at \(z=1\) is 0.8413447. What is the upper tail at the same point? Separately, what is the unit-exponential upper tail at 0?

::: {.callout-tip collapse="true" title="Answer"}
The normal upper tail is \(1-0.8413447=0.1586553\). The unit-exponential upper tail at 0 is \(e^{0}=1\).
:::

## Common misconceptions
The lower tail at a cutoff is the proportion below it, and the upper tail is the proportion above it. Quoting 0.6736 as the chance of exceeding 1,190 swaps those two regions. A long right tail on a histogram is a description of shape. It is not the numerical value of \(P(X>c)\) until a cutoff and a distribution, or an empirical proportion, have been chosen. Skewness and kurtosis also answer different questions: skewness signs a long tail on one side, and kurtosis compares the heaviness of the tails with a normal curve.{{cite:openintro2019}} (Ch. 2, §2.1.3; Ch. 4, §4.1.3){{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Skewness” and “Definition of Kurtosis”)

## Assumptions and limits
The normal tail areas above use a normal model with a stated mean and standard deviation. A different mean or standard deviation changes \(z\) and therefore the area. The exponential tail formula requires the exponential model and a positive cutoff on its scale. A sample histogram can show a long tail in a batch that is too small, or too contaminated by one point, for a tail probability from a named law to be a serious estimate. The empirical proportion beyond a cutoff remains well defined without that model.{{cite:openintro2019}} (Ch. 4, §4.1.3){{cite:dodge2008}} (p. 194)

## Connections
[Skewness](skewness.qmd) signs a long left or right tail, and [kurtosis](kurtosis.qmd) compares tail weight with the normal value 3. [Fat tails](fat-tails.qmd) is the case in which that weight exceeds the normal benchmark. [Exponential tails and the Gumbel law](exponential-tails-and-the-gumbel-law.qmd) describe the maximum when the upper tail is exponential. [Power-law tails and the Fréchet law](power-law-tails-and-the-frechet-law.qmd) describe the maximum when the upper tail decays as a power. A [histogram](histogram.qmd) is where a long tail is seen before any of those models is chosen.

## History
Reading an extreme region of a fitted curve as a proportion is the ordinary use of a normal table or of software that returns a tail area. The exponential distribution contributes an explicit tail, \(e^{-\theta x}\), from its distribution function \(1-e^{-\theta x}\). Descriptive language for a long tail on a histogram is older as a habit of plotting, and the moment signs for a long left or right tail are the skewness convention attached to that picture.{{cite:dodge2008}} (p. 194){{cite:openintro2019}} (Ch. 2, §2.1.3; Ch. 4, §4.1.3){{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Skewness”)
