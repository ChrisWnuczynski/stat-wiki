## Motivating example

A help desk receives requests at a roughly steady average rate, but the exact count in any quarter hour is unpredictable. If a homogeneous Poisson-process model is plausible and the rate is four requests per hour, a quarter hour has expected count one. The Poisson distribution then gives probabilities for zero, one, two and more requests in that fixed interval. The *process* assumption says more than the marginal count law: it also asserts the independence and stability needed to carry one rate across disjoint intervals.{{cite:siegrist2022_poisson_distribution}} (§4, “Basic Theory,” counting process and probability function)

## Intuition

The parameter $\lambda$ is an expected *count for a specified exposure*, not automatically a rate per hour. When events occur at rate $r$ per hour for $t$ hours, $\lambda=rt$. Shortening the window makes both the expected count and its Poisson variance smaller. The probability of no events, $e^{-\lambda}$, falls as exposure grows; the remaining probability is spread over increasingly many positive counts. At a small mean the distribution piles up near zero and is right-skewed, while a large mean gives a more nearly symmetric mound.{{cite:siegrist2022_poisson_distribution}} (§4, “Basic Theory,” probability function, moments and normal approximation){{cite:nist_handbook2002}} (§1.3.6.6.19, Poisson Distribution)

## Definition

For $\lambda>0$, $X\sim\operatorname{Poisson}(\lambda)$ means $X$ takes values $0,1,2,\ldots$ with $\Pr(X=k)=e^{-\lambda}\lambda^k/k!$. The probabilities sum to one because the exponential series gives $e^{-\lambda}\sum_{k=0}^{\infty}\lambda^k/k!=1$. The convention $\lambda=0$ can be added as a limiting point mass at zero, although the infobox states the ordinary positive-parameter family. The CDF at a noninteger threshold $x$ is the same as at $\lfloor x\rfloor$; a count has no mass between consecutive integers.{{cite:siegrist2022_poisson_distribution}} (§4, “Basic Theory,” probability and distribution functions){{cite:nist_handbook2002}} (§1.3.6.6.19, probability and cumulative functions)

The equal mean and variance, both $\lambda$, describe repeated counts under one fixed rate and exposure. They do not say that an observed sample mean must exactly equal its observed sample variance. Sampling fluctuation alone can separate those two summaries, particularly when there are few windows. Persistent excess variance across comparable windows can instead reveal a varying rate, clustering, or dependence. Persistent *under*dispersion can arise when opportunities are constrained, as when at most one event may occur in each window. {{cite:siegrist2022_poisson_distribution}} (§4, “Moments”){{cite:nist_handbook2002}} (§1.3.6.6.19, Common Statistics)

The ratio of successive masses is $\Pr(X=k+1)/\Pr(X=k)=\lambda/(k+1)$. Counts gain probability as $k$ rises while $k+1<\lambda$ and lose probability afterwards. That explains the infobox mode: if $\lambda$ is an integer, the counts $\lambda-1$ and $\lambda$ tie; otherwise the sole mode is $\lfloor\lambda\rfloor$. It also gives a simple way to tabulate the masses for moderate means: begin with $p(0)=e^{-\lambda}$ and successively multiply by $\lambda/(k+1)$, rather than repeatedly computing large factorials. {{cite:siegrist2022_poisson_distribution}} (§4, “Basic Theory,” modes){{cite:nist_handbook2002}} (§1.3.6.6.19, Common Statistics) The weak point is the starting value. In double-precision arithmetic $e^{-\lambda}$ loses relative accuracy once $\lambda$ exceeds about $708$ and rounds to exactly $0$ beyond about $745$, and every later product is then $0$ as well. At $\lambda=1000$ the recurrence therefore returns $0$ even at the tied modes $999$ and $1000$, each of which has probability about $0.01261$. For large means, work with log probabilities instead: in R, `dpois(k, lambda, log = TRUE)` returns $\log\Pr(X=k)$. {{cite:r_stats_poisson2026}} (§Usage and §Arguments, `log`)

## Properties

Independent Poisson counts add because their probability-generating functions multiply to the generating function of another Poisson count. In contrast, observing that each of two counts is marginally Poisson is not enough to conclude their sum is Poisson: the independence condition matters. The Poisson limit of binomial rare-event counts offers a second route to the law. It requires many opportunities with small individual probabilities and a stable total expectation, not merely a large number of trials.{{cite:siegrist2022_poisson_distribution}} (§4, “Sums” and “The Binomial Distribution”){{cite:dodge2008}} (pp. 425–426, “Poisson Distribution,” history and mathematical aspects)

In the homogeneous Poisson process, independent increments give $N(t)-N(s)\sim\operatorname{Poisson}\{r(t-s)\}$ for $t>s$. The wait to the first event exceeds $t$ exactly when $N(t)=0$, so its survival probability is $e^{-rt}$. This count–wait duality is useful for translating questions about arrivals into questions about empty intervals. It depends on the process model; a single Poisson-distributed count for one interval does not establish independent increments at every scale. {{cite:siegrist2022_poisson_distribution}} (§4, “Basic Theory,” counting process and probability function)

## Statistical inference

