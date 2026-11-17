## Motivating example
A laboratory wants its reported mean to have a confidence interval no more than four measurement units wide. Planning starts with the half-width, $E=2$, and a plausible population standard deviation, say $\sigma=10$. A confidence level alone does not determine a sample size: the spread and the desired precision matter as well. For independent normal measurements with known spread, the interval width can be calculated before any observations arrive.{{cite:nist_handbook2002}} (§7.2.2.2, “Sample sizes required”)

## Intuition
An average of independent measurements has standard error $\sigma/\sqrt n$. Increasing $n$ reduces noise because positive and negative errors can cancel, but the square root makes precision expensive. Dividing a margin of error by two requires multiplying the continuous sample-size requirement by four. Increasing confidence also costs observations, because a larger normal quantile multiplies the standard error.{{cite:openintro2019}} (§5.2, “Confidence intervals”)

The requirement is a property of a procedure under a sampling model. It does not guarantee that the error of the particular future sample mean will be smaller than the chosen half-width. Under the exact normal model, the planned interval misses the fixed mean with probability $\alpha$, even when its width is completely predetermined.{{cite:nist_handbook2002}} (§1.3.5.2, confidence coefficient)

## Properties — Deriving and rounding the requirement
Let $z=z_{1-\alpha/2}$ denote the normal quantile. Solving $z\sigma/\sqrt n\le E$ gives
$$n_{\min}=\left\lceil z^2\sigma^2/E^2\right\rceil.$$
The ceiling is necessary: rounding to the nearest integer can violate the width requirement. For the laboratory values and $z=1.96$, the continuous answer is $96.04$. At $n=96$ the half-width is approximately $2.0004$; at $n=97$ it is approximately $1.9901$. Only the second meets the target.{{cite:nist_handbook2002}} (§7.2.2.2, known-standard-deviation formula)

A planned standard deviation is often an estimate from a pilot study. Substituting it produces a planning calculation, not a known-$\sigma$ theorem. If the eventual interval uses a sample standard deviation and a Student quantile, its width is random. One can iterate a Student-quantile approximation using a plausible spread, but guaranteeing a specified probability that the width is small requires an additional assurance calculation.

## Statistical use — Planning a poll
For a Bernoulli response the variance is $p(1-p)$. The identity
$$p(1-p)=\frac14-(p-\tfrac12)^2\le\frac14$$
gives a conservative variance bound when the proportion is unknown. Substituting that bound into the normal approximation gives $n\ge z^2/(4E^2)$. At $95\%$ confidence and $E=0.03$, use of $z=1.96$ gives $1067.1111\ldots$, hence $1068$. A margin of five percentage points instead gives $384.16$, hence $385$. These are approximate normal-interval planning rules. The variance bound is exact; the normal coverage approximation is a separate step.{{cite:openintro2019}} (§6.1, “Inference for a single proportion”, sample-size planning)

The participants must be sampled in a way that supports the standard error. A convenience sample does not become representative merely by becoming large. Clustering and unequal survey weights can increase variance relative to simple independent sampling. Nonresponse can introduce bias as well as reducing the achieved sample size. Planning should distinguish the number invited from the number expected to supply usable responses.{{cite:openintro2019}} (§5.1, “Point estimates and sampling variability”, sampling error and bias)

## Worked example — Precision and expected response
Suppose a study needs the conservative $385$ usable responses for a five-percentage-point margin, and each invitation independently produces a response with probability $0.8$. Inviting $\lceil385/0.8\rceil=482$ people gives an expected $385.6$ responses. This does not guarantee $385$: the response count remains random. The probability of reaching at least $385$ is approximately $0.5543$ under this binomial response model. An invitation target based only on the expected count is therefore quite different from an assurance target.

**Your turn.** With known $\sigma=6$, normal critical value $1.96$, and target half-width $1.5$, compute the minimum sample size. What is the continuous requirement if the target becomes $0.75$?

::: {.callout-tip collapse="true" title="Answer"}
The first requirement is $(1.96\times6/1.5)^2=61.4656$, so use $62$ measurements. Halving the half-width multiplies that continuous requirement by four, giving $245.8624$ and integer requirement $246$.
:::

## Assumptions and limits — Finite populations
Population size matters when the design samples without replacement from a finite population and the sampling fraction is appreciable. For $N>1$ and $1\le n\le N$, if the population has $N$ elements and variance $\sigma_N^2$ defined with divisor $N$, the simple-random-sample mean has variance
$$\operatorname{Var}(\bar X)=\frac{\sigma_N^2}{n}\frac{N-n}{N-1}.$$
Solving the corresponding normal half-width inequality gives
$$n\ge\frac{z^2\sigma_N^2N}{E^2(N-1)+z^2\sigma_N^2}.$$
The correction tends to the independent-sampling answer when $N$ is large relative to $n$. Sampling all $N$ elements removes sampling variation for that finite-population mean, while measurement errors and missing responses can still matter. The independent approximation is reasonable only after checking the design and sampling fraction.{{cite:openintro2019}} (§6.1, independence and the ten-percent condition)

For a direct derivation of the finite-population factor, centre the $N$ population values so their sum is zero. Two distinct ordered draws then have covariance $-\sigma_N^2/(N-1)$, because the sum of cross-products over distinct pairs is minus the sum of squared centred values. Averaging $n$ draws gives variance $n^{-2}\{n\sigma_N^2-n(n-1)\sigma_N^2/(N-1)\}$, which simplifies to the stated expression. This negative covariance is the mathematical contribution of sampling without replacement.
