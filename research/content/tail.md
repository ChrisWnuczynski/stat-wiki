## Lead context

Most of a distribution can sit in a small central range while a thin remainder stretches far to one side or both. That remainder is the tail, and its probability is the quantity used for a percentile, a long-tailed histogram, or the chance of an extreme value.{{cite:openintro2019}} (Ch. 2, §2.1.3; Ch. 4, §4.1.3)

## Motivating example

Cumulative SAT scores are described by a normal model with mean 1,100 and standard deviation 200. The probability of a score of at least 1,190 is an upper-tail probability. The standardised cutoff is $(1190-1100)/200=0.45$, the area to the left of that point is 0.6736, and the upper tail is $1-0.6736=0.3264$. The same picture, read from the left, is the proportion of takers below the cutoff. The calculation starts by drawing the curve and shading the region above 1,190, then finding the $z$-score.{{cite:openintro2019}} (Ch. 4, §4.1.4)

## Definition

For a random variable $X$ and a cutoff $c$, the upper-tail probability is $P(X>c)$ and the lower-tail probability is $P(X\le c)$. When $X$ is continuous these two probabilities add to 1. For a normal law the calculation is done on the standardised value $z=(c-\mu)/\sigma$, and the lower tail at $z$ is the area of the standard normal to the left of $z$. At $z=1$, that lower tail is 0.8413447.{{cite:openintro2019}} (Ch. 4, §4.1.3) An exponential law with parameter $\theta>0$ has an explicit upper tail. Its distribution function is $1-e^{-\theta x}$, so $P(X>x)=e^{-\theta x}$ for $x>0$. The mean is $1/\theta$.{{cite:dodge2008}} (p. 194)

