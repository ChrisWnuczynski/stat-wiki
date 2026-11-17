## Motivating example
Suppose a small sample gives a median, but the familiar standard-error formula for a sample mean does not describe its uncertainty. Repeating the original sampling experiment would reveal how much the median changes, yet that experiment may be too expensive. The bootstrap replaces the unknown population distribution by an estimate from the data, repeatedly samples from that estimate, and recomputes the same median. The resulting variation is a model-based approximation to repeated sampling, not extra information created by a computer.{{cite:shalizi2025_truth_regression}} (Ch. 24, §§24.2–24.4, pp. 390–392){{cite:dodge2008}} (pp. 51–52, “Bootstrap”)

## Intuition
The empirical distribution assigns mass $1/n$ to each observed independent unit. Sampling $n$ times from it with replacement makes some units recur and leaves others out, just as ordinary sampling can produce repeats of similar values and miss others. For every bootstrap sample, apply exactly the statistic or fitting procedure used on the original sample. The spread of those recalculated values describes uncertainty *conditional on the observed empirical distribution*. Its usefulness depends on how well that distribution represents the population and whether the resampling preserves the sampling design.{{cite:shalizi2025_truth_regression}} (Ch. 24, §§24.3–24.6, pp. 391–400)

## Definition
Given independent observations $x_1,\ldots,x_n$, let $\widehat F_n=n^{-1}\sum_i\delta_{x_i}$ and $\widehat\theta=T(x_1,\ldots,x_n)$. A nonparametric bootstrap replicate $X_1^*,\ldots,X_n^*$ is sampled independently from $\widehat F_n$ and produces $\widehat\theta^*=T(X_1^*,\ldots,X_n^*)$. Repeating this construction approximates the conditional distribution of $\widehat\theta^*$ given the data, which is used as a stand-in for the sampling distribution of $\widehat\theta$. The approximation is about a statistic under a sampling model; it does not make the observed cases a new independent study.{{cite:shalizi2025_truth_regression}} (Ch. 24, §24.4, p. 391){{cite:dodge2008}} (pp. 51–52, algorithm)

## Interpretation
The $0.632$ calculation concerns membership of a particular original case in a size-$n$ bootstrap sample. It does not mean that every draw has exactly $0.632n$ different cases, nor that a $0.632$ error correction is exact. For estimating a statistic's standard error, the conditional standard deviation of its bootstrap replicates is the direct quantity. Percentile intervals use their ordered values; they may need refinement when the statistic is biased, skewed, near a boundary, or unstable under resampling.{{cite:shalizi2025_truth_regression}} (Ch. 24, §§24.4 and 24.6, pp. 391, 399–400; Ch. 25, §25.1, pp. 402–403)

## Properties
For a sample mean, the bootstrap variance is available without simulation: $\operatorname{Var}_*(\overline X^*)=n^{-2}\sum_i(x_i-\bar x)^2$. It is slightly smaller than the usual plug-in $s^2/n$ because the empirical distribution uses divisor $n$ rather than $n-1$ for its variance. The same simple formula need not exist for a median, fitted model or nonlinear statistic; that is where resampling earns its computational cost. Increasing the number of replicates reduces Monte Carlo error but does not repair a poor approximation $\widehat F_n\approx F$.{{cite:shalizi2025_truth_regression}} (Ch. 24, §§24.3–24.4 and 24.6, pp. 391–392, 399–400)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Conditional on the data, one bootstrap draw has mean $\bar x$ and variance $n^{-1}\sum_i(x_i-\bar x)^2$. The $n$ draws are conditionally independent, so dividing their sum by $n$ gives $\operatorname{Var}_*(\overline X^*)=n^{-2}\sum_i(x_i-\bar x)^2$. For an original case $i$, each draw misses it with probability $1-1/n$; all $n$ draws miss it with probability $(1-1/n)^n$. Thus its inclusion indicator has expectation $1-(1-1/n)^n$, and summing indicators gives expected distinct-case count $n[1-(1-1/n)^n]$. The limit is $n(1-e^{-1})$ in the sense that the expected fraction tends to $1-e^{-1}$.{{cite:shalizi2025_truth_regression}} (Ch. 24, §§24.3–24.4, pp. 391–392)
:::
:::