For counts observed over unequal exposures, use $\lambda_i=r_i t_i$ and keep the rate and exposure units explicit. If one constant rate is assumed, the total count over independent windows divided by their total exposure estimates that rate. In a Poisson regression, a log exposure offset permits the rate to depend on predictors while maintaining the appropriate expected count for each observation. The mean–variance equality then supplies a diagnostic baseline; it should be checked against residuals and grouped counts before relying on model-based uncertainty.{{cite:siegrist2022_poisson_distribution}} (§4, “Basic Theory,” dependence on rate times exposure){{cite:nist_handbook2002}} (§1.3.6.6.19, mean, variance and parameter estimation)

A half-hour window asks for both a count probability and a waiting-time probability, and independent Poisson counts determine the precision of the sample mean as an estimator of $\lambda$. Neither calculation is settled by the name of the distribution alone: the exposure and the sampling model determine which formula applies. {{cite:siegrist2022_poisson_distribution}} (§4, “Basic Theory” and “Moments”)

## Worked example

At four help-desk requests per hour, a fifteen-minute window has $t=1/4$ hour and $\lambda=4(1/4)=1$. Thus $\Pr\{N(1/4)=0\}=e^{-1}\approx0.3679$. The chance of at least two requests is the complement of zero or one: $1-e^{-1}(1+1)=1-2e^{-1}\approx0.2642$. The first probability is the chance of an idle quarter hour; the second is the chance that one available worker would face overlapping requests if each request took the entire window. The Poisson calculation counts arrivals and does not itself model service times.{{cite:siegrist2022_poisson_distribution}} (§4, “Basic Theory,” probability function and count–wait duality)

To see what a varying rate does, suppose half the windows have mean $1$ and half have mean $9$, with a Poisson count conditional on that mean. The pooled mean is $5$. The law of total variance gives $\operatorname{Var}(Y)=\E(\Lambda)+\operatorname{Var}(\Lambda)=5+16=21$, far above the pooled mean. A Poisson fit with mean $5$ misses this extra variability because it treats the rate as fixed. {{cite:siegrist2022_poisson_distribution}} (§4, “Moments,” conditional Poisson variance)

**Your turn.** A station receives events at a steady rate of two per hour. Under a homogeneous Poisson-process model, find the mean number in ninety minutes and the probability of at most one event in that period.

::: {.callout-tip collapse="true" title="Answer"}
Ninety minutes is $3/2$ hours, so $\lambda=2(3/2)=3$. The probability is $\Pr\{N(3/2)\le1\}=e^{-3}(1+3)=4e^{-3}\approx0.1991$. The mean is an expected count over the specified exposure; it is not a count guaranteed in every such window.
:::

For a Poisson count with mean 2.5, which integer is the unique mode, and what is the probability of a zero count?

::: {.callout-tip collapse="true" title="Answer"}
Because 2.5 is not an integer, the unique mode is $\lfloor 2.5\rfloor=2$. The zero probability is $e^{-2.5}\approx 0.082085$.
:::

## Common misconceptions

A Poisson mean is not automatically an hourly rate: its unit is an expected count for the stated window. A Poisson *marginal* count does not by itself imply independent arrivals or exponential waits; those require a process assumption. “Mean equals variance” is a model property, not an identity that every finite dataset must satisfy. And a rare-event approximation is not justified merely because $n$ is large: the individual success probability must be small enough that its dependence on $n$ leaves a stable expected total.{{cite:siegrist2022_poisson_distribution}} (§4, “Basic Theory,” “Moments,” and “The Binomial Distribution”)

## Assumptions and limits — When a fixed rate fails

The equal-mean–variance rule fails for the mixed-rate example: $21$ rather than $5$ is the pooled variance. If events arrive in bursts, adjacent windows can be correlated and the independent-increment process description fails even if individual window histograms look roughly Poisson. If each window permits at most one event with probability $1/2$, its Bernoulli count has mean $1/2$ and variance $1/4$, below the Poisson variance $1/2$. These concrete alternatives show why count support alone cannot identify the law.{{cite:siegrist2022_poisson_distribution}} (§4, “Moments” and “Basic Theory”){{cite:nist_handbook2002}} (§1.3.6.6.19, Common Statistics)

## Connections

The [binomial distribution](binomial-distribution.qmd) approaches the Poisson law under rare independent opportunities. The [homogeneous Poisson process](homogeneous-poisson-process.qmd) gives Poisson counts in time and exponential first waits. The [Gamma distribution](gamma-distribution.qmd) describes later arrival times and can be a prior for an uncertain event rate. [Poisson regression](poisson-regression.qmd) extends the expected count to predictor-dependent exposures, while the [negative binomial distribution](negative-binomial-distribution.qmd) allows greater count variance than the fixed-rate Poisson rule.{{cite:siegrist2022_poisson_distribution}} (§4, “Basic Theory,” “Sums,” and “The Binomial Distribution”)

## History

Poisson's 1837 work obtained the count law as a limit of binomial probabilities, the route preserved in the theorem above. Later uses in time and space made it a standard model for arrivals, defects and other counts. Dodge's account notes these applications while deriving the equal mean and variance and showing how a count of errors per page can be calculated from the mass function.{{cite:dodge2008}} (pp. 425–426, “History,” “Mathematical Aspects,” and “Domains and Limitations”)
