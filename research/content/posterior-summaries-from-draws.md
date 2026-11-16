## Motivating example

A posterior distribution may be easy to sample even when its mean or quantiles have no convenient closed form. Each simulated parameter value is one draw from that distribution, so averages, event counts, and ordered draws can approximate different posterior questions. The accuracy of those approximations depends on how the draws were obtained. Geyer's 1992 analysis made the dependence in Markov-chain output central: a long list of draws is not the same as an equally long independent sample.{{cite:geyer1992}} (§§1–3, pp. 473–479){{cite:wang2025_foundations}} (Ch. 20, §§24.1, 28.1)

## Statement

The three displayed summaries answer different questions. The average estimates a posterior expectation, the sample variance describes posterior spread, and the fraction of draws below $c$ estimates a posterior probability. Ordering the draws gives an empirical median or interval. These are *numerical approximations to properties of one posterior distribution*, not new posterior distributions. The familiar $L-1$ denominator makes the sample variance unbiased for iid draws with a finite second moment; for autocorrelated MCMC draws, consistency can still hold under ergodicity, but the finite-sample unbiasedness argument does not carry over.{{cite:geyer1992}} (§§1–3, pp. 473–479){{cite:wang2025_foundations}} (Ch. 20, §§24.1, 28.1)

## Intuition

An indicator such as $\mathbf1\{\theta<c\}$ turns a probability question into an average of zeros and ones. A quantile asks where the required fraction of sorted values has accumulated. A mean uses the *distances* of all draws from zero, so extreme values can move it much more than they move a median. The distinction is useful when a skewed posterior makes its mean, median, and interval tell different parts of the story.{{cite:wang2025_foundations}} (Ch. 20, §§24.1, 28.1)

## Proof

For iid posterior draws with $\mathbb E|\theta|<\infty$, the law of large numbers sends the draw average to $\mathbb E(\theta\mid x)$. Applying it to the bounded indicator $\mathbf1\{\theta<c\}$ sends its average to $\Pr(\theta<c\mid x)$ at the specified threshold. If $\mathbb E(\theta^2\mid x)<\infty$, applying the same law to squared draws and using $s_L^2=\{\sum_l(\theta^{(l)})^2-L\bar\theta^2\}/(L-1)$ gives convergence of the displayed sample variance to $\operatorname{Var}(\theta\mid x)$. For iid draws, expanding the squares around the posterior mean also yields $\mathbb E(s_L^2)=\operatorname{Var}(\theta\mid x)$. At a continuity point of the posterior CDF, empirical quantiles converge to the corresponding posterior quantiles. For a stationary ergodic Markov chain, the ergodic average replaces the iid law of large numbers for integrable functions, but its Monte Carlo variance must account for serial covariance.{{cite:wang2025_foundations}} (Ch. 9, §§18–19; Ch. 20, §§24.1, 28.1){{cite:geyer1992}} (§§1–3, pp. 473–479)

## Statistical use

Specify the target quantity before computing it. For $\Pr(\theta<c\mid x)$, count the strict event $\theta<c$; counting $\theta\le c$ can differ when the posterior has an atom at $c$. For a central interval, report the quantile levels and the software convention, especially with a short sample where adjacent order statistics are far apart. A posterior standard deviation describes uncertainty about $\theta$ under the model; a Monte Carlo standard error describes numerical uncertainty in a simulated estimate. For iid draws the estimated standard error of their mean is $s_L/\sqrt L$; MCMC needs a dependence-adjusted calculation.{{cite:geyer1992}} (§§1–3.6, pp. 473–480){{cite:wang2025_foundations}} (Ch. 20, §28.1)

## Worked example

Suppose five exact independent posterior draws are $1,2,2,3,7$. Their mean is $(1+2+2+3+7)/5=3$. Squared deviations from $3$ sum to $4+1+1+0+16=22$, so the sample variance is $22/(5-1)=5.5$. Two of the five draws exceed $2$, giving $\widehat{\Pr}(\theta>2\mid x)=2/5=0.4$; the empirical median is the third ordered value, $2$. An illustrative iid Monte Carlo standard error for the estimated mean is $\sqrt{5.5/5}\approx1.04881$. It is large because five draws are few; it is not the posterior standard deviation $\sqrt{5.5}\approx2.34521$.{{cite:geyer1992}} (§§1–3, pp. 473–479){{cite:wang2025_foundations}} (Ch. 20, §24.1)

**Your turn.** For five independent draws $0,1,2,2,5$, find their mean, sample variance, empirical median, and the fraction exceeding $1$. Compute the illustrative iid Monte Carlo standard error of their mean.

::: {.callout-tip collapse="true" title="Answer"}
The mean is $(0+1+2+2+5)/5=2$. Squared deviations sum to $4+1+0+0+9=14$, so the sample variance is $14/4=3.5$. The median is $2$, and three draws exceed $1$, giving $3/5=0.6$. The iid Monte Carlo standard error estimate is $\sqrt{3.5/5}\approx0.83666$. That last number estimates uncertainty in the computed mean, not spread of the posterior itself.{{cite:geyer1992}} (§§1–3, pp. 473–479)
:::

## Common misconceptions

The sample variance of posterior draws is not the Monte Carlo variance of their average. A repeated value in a small continuous sample does not identify the posterior density mode; a mode calls for density optimization or deliberate density estimation. More saved MCMC draws do not guarantee the same precision gain as more independent draws, because nearby chain states can be correlated. Finally, an interval between empirical quantiles summarizes posterior uncertainty under the model; it is not a frequentist confidence interval for the simulation algorithm.{{cite:geyer1992}} (§§1–3, pp. 473–479){{cite:wang2025_foundations}} (Ch. 20, §§24.1, 28.1)

## Generalizations — When draw summaries mislead

If a sampler remains in one mode of a bimodal posterior, its empirical mean and quantiles describe that mode alone, even if thousands of values were saved. If the posterior has a Cauchy-like tail, a finite posterior mean does not exist and the draw average has no stable expectation target. If a posterior has a point mass at the threshold $c$, the distinction between $<c$ and $\le c$ is substantive. For dependent chains, a naive $s_L/\sqrt L$ can understate Monte Carlo error when autocorrelation is positive. Each failure calls for checking the target, sampler, or summary rather than merely changing the number of displayed digits.{{cite:geyer1992}} (§§1–3.7, pp. 473–480){{cite:wang2025_foundations}} (Ch. 20, §§24.1, 28.1)

## Related concepts

[Posterior mean](posterior-mean.qmd) and [posterior median](posterior-median.qmd) are population features that a draw sample estimates. [Credible-region constructions](credible-region-constructions.qmd) explains the interval targets; [effective sample size](effective-sample-size.qmd) and [autocorrelation](autocorrelation-function.qmd) explain why a dependent chain contains less independent information than its draw count suggests.{{cite:geyer1992}} (§§1–3, pp. 473–479){{cite:wang2025_foundations}} (Ch. 20, §§24.1, 28.1)