## Statistical use
Choose the resampling unit from the data-generating design. For independent people, resample people; for repeated visits to each person, resample whole people with their visits rather than treating visits as independent. In regression, resampling complete $(x,y)$ cases targets variation under random predictors, while residual resampling assumes a suitable fitted mean and a shared error distribution across predictor values. A parametric bootstrap simulates from a fitted probability model and inherits that model's assumptions. Refit every tuning step within each replicate if its variation is part of the target procedure.{{cite:shalizi2025_truth_regression}} (Ch. 24, §24.5–24.6, pp. 392–400)

If ten visits come from each of five people, resampling 50 visits independently breaks within-person dependence and generally understates uncertainty for a population of people. Resampling individual time points from an autocorrelated series destroys its serial structure. An empirical sample with no rare events cannot generate one in ordinary nonparametric resamples, so a tail-risk estimate can be severely optimistic. Residual resampling under strongly changing error variance also erases the variance pattern; resampling whole cases or using a design-aware alternative targets a different, more appropriate law.{{cite:shalizi2025_truth_regression}} (Ch. 24, §§24.5–24.6, pp. 398–400)

## Worked example
Take the observed sample $(2,4,6)$, whose mean is $4$. There are $3^3=27$ equally likely ordered bootstrap samples. Their means are $2,8/3,10/3,4,14/3,16/3,6$, with respective counts $1,3,6,7,6,3,1$. Thus the exact conditional bootstrap mean is $4$, and its variance is $[(2-4)^2+(4-4)^2+(6-4)^2]/3^2=8/9$. The bootstrap standard error is $\sqrt8/3\approx0.943$. Enumerating all draws avoids simulation error in this tiny illustration; it cannot eliminate the gap between the empirical distribution and the population.{{cite:shalizi2025_truth_regression}} (Ch. 24, §§24.3–24.4, pp. 391–392)

**Your turn.** The observed sample is $(1,3)$. List the four equally likely ordered bootstrap samples, their means, and the bootstrap standard error of the sample mean.

::: {.callout-tip collapse="true" title="Answer"}
The samples $(1,1),(1,3),(3,1),(3,3)$ give means $1,2,2,3$. Their conditional mean is $2$ and variance is $[(1-2)^2+0+0+(3-2)^2]/4=1/2$, so the standard error is $1/\sqrt2\approx0.707$. This estimates the mean's sampling spread under the two-point empirical distribution.
:::

## Common misconceptions
The bootstrap does not simulate fresh draws from the unknown population; it simulates from a fitted substitute. More replicates can reduce numerical noise but cannot compensate for a tiny or biased original sample. The $0.632$ membership probability is not a fixed training-set fraction in every draw, and an out-of-bag error estimate is not automatically unbiased. Finally, a bootstrap interval is a repeated-sampling construction, not a posterior probability statement about the parameter after observing the data.{{cite:shalizi2025_truth_regression}} (Ch. 24, §24.6, pp. 399–400)

## Connections
The [jackknife](jackknife-bias-and-standard-error.qmd) changes the sample by omitting cases in a systematic way; a [parametric bootstrap](../notes/sl-05-mixtures-em.qmd#s-uncertainty-about-the-parameters) draws from a fitted model. The [resampling-unit question](../questions/ex-ur-bootstrap-unit.qmd) tests dependence preservation, the [$0.632$ question](../questions/ex-sl-09-3.qmd) distinguishes inclusion from error correction, and the [overfit-tree question](../questions/ex-sl-12-6.qmd) asks why apparent error does not replace validation or an appropriate out-of-bag calculation.{{cite:shalizi2025_truth_regression}} (Ch. 24, §§24.5–24.6, pp. 392–400)

## History
Efron's 1979 bootstrap paper framed resampling as a general way to approximate the sampling distribution of a statistic and connected it to the earlier jackknife. Computer simulation of the bootstrap was then used for standard errors, bias and intervals. The modern method has many variants because the distribution to simulate must reflect the sampling units and model assumptions of the actual problem.{{cite:shalizi2025_truth_regression}} (Ch. 24, §24.7, p. 401){{cite:dodge2008}} (pp. 51–53, “Bootstrap”)