A long tail in a sample is a shape, not yet a probability. It is the direction in which a histogram decays slowly. Data that trail off to the right, and have a longer right tail, are right-skewed. Data that trail off to the left have a long left tail and are left-skewed. A symmetric histogram trails off in both directions together. Negative values of the skewness coefficient indicate data skewed left, meaning the left tail is long relative to the right tail. Positive values indicate data skewed right.{{cite:openintro2019}} (Ch. 2, §2.1.3){{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Skewness”)

## Properties

Lower and upper tails at the same cutoff add to 1 for a continuous distribution. In the SAT example the lower tail 0.6736 and the upper tail 0.3264 add to 1. At the standard normal point $z=1$, the lower tail is 0.8413447, so the upper tail is $1-0.8413447=0.1586553$.{{cite:openintro2019}} (Ch. 4, §4.1.3 and §4.1.4) For a unit exponential the upper tail at $x$ is $e^{-x}$, which at $x=0$ equals 1 and at $x=4$ equals $e^{-4}\approx 0.018316$. The exponential mean $1/\theta$ is a different functional of the same distribution. It averages the whole curve, and the tail probability only asks about the region beyond $x$.{{cite:dodge2008}} (p. 194)

Kurtosis compares tail weight with a normal curve. Data with high kurtosis tend to have heavy tails, or outliers. Data with low kurtosis tend to have light tails. The kurtosis of a standard normal distribution is three, which is why an excess kurtosis subtracts 3. Skewness and kurtosis answer different questions. Skewness signs a long tail on one side. Kurtosis compares the heaviness of the tails with the normal benchmark, without saying which side is longer.{{cite:nist_skewness2002}} (§1.3.5.11, “Definition of Skewness” and “Definition of Kurtosis”)

## Statistical use

A tail probability answers questions such as the proportion of people below a score, or the chance a waiting time exceeds a limit. Draw the curve and shade the region before computing the standardised value. A histogram tail is used earlier, at the descriptive stage, to name skew and to notice a handful of extreme observations. In the loan-rate histogram most of the mass sits under 15 percent, and only a handful of rates sit above 20 percent, which is the long right tail of that batch.{{cite:openintro2019}} (Ch. 2, §2.1.3; Ch. 4, §4.1.4)

Failure times in a reliability study cannot be negative, and a measurement with a lower bound of that kind is a standard setting for right skew. The sign of a skewness coefficient can also be pulled by a second mode, so a long tail and a second hump are not the same diagnosis. High kurtosis is the numerical companion when the tails, rather than one-sided length, are the feature of interest.{{cite:nist_skewness2002}} (§1.3.5.11){{cite:openintro2019}} (Ch. 2, §2.1.3)

The normal tail areas above use a normal model with a stated mean and standard deviation. A different mean or standard deviation changes $z$ and therefore the area. The exponential tail formula requires the exponential model and a positive cutoff on its scale. A sample histogram can show a long tail in a batch that is too small, or too influenced by one point, for a tail probability from a named law to be a serious estimate. The empirical proportion beyond a cutoff remains well defined without that model.{{cite:openintro2019}} (Ch. 4, §4.1.4){{cite:dodge2008}} (p. 194)

## Worked example

For the SAT model, a cutoff of 1,190 has

$$
z=\frac{1190-1100}{200}=0.45.
$$


The lower-tail area at this $z$ is 0.6736, so the upper tail is 0.3264. For a unit exponential the upper tail at 2 is $e^{-2}\approx 0.135335$, and the lower tail is $1-e^{-2}\approx 0.864665$. The two calculations use different laws and different cutoffs. Both are tail probabilities.{{cite:openintro2019}} (Ch. 4, §4.1.4){{cite:dodge2008}} (p. 194)

**Your turn.** A standard normal lower tail at $z=1$ is 0.8413447. What is the upper tail at the same point? Separately, what is the unit-exponential upper tail at 0?

::: {.callout-tip collapse="true" title="Answer"}
The normal upper tail is $1-0.8413447=0.1586553$. The unit-exponential upper tail at 0 is $e^{0}=1$.
:::

## Common misconceptions

The lower tail at a cutoff is the proportion below it, and the upper tail is the proportion above it. Quoting 0.6736 as the chance of exceeding 1,190 swaps those two regions. A long right tail on a histogram is a description of shape. It is not the numerical value of $P(X>c)$ until a cutoff and a distribution, or an empirical proportion, have been chosen.{{cite:openintro2019}} (Ch. 2, §2.1.3; Ch. 4, §4.1.4)

Skewness and kurtosis also answer different questions. Negative skewness signs a long left tail, and positive skewness a long right tail. Kurtosis compares the heaviness of the tails with a normal curve, whose kurtosis is 3. A symmetric heavy-tailed distribution can have skewness near zero and kurtosis well above 3.{{cite:nist_skewness2002}} (§1.3.5.11)

## History

Reading an extreme region of a fitted curve as a proportion is the ordinary use of a normal table, of a calculator, or of software that returns a tail area. The SAT calculation is the usual form of that habit: standardise, read the lower tail, and subtract from 1 for the upper tail. The exponential distribution contributes an explicit tail, $e^{-\theta x}$, from its distribution function $1-e^{-\theta x}$, and it is the continuous law used for lifetimes and other events in time.{{cite:dodge2008}} (p. 194){{cite:openintro2019}} (Ch. 4, §4.1.3 and §4.1.4)

Descriptive language for a long tail on a histogram is the ordinary reading of a binned plot. The moment signs for a long left or right tail are the skewness convention attached to that picture, and the comparison of tail weight with the normal value 3 is the kurtosis convention.{{cite:nist_skewness2002}} (§1.3.5.11){{cite:openintro2019}} (Ch. 2, §2.1.3)

## Connections

[Skewness](skewness.qmd) signs a long left or right tail, and [kurtosis](kurtosis.qmd) compares tail weight with the normal value 3. [Fat tails](fat-tails.qmd) is the case in which that weight exceeds the normal benchmark. [Exponential tails and the Gumbel law](exponential-tails-and-the-gumbel-law.qmd) describe the maximum when the upper tail is exponential. [Power-law tails and the Fréchet law](power-law-tails-and-the-frechet-law.qmd) describe the maximum when the upper tail decays as a power. A [histogram](histogram.qmd) is where a long tail is seen before any of those models is chosen.
